# src/main.py

import itertools
import os
import json
from .mapa import Mapa
from .astar import astar_search
from .visualizacao import gerar_imagem_mapa

def carregar_configuracao(arquivo_config="config.json"):
    """Lê o arquivo de configuração JSON e retorna os pontos de interesse."""
    try:
        with open(arquivo_config, 'r') as f:
            config = json.load(f)
        pontos = config["pontos_de_interesse"]
        for key, value in pontos.items():
            pontos[key] = tuple(value)
        return pontos
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo de configuração '{arquivo_config}' não encontrado.")
    except KeyError:
        raise KeyError("Chave 'pontos_de_interesse' não encontrada no arquivo de configuração.")

def verificar_mapas(mapas_e_pontos):
    for nome, mapa, entrada, pingente in mapas_e_pontos:
        if mapa.get_custo(entrada) == float('inf'):
            raise ValueError(f"Ponto de ENTRADA {entrada} da {nome} está sobre uma parede!")
        if mapa.get_custo(pingente) == float('inf'):
            raise ValueError(f"Ponto do PINGENTE {pingente} da {nome} está sobre uma parede!")
    return True

def calcular_custo_masmorra(mapa_masmorra, entrada, pingente):
    caminho_ida, custo_ida = astar_search(mapa_masmorra, entrada, pingente)
    if not caminho_ida: return None
    caminho_volta, custo_volta = astar_search(mapa_masmorra, pingente, entrada)
    if not caminho_volta: return None
    return custo_ida + custo_volta

def visualizar_jornada_otima(ordem, mapas, pontos, pasta_resultados):
    print("\n\n--- Gerando Imagens da Jornada Ótima ---")
    mapa_hyrule = mapas["hyrule"]
    info_masmorras = {
        "M1": {"mapa": mapas["m1"], "entrada": pontos["M1_ENTRADA"], "pingente": pontos["M1_PINGENTE"]},
        "M2": {"mapa": mapas["m2"], "entrada": pontos["M2_ENTRADA"], "pingente": pontos["M2_PINGENTE"]},
        "M3": {"mapa": mapas["m3"], "entrada": pontos["M3_ENTRADA"], "pingente": pontos["M3_PINGENTE"]},
    }
    pontos_hyrule = {
        "INICIO": pontos["CASA_LINK"],
        "M1": pontos["MASMORRA_1_ENTRADA_HYRULE"], "M2": pontos["MASMORRA_2_ENTRADA_HYRULE"],
        "M3": pontos["MASMORRA_3_ENTRADA_HYRULE"], "FIM": pontos["LOST_WOODS"]
    }

    passo_counter = 1
    for i in range(len(ordem) - 1):
        p_partida, p_chegada = ordem[i], ordem[i+1]
        c_partida, c_chegada = pontos_hyrule[p_partida], pontos_hyrule[p_chegada]
        caminho, _ = astar_search(mapa_hyrule, c_partida, c_chegada)
        nome_arquivo = os.path.join(pasta_resultados, f"{passo_counter:02d}_jornada_{p_partida}_para_{p_chegada}.png")
        gerar_imagem_mapa(mapa_hyrule, caminho, c_partida, c_chegada, nome_arquivo)
        passo_counter += 1
        
        if p_chegada in info_masmorras:
            info = info_masmorras[p_chegada]
            caminho_ida, _ = astar_search(info["mapa"], info["entrada"], info["pingente"])
            nome_ida = os.path.join(pasta_resultados, f"{passo_counter:02d}_jornada_{p_chegada}_ida.png")
            gerar_imagem_mapa(info["mapa"], caminho_ida, info["entrada"], info["pingente"], nome_ida, is_dungeon=True)
            passo_counter += 1
            
            caminho_volta, _ = astar_search(info["mapa"], info["pingente"], info["entrada"])
            nome_volta = os.path.join(pasta_resultados, f"{passo_counter:02d}_jornada_{p_chegada}_volta.png")
            gerar_imagem_mapa(info["mapa"], caminho_volta, info["pingente"], info["entrada"], nome_volta, is_dungeon=True)
            passo_counter += 1

def main():
    try:
        PASTA_RESULTADOS = "imagens_geradas"
        if not os.path.exists(PASTA_RESULTADOS):
            os.makedirs(PASTA_RESULTADOS)
        else:
            for arquivo in os.listdir(PASTA_RESULTADOS):
                os.remove(os.path.join(PASTA_RESULTADOS, arquivo))

        print("\n--- A Lenda de Link: Em Busca da Rota Ótima ---")
        PONTOS = carregar_configuracao()
        print("Carregando mapas...")
        mapa_hyrule = Mapa("hyrule.txt")
        mapa_m1 = Mapa("masmorra1.txt")
        mapa_m2 = Mapa("masmorra2.txt")
        mapa_m3 = Mapa("masmorra3.txt")

        verificar_mapas([
            ("M1", mapa_m1, PONTOS["M1_ENTRADA"], PONTOS["M1_PINGENTE"]),
            ("M2", mapa_m2, PONTOS["M2_ENTRADA"], PONTOS["M2_PINGENTE"]),
            ("M3", mapa_m3, PONTOS["M3_ENTRADA"], PONTOS["M3_PINGENTE"]),
        ])

        print("\nCalculando custos internos das masmorras...")
        custos_internos = {
            "M1": calcular_custo_masmorra(mapa_m1, PONTOS["M1_ENTRADA"], PONTOS["M1_PINGENTE"]),
            "M2": calcular_custo_masmorra(mapa_m2, PONTOS["M2_ENTRADA"], PONTOS["M2_PINGENTE"]),
            "M3": calcular_custo_masmorra(mapa_m3, PONTOS["M3_ENTRADA"], PONTOS["M3_PINGENTE"])
        }
        for masmorra, custo in custos_internos.items():
            print(f"Custo para completar a {masmorra}: {custo}")

        print("\nCalculando custos de percurso em Hyrule...")
        pontos_hyrule_principais = {
            "INICIO": PONTOS["CASA_LINK"], "M1": PONTOS["MASMORRA_1_ENTRADA_HYRULE"],
            "M2": PONTOS["MASMORRA_2_ENTRADA_HYRULE"], "M3": PONTOS["MASMORRA_3_ENTRADA_HYRULE"],
            "FIM": PONTOS["LOST_WOODS"]
        }
        custos_percursos = {}
        for p1, p2 in itertools.combinations(pontos_hyrule_principais.keys(), 2):
            _, custo = astar_search(mapa_hyrule, pontos_hyrule_principais[p1], pontos_hyrule_principais[p2])
            if custo > 0:
                custos_percursos[f"{p1}-{p2}"] = custo
                custos_percursos[f"{p2}-{p1}"] = custo
            else:
                raise ValueError(f"Não foi possível encontrar caminho entre {p1} e {p2}.")

        print("\nAnalisando as ordens de visita das masmorras...")
        ordens = list(itertools.permutations(["M1", "M2", "M3"]))
        melhor_ordem, menor_custo_total = None, float('inf')
        for ordem in ordens:
            ponto_atual, custo_total_ordem = "INICIO", 0
            percurso_str = ["INICIO"]
            for proxima_masmorra in ordem:
                custo_total_ordem += custos_percursos[f"{ponto_atual}-{proxima_masmorra}"]
                custo_total_ordem += custos_internos[proxima_masmorra]
                ponto_atual = proxima_masmorra
                percurso_str.append(proxima_masmorra)
            custo_total_ordem += custos_percursos[f"{ponto_atual}-FIM"]
            percurso_str.append("FIM")
            
            print(f"Ordem {' -> '.join(percurso_str)}: Custo Total = {custo_total_ordem}")
            
            if custo_total_ordem < menor_custo_total:
                menor_custo_total = custo_total_ordem
                melhor_ordem = percurso_str
        
        print("\n--- Resultado Final ---")
        print(f"A melhor ordem para visitar as masmorras é: {' -> '.join(melhor_ordem)}")
        print(f"O menor custo total para completar a jornada é: {menor_custo_total}")
        visualizar_jornada_otima(melhor_ordem, {"hyrule": mapa_hyrule, "m1": mapa_m1, "m2": mapa_m2, "m3": mapa_m3}, PONTOS, PASTA_RESULTADOS)

    except (ValueError, FileNotFoundError, KeyError) as e:
        print(f"\nERRO NA EXECUÇÃO: {e}")

if __name__ == '__main__':
    main()
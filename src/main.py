# src/main.py

import itertools
import os
from .mapa import Mapa
from .astar import astar_search
from .visualizacao import gerar_imagem_mapa

# --- DEFINIÇÃO DOS PONTOS DE INTERESSE ---
PONTOS = {
    "CASA_LINK": (24, 27),
    "LOST_WOODS": (6, 5),
    "MASMORRA_1_ENTRADA_HYRULE": (24, 1),
    "MASMORRA_2_ENTRADA_HYRULE": (39, 17),
    "MASMORRA_3_ENTRADA_HYRULE": (5, 33),
    "M1_ENTRADA": (14, 26), 
    "M1_PINGENTE": (3, 13),
    "M2_ENTRADA": (13, 25), 
    "M2_PINGENTE": (13, 2),
    "M3_ENTRADA": (14, 25), 
    "M3_PINGENTE": (15, 19)
}

def verificar_mapas(mapas_e_pontos):
    for nome, mapa, entrada, pingente in mapas_e_pontos:
        if mapa.get_custo(entrada) == float('inf'):
            print(f"ERRO DE VERIFICAÇÃO: Ponto de ENTRADA {entrada} da {nome} está sobre uma parede!")
            return False
        if mapa.get_custo(pingente) == float('inf'):
            print(f"ERRO DE VERIFICAÇÃO: Ponto do PINGENTE {pingente} da {nome} está sobre uma parede!")
            return False
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
        ponto_de_partida_nome = ordem[i]
        ponto_de_chegada_nome = ordem[i+1]
        
        partida_coord = pontos_hyrule[ponto_de_partida_nome]
        chegada_coord = pontos_hyrule[ponto_de_chegada_nome]
        
        caminho, _ = astar_search(mapa_hyrule, partida_coord, chegada_coord)
        
        nome_base = f"{passo_counter:02d}_jornada_{ponto_de_partida_nome}_para_{ponto_de_chegada_nome}.png"
        caminho_completo_arquivo = os.path.join(pasta_resultados, nome_base)
        gerar_imagem_mapa(mapa_hyrule, caminho, partida_coord, chegada_coord, caminho_completo_arquivo)
        passo_counter += 1
        
        if ponto_de_chegada_nome in info_masmorras:
            masmorra_info = info_masmorras[ponto_de_chegada_nome]
            
            caminho_ida, _ = astar_search(masmorra_info["mapa"], masmorra_info["entrada"], masmorra_info["pingente"])
            nome_base_ida = f"{passo_counter:02d}_jornada_{ponto_de_chegada_nome}_ida.png"
            caminho_completo_ida = os.path.join(pasta_resultados, nome_base_ida)
            gerar_imagem_mapa(masmorra_info["mapa"], caminho_ida, masmorra_info["entrada"], masmorra_info["pingente"], caminho_completo_ida, is_dungeon=True)
            passo_counter += 1
            
            caminho_volta, _ = astar_search(masmorra_info["mapa"], masmorra_info["pingente"], masmorra_info["entrada"])
            nome_base_volta = f"{passo_counter:02d}_jornada_{ponto_de_chegada_nome}_volta.png"
            caminho_completo_volta = os.path.join(pasta_resultados, nome_base_volta)
            gerar_imagem_mapa(masmorra_info["mapa"], caminho_volta, masmorra_info["pingente"], masmorra_info["entrada"], caminho_completo_volta, is_dungeon=True)
            passo_counter += 1

def main():
    PASTA_RESULTADOS = "imagens_geradas"
    if not os.path.exists(PASTA_RESULTADOS):
        os.makedirs(PASTA_RESULTADOS)
        print(f"Pasta '{PASTA_RESULTADOS}' criada.")
    else:
        print(f"Limpando pasta '{PASTA_RESULTADOS}'...")
        for arquivo in os.listdir(PASTA_RESULTADOS):
            os.remove(os.path.join(PASTA_RESULTADOS, arquivo))

    print("\n--- A Lenda de Link: Em Busca da Rota Ótima ---")
    print("Carregando mapas...")
    
    mapa_hyrule = Mapa("hyrule.txt")
    # Chamadas simplificadas, sem o parâmetro 'is_dungeon'
    mapa_m1 = Mapa("masmorra1.txt")
    mapa_m2 = Mapa("masmorra2.txt")
    mapa_m3 = Mapa("masmorra3.txt")

    if not verificar_mapas([
        ("M1", mapa_m1, PONTOS["M1_ENTRADA"], PONTOS["M1_PINGENTE"]),
        ("M2", mapa_m2, PONTOS["M2_ENTRADA"], PONTOS["M2_PINGENTE"]),
        ("M3", mapa_m3, PONTOS["M3_ENTRADA"], PONTOS["M3_PINGENTE"]),
    ]):
        print("\nCorrija as coordenadas em main.py ou o mapa em .txt e tente novamente.")
        return

    print("\nCalculando custos internos das masmorras...")
    custos_internos = {
        "M1": calcular_custo_masmorra(mapa_m1, PONTOS["M1_ENTRADA"], PONTOS["M1_PINGENTE"]),
        "M2": calcular_custo_masmorra(mapa_m2, PONTOS["M2_ENTRADA"], PONTOS["M2_PINGENTE"]),
        "M3": calcular_custo_masmorra(mapa_m3, PONTOS["M3_ENTRADA"], PONTOS["M3_PINGENTE"])
    }

    for masmorra, custo in custos_internos.items():
        if custo is None:
            print(f"ERRO CRÍTICO: Não foi possível calcular a rota interna da {masmorra}.")
            return
        print(f"Custo para completar a {masmorra}: {custo}")

    print("\nCalculando custos de percurso em Hyrule...")
    pontos_hyrule_principais = {
        "INICIO": PONTOS["CASA_LINK"],
        "M1": PONTOS["MASMORRA_1_ENTRADA_HYRULE"],
        "M2": PONTOS["MASMORRA_2_ENTRADA_HYRULE"],
        "M3": PONTOS["MASMORRA_3_ENTRADA_HYRULE"],
        "FIM": PONTOS["LOST_WOODS"]
    }
    custos_percursos = {}
    for p1, p2 in itertools.combinations(pontos_hyrule_principais.keys(), 2):
        print(f"Calculando rota de {p1} para {p2}...")
        _, custo = astar_search(mapa_hyrule, pontos_hyrule_principais[p1], pontos_hyrule_principais[p2])
        if custo > 0:
            custos_percursos[f"{p1}-{p2}"] = custo
            custos_percursos[f"{p2}-{p1}"] = custo
        else:
            print(f"ERRO: Não foi possível encontrar caminho entre {p1} e {p2}.")
            return

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
    if melhor_ordem:
        print(f"A melhor ordem para visitar as masmorras é: {' -> '.join(melhor_ordem)}")
        print(f"O menor custo total para completar a jornada é: {menor_custo_total}")
        
        visualizar_jornada_otima(melhor_ordem, 
                                {"hyrule": mapa_hyrule, "m1": mapa_m1, "m2": mapa_m2, "m3": mapa_m3}, 
                                PONTOS,
                                PASTA_RESULTADOS)
    else:
        print("Não foi possível encontrar uma rota válida para completar a missão.")

if __name__ == '__main__':
    main()
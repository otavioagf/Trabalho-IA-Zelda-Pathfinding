# src/main.py

import itertools
from .mapa import Mapa
from .astar import astar_search

# --- DEFINIÇÃO DOS PONTOS DE INTERESSE ---
PONTOS = {
    "CASA_LINK": (24, 27),
    "LOST_WOODS": (6, 5),
    "MASMORRA_1_ENTRADA_HYRULE": (32, 5),
    "MASMORRA_2_ENTRADA_HYRULE": (17, 39),
    "MASMORRA_3_ENTRADA_HYRULE": (1, 24),
    "M1_ENTRADA": (14, 26), 
    "M1_PINGENTE": (3, 13),
    "M2_ENTRADA": (13, 25), 
    "M2_PINGENTE": (13, 2),
    "M3_ENTRADA": (14, 25), 
    "M3_PINGENTE": (15, 19)
}

def verificar_mapas(mapas_e_pontos):
    """Função de segurança para verificar se os pontos estão em locais caminháveis."""
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

def main():
    print("--- A Lenda de Link: Em Busca da Rota Ótima ---")
    print("Carregando mapas...")
    
    mapa_hyrule = Mapa("hyrule.txt")
    # Ao carregar as masmorras, informamos ao construtor para tratar 'F' como piso
    mapa_m1 = Mapa("masmorra1.txt", is_dungeon=True)
    mapa_m2 = Mapa("masmorra2.txt", is_dungeon=True)
    mapa_m3 = Mapa("masmorra3.txt", is_dungeon=True)

    # --- ETAPA DE VERIFICAÇÃO ---
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
    pontos_hyrule = {
        "INICIO": PONTOS["CASA_LINK"],
        "M1": PONTOS["MASMORRA_1_ENTRADA_HYRULE"],
        "M2": PONTOS["MASMORRA_2_ENTRADA_HYRULE"],
        "M3": PONTOS["MASMORRA_3_ENTRADA_HYRULE"],
        "FIM": PONTOS["LOST_WOODS"]
    }
    custos_percursos = {}
    for p1, p2 in itertools.combinations(pontos_hyrule.keys(), 2):
        print(f"Calculando rota de {p1} para {p2}...")
        _, custo = astar_search(mapa_hyrule, pontos_hyrule[p1], pontos_hyrule[p2])
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
    else:
        print("Não foi possível encontrar uma rota válida para completar a missão.")

if __name__ == '__main__':
    main()
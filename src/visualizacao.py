# src/visualizacao.py

import copy

def desenhar_mapa(mapa, caminho=None, inicio=None, fim=None):
    """
    Desenha o mapa no console, opcionalmente com o caminho, início e fim.
    """
    # Cria uma cópia do grid para não modificar o original
    grid_desenho = copy.deepcopy(mapa.grid)

    # Desenha o caminho no grid
    if caminho:
        for passo in caminho:
            x, y = passo
            # Não sobrescreve o início ou o fim
            if (inicio and passo == inicio) or (fim and passo == fim):
                continue
            grid_desenho[y][x] = '*' # '*' representa o caminho

    # Marca o ponto de início
    if inicio:
        x, y = inicio
        grid_desenho[y][x] = 'I' # 'I' de Início

    # Marca o ponto de fim
    if fim:
        x, y = fim
        grid_desenho[y][x] = 'F' # 'F' de Fim
    
    # Imprime o grid finalizado no console
    for linha in grid_desenho:
        print(" ".join(linha))
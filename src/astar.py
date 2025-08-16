# src/astar.py

import heapq
from .mapa import Mapa

class Node:
    """Representa um nó na grade de busca do A*."""
    def __init__(self, posicao, pai=None):
        self.posicao = posicao
        self.pai = pai
        self.g = 0; self.h = 0; self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def astar_search(mapa, inicio, fim):
    """Executa o algoritmo de busca A* para encontrar o caminho de menor custo.

    Args:
        mapa (Mapa): Uma instância da classe Mapa contendo a grade e os custos.
        inicio (tuple): Uma tupla (x, y) para a posição inicial.
        fim (tuple): Uma tupla (x, y) para a posição de destino.

    Returns:
        tuple: Uma tupla contendo:
            - list: A lista de coordenadas (x, y) do caminho. None se não houver caminho.
            - int: O custo total do caminho. 0 se não houver caminho.
    """
    no_inicio = Node(inicio)
    no_fim = Node(fim)
    lista_aberta = [no_inicio]
    lista_fechada = set()

    while lista_aberta:
        no_atual = heapq.heappop(lista_aberta)
        if no_atual.posicao in lista_fechada:
            continue
        lista_fechada.add(no_atual.posicao)

        if no_atual.posicao == no_fim.posicao:
            caminho, custo_total = [], no_atual.g
            temp = no_atual
            while temp is not None:
                caminho.append(temp.posicao)
                temp = temp.pai
            return caminho[::-1], custo_total

        for nova_posicao in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            posicao_vizinho = (no_atual.posicao[0] + nova_posicao[0], no_atual.posicao[1] + nova_posicao[1])
            if not (0 <= posicao_vizinho[0] < mapa.largura and 0 <= posicao_vizinho[1] < mapa.altura):
                continue
            if mapa.get_custo(posicao_vizinho) == float('inf'):
                continue
            
            vizinho = Node(posicao_vizinho, no_atual)
            vizinho.g = no_atual.g + mapa.get_custo(vizinho.posicao)
            vizinho.h = (abs(vizinho.posicao[0] - no_fim.posicao[0]) + abs(vizinho.posicao[1] - no_fim.posicao[1])) * 10
            vizinho.f = vizinho.g + vizinho.h
            heapq.heappush(lista_aberta, vizinho)
            
    return None, 0
import heapq
from .mapa import Mapa

# Mude para False para desativar as mensagens de depuração
DEBUG = False

class Node:
    def __init__(self, posicao, pai=None):
        self.posicao = posicao
        self.pai = pai
        self.g = 0  # Custo do início até o nó atual
        self.h = 0  # Custo heurístico estimado até o destino
        self.f = 0  # Custo total (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar_search(mapa, inicio, fim):
    no_inicio = Node(inicio)
    no_fim = Node(fim)

    lista_aberta = [no_inicio]  # Fila de prioridade
    lista_fechada = set()       # Um conjunto de posições (x, y) já visitadas

    while lista_aberta:
        no_atual = heapq.heappop(lista_aberta)

        # Se já processamos essa posição, pule
        if no_atual.posicao in lista_fechada:
            continue

        lista_fechada.add(no_atual.posicao)

        # Se alcançamos o destino, reconstrói o caminho
        if no_atual.posicao == no_fim.posicao:
            caminho = []
            custo_total = no_atual.g
            temp = no_atual
            while temp is not None:
                caminho.append(temp.posicao)
                temp = temp.pai
            return caminho[::-1], custo_total

        # Gera vizinhos (adjacentes)
        for nova_posicao in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            posicao_vizinho = (no_atual.posicao[0] + nova_posicao[0], 
                               no_atual.posicao[1] + nova_posicao[1])

            largura, altura = mapa.get_dimensoes()
            if not (0 <= posicao_vizinho[0] < largura and 0 <= posicao_vizinho[1] < altura):
                continue
            
            if mapa.get_custo(posicao_vizinho) == float('inf'):
                continue
            
            vizinho = Node(posicao_vizinho, no_atual)
            vizinho.g = no_atual.g + mapa.get_custo(vizinho.posicao)
            vizinho.h = (abs(vizinho.posicao[0] - no_fim.posicao[0]) + 
                         abs(vizinho.posicao[1] - no_fim.posicao[1])) * 10
            vizinho.f = vizinho.g + vizinho.h

            heapq.heappush(lista_aberta, vizinho)

    return None, 0 # Retorna None se não encontrar caminho

# --- Bloco de Teste ---
if __name__ == '__main__':
    mapa_teste = Mapa("masmorra1.txt")
    inicio_teste = (16, 26)
    fim_teste = (4, 3)

    print(f"Buscando caminho de {inicio_teste} para {fim_teste} na masmorra 1...")

    caminho, custo = astar_search(mapa_teste, inicio_teste, fim_teste)

    if caminho:
        print(f"\nCaminho encontrado com sucesso!")
        print(f"Custo total do caminho: {custo}")
        print(f"Número de passos: {len(caminho)}")
    else:
        print("\nNão foi possível encontrar um caminho.")
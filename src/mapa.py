# src/mapa.py

class Mapa:
    """Representa um mapa do jogo, carregado de um arquivo.

    Esta classe lê um arquivo .txt, armazena a grade do mapa e fornece
    métodos para obter custos de terreno e dimensões.

    Attributes:
        custos (dict): Dicionário que mapeia caracteres de terreno a custos.
        grid (list): Matriz 2D (lista de listas) representando o mapa.
        altura (int): A altura da grade do mapa.
        largura (int): A largura da grade do mapa.
    """
    def __init__(self, nome_arquivo):
        """Inicializa o mapa carregando-o de um arquivo.

        Args:
            nome_arquivo (str): O nome do arquivo a ser carregado da pasta 'maps'.
        """
        self.custos = {
            'G': 10,   # Grama
            'S': 20,   # Areia
            'F': 100,  # Floresta
            'M': 150,  # Montanha
            'A': 180,  # Água
            'P': 10,   # Piso da Masmorra
            'L': 10,   # Link (Posição Inicial)
            'LW': 10,  # Lost Woods
            'MA': 20,  # Entrada da Masmorra (Custo de Areia)
            'MS': 10,  # Master Sword
            'X': float('inf') # Parede ou obstáculo
        }
        
        self.grid = self._carregar_mapa_de_arquivo(nome_arquivo)
        self.altura = len(self.grid)
        self.largura = len(self.grid[0]) if self.altura > 0 else 0

    def _carregar_mapa_de_arquivo(self, nome_arquivo):
        caminho_completo = f"maps/{nome_arquivo}"
        try:
            with open(caminho_completo, 'r') as f:
                linhas = [line.strip().split('\t') for line in f.readlines()]
                if not linhas: return []
                
                max_largura = max(len(l) for l in linhas)
                
                for linha in linhas:
                    linha.extend(['X'] * (max_largura - len(linha)))
                
                return linhas
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo de mapa '{caminho_completo}' não foi encontrado.")

    def get_custo(self, posicao):
        x, y = posicao
        if 0 <= y < self.altura and 0 <= x < self.largura:
            return self.custos.get(self.grid[y][x], float('inf'))
        return float('inf')

    def get_dimensoes(self):
        return (self.largura, self.altura)
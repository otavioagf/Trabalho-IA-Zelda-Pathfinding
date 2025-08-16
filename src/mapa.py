# src/mapa.py

class Mapa:
    """
    Classe responsável por carregar um mapa de um arquivo, armazenar os custos
    de terreno e fornecer informações sobre o mapa.
    """
    def __init__(self, nome_arquivo):
        # Dicionário de custos final e unificado
        self.custos = {
            'G': 10,   # Grama
            'S': 20,   # Areia
            'F': 100,  # Floresta
            'M': 150,  # Montanha
            'A': 180,  # Água
            'P': 10,   # Piso da Masmorra
            'L': 10,   # Link (Posição Inicial)
            'LW': 10,  # Lost Woods
            'MA': 20,  # Masmorra (considerada Areia)
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
                
                max_largura = 0
                for linha in linhas:
                    if len(linha) > max_largura:
                        max_largura = len(linha)
                
                for linha in linhas:
                    while len(linha) < max_largura:
                        linha.append('X')
                
                return linhas
        except FileNotFoundError:
            print(f"Erro: O arquivo '{caminho_completo}' não foi encontrado.")
            return []

    def get_custo(self, posicao):
        x, y = posicao
        if 0 <= y < self.altura and 0 <= x < self.largura:
            tipo_terreno = self.grid[y][x]
            return self.custos.get(tipo_terreno, float('inf'))
        return float('inf')

    def get_dimensoes(self):
        return (self.largura, self.altura)
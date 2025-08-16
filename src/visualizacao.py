# src/visualizacao.py

from PIL import Image, ImageDraw

def gerar_imagem_mapa(mapa, caminho, inicio, fim, nome_arquivo_saida, is_dungeon=False):
    """
    Gera uma imagem PNG do mapa com o caminho desenhado.
    """
    tile_size = 10  # Tamanho de cada quadrado em pixels
    largura, altura = mapa.get_dimensoes()
    
    # Define a paleta de cores com base na sua legenda
    cor_terreno = {
        'G': (144, 238, 144), # Verde claro (Grama)
        'S': (240, 230, 140), # Marrom claro (Areia)
        'F': (0, 100, 0),     # Verde escuro (Floresta)
        'M': (139, 69, 19),   # Marrom (Montanha)
        'A': (0, 0, 255),     # Azul (Água)
        'L': (144, 238, 144), # Link's House (Grama)
        'LW': (144, 238, 144),# Lost Woods (Grama)
        'MA': (105, 105, 105),# Entrada da Masmorra
        'MS': (255, 215, 0),  # Master Sword (Dourado)
        'P': (255, 255, 255), # Piso da Masmorra
        'X': (0, 0, 0)        # Parede da Masmorra
    }

    # Paleta de cores específica para masmorras
    if is_dungeon:
        cor_terreno['F'] = (255, 255, 255) # Piso da masmorra é branco
        cor_terreno['X'] = (0, 0, 0)       # Parede é preta
    
    cor_caminho = (255, 0, 0)   # Vermelho
    cor_inicio = (0, 255, 0)    # Verde (para destacar o início)
    cor_fim = (255, 255, 0)     # Amarelo (para destacar o fim)

    # Cria a imagem
    img = Image.new('RGB', (largura * tile_size, altura * tile_size), 'black')
    draw = ImageDraw.Draw(img)

    # Desenha o mapa base
    for y in range(altura):
        for x in range(largura):
            char = mapa.grid[y][x]
            cor = cor_terreno.get(char, (0, 0, 0)) # Padrão preto para caracteres desconhecidos
            draw.rectangle(
                [x * tile_size, y * tile_size, (x + 1) * tile_size - 1, (y + 1) * tile_size - 1],
                fill=cor
            )
            
    # Desenha o caminho
    if caminho:
        for passo in caminho:
            x, y = passo
            draw.rectangle(
                [x * tile_size + 2, y * tile_size + 2, (x + 1) * tile_size - 3, (y + 1) * tile_size - 3],
                fill=cor_caminho
            )

    # Desenha marcadores de início e fim
    if inicio:
        x, y = inicio
        draw.rectangle([x * tile_size, y * tile_size, (x + 1) * tile_size - 1, (y + 1) * tile_size - 1], fill=cor_inicio)
    if fim:
        x, y = fim
        draw.rectangle([x * tile_size, y * tile_size, (x + 1) * tile_size - 1, (y + 1) * tile_size - 1], fill=cor_fim)
        
    img.save(nome_arquivo_saida)
    print(f"Imagem gerada: {nome_arquivo_saida}")
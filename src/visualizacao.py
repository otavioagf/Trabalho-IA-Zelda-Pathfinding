# src/visualizacao.py

from PIL import Image, ImageDraw
import math

def draw_dashed_line(draw, p1, p2, fill, width, dash_len, gap_len):
    """Desenha uma linha tracejada entre dois pontos."""
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    dist = math.sqrt(dx**2 + dy**2)
    if dist == 0: return
    
    dash_count = int(dist / (dash_len + gap_len))
    dx_step = dx / dist
    dy_step = dy / dist

    for i in range(dash_count + 1):
        start_x = p1[0] + i * (dash_len + gap_len) * dx_step
        start_y = p1[1] + i * (dash_len + gap_len) * dy_step
        
        end_x = start_x + dash_len * dx_step
        end_y = start_y + dash_len * dy_step
        
        draw.line([(start_x, start_y), (end_x, end_y)], fill=fill, width=width)

def gerar_imagem_mapa(mapa, caminho, inicio, fim, nome_arquivo_saida, is_dungeon=False):
    """Gera uma imagem PNG do mapa com o caminho desenhado como uma linha tracejada."""
    tile_size = 10
    largura, altura = mapa.get_dimensoes()
    
    cor_terreno = {
        'G': (144, 238, 144), 'S': (240, 230, 140), 'F': (0, 100, 0),
        'M': (139, 69, 19), 'A': (100, 149, 237), 'L': (144, 238, 144),
        'LW': (144, 238, 144), 'MS': (255, 215, 0), 'P': (255, 255, 255),
        'MA': (240, 230, 140),
        'X': (0, 0, 0)
    }
    if is_dungeon:
        cor_terreno['F'] = (255, 255, 255)
    
    cor_caminho = (255, 0, 0)
    cor_inicio = (0, 255, 0)
    cor_fim = (255, 255, 0)

    img = Image.new('RGB', (largura * tile_size, altura * tile_size), 'black')
    draw = ImageDraw.Draw(img)

    for y in range(altura):
        for x in range(largura):
            char = mapa.grid[y][x]
            cor = cor_terreno.get(char, (0, 0, 0))
            draw.rectangle([x * tile_size, y * tile_size, (x + 1) * tile_size, (y + 1) * tile_size], fill=cor)
            
    if caminho:
        # Converte os passos do caminho para coordenadas de pixel no centro de cada tile
        path_pixels = [(x * tile_size + tile_size // 2, y * tile_size + tile_size // 2) for x, y in caminho]
        
        # Desenha um segmento tracejado entre cada par de pontos no caminho
        for i in range(len(path_pixels) - 1):
            draw_dashed_line(draw, path_pixels[i], path_pixels[i+1], cor_caminho, width=3, dash_len=4, gap_len=2)

    if inicio:
        x, y = inicio
        draw.rectangle([x * tile_size, y * tile_size, (x + 1) * tile_size, (y + 1) * tile_size], fill=cor_inicio, outline="black")
    if fim:
        x, y = fim
        draw.rectangle([x * tile_size, y * tile_size, (x + 1) * tile_size, (y + 1) * tile_size], fill=cor_fim, outline="black")
        
    img.save(nome_arquivo_saida)
    print(f"Imagem gerada: {nome_arquivo_saida}")
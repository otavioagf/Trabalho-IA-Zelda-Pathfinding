# Trabalho Prático - Busca Heurística (IA)

## A Lenda de Link: Em Busca da Rota Ótima

### 🇧🇷 PT-BR

Este repositório contém a implementação de um agente autônomo para resolver um desafio de busca de caminho no universo de *The Legend of Zelda*. [cite_start]O objetivo é guiar o herói, Link, a encontrar o caminho de menor custo para coletar os três Pingentes da Virtude e, em seguida, chegar à Master Sword[cite: 8]. O projeto foi desenvolvido para a disciplina de Inteligência Artificial, utilizando o algoritmo de busca heurística A*.

### 🇺🇸 EN-US

This repository contains the implementation of an autonomous agent to solve a pathfinding challenge in the universe of *The Legend of Zelda*. [cite_start]The goal is to guide the hero, Link, to find the lowest-cost path to collect the three Pendants of Virtue and then reach the Master Sword[cite: 8]. This project was developed for the Artificial Intelligence course, using the A* heuristic search algorithm.

---

## O Desafio

[cite_start]A jornada de Link começa em sua casa, na posição **[25, 28]** [cite: 34][cite_start], e o objetivo final é a entrada de Lost Woods, na posição **[7, 6]**[cite: 34]. [cite_start]Para isso, ele precisa primeiro encontrar os três Pingentes da Virtude (coragem, poder e sabedoria), que estão localizados dentro de três masmorras distintas espalhadas pelo reino de Hyrule[cite: 6, 7].

O problema é duplo:
1.  **Busca de Caminho (Pathfinding):** Encontrar o caminho de menor custo entre dois pontos, navegando por diferentes tipos de terreno e dentro das masmorras.
2.  [cite_start]**Otimização de Rota (TSP):** Determinar a melhor *ordem* para visitar as três masmorras, de forma a minimizar o custo total da jornada [cite: 44][cite_start], um problema análogo ao do Caixeiro Viajante[cite: 60].

### Mapas e Custos

[cite_start]O agente deve navegar por diferentes terrenos, cada um com um custo de movimento específico[cite: 19]:

* [cite_start]**Grama:** Custo +10 [cite: 20, 21]
* [cite_start]**Areia:** Custo +20 [cite: 22]
* [cite_start]**Floresta:** Custo +100 [cite: 23]
* [cite_start]**Montanha:** Custo +150 [cite: 24]
* [cite_start]**Água:** Custo +180 [cite: 25]
* [cite_start]**Piso da Masmorra:** Custo +10 [cite: 33]

[cite_start]O movimento do agente é restrito à vertical e horizontal, não sendo permitido andar na diagonal[cite: 45].

### Pontos de Interesse

* [cite_start]**Início:** Casa do Link `[25, 28]` [cite: 34]
* [cite_start]**Final:** Entrada de Lost Woods `[7, 6]` [cite: 34]
* [cite_start]**Entrada da Masmorra 1:** `[6, 33]` [cite: 29]
* [cite_start]**Entrada da Masmorra 2:** `[40, 18]` [cite: 30]
* [cite_start]**Entrada da Masmorra 3:** `[25, 2]` [cite: 31]

## Funcionalidades Implementadas

* **Algoritmo A\*:** Implementação genérica do algoritmo para busca de caminhos de menor custo.
* **Cálculo de Permutações:** O programa testa todas as 6 ordens possíveis de visita às masmorras para garantir a rota de menor custo total.
* [cite_start]**Visualização no Console:** Exibição do mapa e da movimentação do agente em tempo real diretamente no terminal[cite: 46, 47].
* [cite_start]**Relatório de Custos:** O custo do caminho é exibido durante a execução e o custo final total é apresentado ao término da missão[cite: 51].
* [cite_start]**Mapas Configuráveis:** Os mapas do reino e das masmorras são carregados a partir de arquivos externos, permitindo fácil edição[cite: 49, 50].

## Estrutura do Repositório

```
/
├── maps/              # Arquivos .txt com a representação dos mapas
│   ├── hyrule.txt
│   └── ...
├── src/               # Código-fonte do projeto
│   ├── astar.py       # Lógica do algoritmo A*
│   ├── mapa.py        # Módulo para carregar e gerenciar os mapas
│   └── main.py        # Orquestrador principal do programa
└── README.md          # Este arquivo
```

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/otavioagf/Trabalho-IA-Zelda-Pathfinding.git](https://github.com/otavioagf/Trabalho-IA-Zelda-Pathfinding.git)
    cd Trabalho-IA-Zelda-Pathfinding
    ```

2.  **(Opcional) Crie um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Instale as dependências (se houver):**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o programa:**
    ```bash
    python src/main.py
    ```

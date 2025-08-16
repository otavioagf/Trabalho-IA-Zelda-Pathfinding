# Trabalho Prático - Busca Heurística (IA)

## A Lenda de Link: Em Busca da Rota Ótima

### 🇧🇷 PT-BR

Este repositório contém a implementação de um agente autônomo para resolver um desafio de busca de caminho no universo de *The Legend of Zelda*. O objetivo é guiar o herói, Link, a encontrar o caminho de menor custo para coletar os três Pingentes da Virtude e, em seguida, chegar à Master Sword. O projeto foi desenvolvido para a disciplina de Inteligência Artificial, utilizando o algoritmo de busca heurística A*.

### 🇺🇸 EN-US

This repository contains the implementation of an autonomous agent to solve a pathfinding challenge in the universe of *The Legend of Zelda*. The goal is to guide the hero, Link, to find the lowest-cost path to collect the three Pendants of Virtue and then reach the Master Sword. This project was developed for the Artificial Intelligence course, using the A* heuristic search algorithm.

---

## O Desafio

A jornada de Link começa em sua casa e o objetivo final é a entrada de Lost Woods. Para provar seu valor, ele precisa primeiro encontrar os três Pingentes da Virtude (coragem, poder e sabedoria), que estão localizados dentro de três masmorras distintas espalhadas pelo reino de Hyrule.

O problema é duplo:
1.  **Busca de Caminho (Pathfinding):** Encontrar o caminho de menor custo entre dois pontos, navegando por diferentes tipos de terreno e dentro das masmorras, utilizando o algoritmo A*.
2.  **Otimização de Rota (TSP):** Determinar a melhor *ordem* para visitar as três masmorras, de forma a minimizar o custo total da jornada, um problema análogo ao do Caixeiro Viajante.

## Funcionalidades

* **Algoritmo A***: Implementação do algoritmo para busca de caminhos de menor custo em grades.
* **Análise de Permutações**: O programa testa todas as 6 ordens possíveis de visita às masmorras para garantir a rota de menor custo total.
* **Carregamento de Mapas Externos**: Os mapas do reino e das masmorras são carregados a partir de arquivos `.txt`, permitindo fácil edição.
* **Sistema de Verificação**: Uma função de segurança valida se os pontos de interesse (entradas, pingentes) estão em locais caminháveis antes de iniciar a busca.

## Legenda dos Mapas

Os terrenos e seus respectivos custos de movimento, conforme definido no código, são:

| Caractere | Terreno / Item         | Custo |
|:---------:|:-----------------------|:-----:|
|     G     | Grama                  |   10  |
|     S     | Areia                  |   20  |
|     F     | Floresta               |   100 |
|     M     | Montanha               |   150 |
|     A     | Água                   |   180 |
|     P     | Piso da Masmorra       |   10  |
|     L     | Posição do Link        |   10  |
|     LW    | Lost Woods             |   10  |
|     MA    | Entrada da Masmorra    |   10  |
|     MS    | Master Sword           |   10  |
|     X     | Parede / Obstáculo     |   ∞   |

## [cite_start]Estrutura do Repositório [cite: 1]

[cite_start]A estrutura de arquivos do projeto está organizada da seguinte forma: [cite: 1]

```
/
├── docs/
│   └── Trabalho - Busca Heurística.pdf
├── maps/
│   ├── hyrule.txt
│   ├── legenda.txt
│   ├── masmorra1.txt
│   ├── masmorra2.txt
│   └── masmorra3.txt
├── src/
│   ├── __pycache__/
│   ├── astar.py
│   ├── main.py
│   ├── mapa.py
│   └── visualizacao.py
├── .gitignore
├── LICENSE
└── README.md
```

## Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/otavioagf/Trabalho-IA-Zelda-Pathfinding.git](https://github.com/otavioagf/Trabalho-IA-Zelda-Pathfinding.git)
    cd Trabalho-IA-Zelda-Pathfinding
    ```

2.  **Execute o programa:**
    Nenhuma dependência externa é necessária. Para rodar a simulação principal, utilize o seguinte comando na raiz do projeto:
    ```powershell
    python -m src.main
    ```

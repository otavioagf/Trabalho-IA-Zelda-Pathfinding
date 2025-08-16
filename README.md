# Busca Heurística - A Lenda de Link

### Trabalho Prático de Inteligência Artificial

Um agente autônomo desenvolvido em Python para encontrar a rota ótima em um mapa inspirado no universo de *The Legend of Zelda*, utilizando o algoritmo de busca A* e solucionando uma variação do Problema do Caixeiro Viajante.

---

### Contexto Acadêmico
* **Disciplina:** Inteligência Artificial
* **Professor:** Matheus Satler
* **Instituição:** Universidade Federal de Ouro Preto (UFOP) - Campus ICEA
* **Autores:**
    * Arthur Campos
    * Otávio Guimarães

---

## Funcionalidades Principais

* **Algoritmo A***: O núcleo do agente utiliza o A* para encontrar o caminho de menor custo entre dois pontos, considerando os diferentes custos de terreno.
* **Solução para o "Caixeiro Viajante"**: O programa calcula o custo de todas as 6 permutações possíveis de visita às três masmorras para garantir que a jornada total seja a de menor custo possível.
* **Geração de Imagens**: Ao final da execução, o programa gera uma série de imagens `.png` que ilustram visualmente, passo a passo, cada etapa da rota ótima encontrada. O caminho do agente é destacado com uma linha contínua para fácil visualização.
* **Configuração Externa**: As coordenadas de todos os pontos de interesse (casa do Link, masmorras, etc.) são carregadas de um arquivo `config.json`, permitindo ajustes fáceis sem alterar o código-fonte.
* **Carregamento Robusto de Mapas**: O sistema lê os mapas a partir de arquivos `.txt` e é robusto a pequenas falhas de formatação (como linhas de comprimentos diferentes), garantindo a execução.
* **Tratamento de Exceções**: O programa possui um tratamento de erros que informa o usuário de forma clara caso um arquivo de mapa não seja encontrado ou uma coordenada esteja sobre uma parede.

## Visualização do Resultado

Ao final da execução, o programa gera uma pasta `imagens_geradas` com a jornada completa do Link.

*(Dica: Após enviar as imagens para o GitHub, você pode clicar em uma delas, copiar o endereço e colar aqui para exibi-la diretamente no README).*
![Exemplo de Rota em Hyrule](URL_DA_SUA_IMAGEM_AQUI.png)

## Estrutura do Repositório

```
/
├── config.json               # Arquivo de configuração com as coordenadas
├── docs/
│   └── Trabalho-Busca-Heuristica.pdf
├── imagens_geradas/          # Pasta onde as imagens da rota são salvas
├── maps/
│   ├── hyrule.txt
│   └── masmorra1.txt, masmorra2.txt, masmorra3.txt
├── src/
│   ├── __init__.py
│   ├── astar.py              # Implementação do algoritmo A*
│   ├── main.py               # Orquestrador principal do programa
│   ├── mapa.py               # Classe para carregar e gerenciar os mapas
│   └── visualizacao.py       # Módulo para gerar as imagens da rota
├── requirements.txt          # Lista de dependências do projeto
└── README.md                 # Este arquivo
```

## Legenda dos Mapas

Os terrenos e seus respectivos custos de movimento são:

| Caractere | Terreno / Item                  | Custo |
|:---------:|:--------------------------------|:-----:|
|     G     | Grama                           |   10  |
|     S     | Areia                           |   20  |
|     F     | Floresta (em Hyrule)            |  100  |
|     M     | Montanha                        |   150 |
|     A     | Água                            |   180 |
|     P     | Piso da Masmorra                |   10  |
|     L     | Casa do Link (Ponto Inicial)    |   10  |
|     LW    | Lost Woods (Destino Final)      |   10  |
|     MA    | Entrada da Masmorra (em Hyrule) |   20  |
|     MS    | Marco da Master Sword           |   10  |
|     X     | Parede / Obstáculo              |  ∞    |

*Observação: O código também está programado para tratar a letra 'F' como piso de custo 10 caso seja usada nos mapas das masmorras.*

## Guia de Execução (a partir do arquivo ZIP)

Este guia descreve os passos para configurar e executar o programa em um novo dispositivo.

### 1. Pré-requisitos
Antes de começar, garanta que você tem o **Python** (versão 3.8 ou superior) instalado.

### 2. Preparar a Pasta do Projeto
1.  Descompacte o arquivo `.zip` do projeto em uma pasta de sua preferência.
2.  Abra um terminal (PowerShell, CMD, etc.) e navegue com o comando `cd` até a pasta que foi criada.

### 3. Configurar o Ambiente Virtual (venv)
É uma boa prática isolar as dependências do projeto.

a) Crie o ambiente virtual:
   ```powershell
   python -m venv .venv
   ```

b) Ative o ambiente virtual:
   - No **Windows**:
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   - No **Mac ou Linux**:
     ```bash
     source .venv/bin/activate
     ```
   Após ativar, você deverá ver um `(.venv)` no início do seu terminal.

### 4. Instalar as Dependências
Com o ambiente virtual ativo, instale a biblioteca `Pillow` usando o arquivo `requirements.txt`.

```powershell
pip install -r requirements.txt
```

### 5. Executar o Programa
Agora, com tudo configurado, execute o programa principal:

```powershell
python -m src.main
```
O programa irá rodar, exibir os cálculos no terminal e salvar as imagens da rota ótima na pasta `imagens_geradas`.

---
## Tecnologias Utilizadas
* **Python 3**
* **Pillow (PIL)**: Para a geração das imagens.

import random

TAMANHO = 10 # Matriz de TAMANHO x TAMANHO
TAXA_OBSTACULOS = 0.1  # Taxa de obstáculos (10%)
posicao_inicial = None
posicao_objetivo = None

def criar_mapa(tamanho, taxa_obstaculos):
    global posicao_inicial, posicao_objetivo

    mapa = [['_'] * tamanho for _ in range(tamanho)]

    num_obstaculos = int(tamanho * tamanho * taxa_obstaculos)
    obstaculos_inseridos = 0

    while obstaculos_inseridos < num_obstaculos:
        x = random.randint(0, tamanho - 1)
        y = random.randint(0, tamanho - 1)

        if mapa[y][x] == '_':
            mapa[y][x] = '|'
            obstaculos_inseridos += 1

    # Insere a posição inicial '@'
    x_inicial = random.randint(0, tamanho - 1)
    y_inicial = random.randint(0, tamanho - 1)
    mapa[y_inicial][x_inicial] = '@'
    posicao_inicial = (x_inicial, y_inicial)


    # Insere a posição do objetivo '$'
    x_objetivo = random.randint(0, tamanho - 1)
    y_objetivo = random.randint(0, tamanho - 1)

    # Certifica-se de que o objetivo não esteja na mesma posição da inicial
    while (x_objetivo, y_objetivo) == (x_inicial, y_inicial):
        x_objetivo = random.randint(0, tamanho - 1)
        y_objetivo = random.randint(0, tamanho - 1)
    mapa[y_objetivo][x_objetivo] = '$'
    posicao_objetivo = (x_objetivo, y_objetivo)

    return mapa

def imprimir_mapa(mapa):
    for linha in mapa:
        print(''.join(linha))
    print()



# Execução do algoritmo
mapa = criar_mapa(TAMANHO, TAXA_OBSTACULOS)
imprimir_mapa(mapa)
import random

def criar_fila(participantes):
    fila = random.sample(participantes, len(participantes)) #Cria uma nova lista chamada fila com as posiçoes aleatorias
    jogador1 = fila[0] # Atribui o 1 da lista ao jogador1
    jogador2 = fila[1] # Atribui o 2 da lista ao jogador2
    restantes = fila[2:] # Cria uma nova lista sem alterar a fila, com os jogadores restantes

    return fila, restantes, jogador1, jogador2 #Retorna tudo

def proxima_partida(fila): #Cria uma funçao para poder atualizar os jogadores apos a primeira partida, tendo como entrada a fila original ja ordenada
    jogador1 = fila[0]
    jogador2 = fila[1]
    restantes = fila[2:]

    return jogador1, jogador2, restantes

def enfileirar(fila, entrada):
    fila.append(entrada)

def desenfileirar(fila):
    return fila.pop(0)
def livros():
    pilha = []
    return pilha

def receber(pilha, entrada):
    pilha.append(entrada)

def ler(pilha):
    return pilha.pop()

def livros_lidos():
    fila = []
    return fila

def adiciona_lidos(fila, pilha):
    fila.append(pilha[len(pilha)-1])
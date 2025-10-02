def criar_pilha():
    pilha = []
    return pilha

def empilhar(pilha, entrada):
    pilha.append(entrada)

def desempilhar(pilha):
    return pilha.pop()

def mostrar_pilha(pilha):
    for i in range(len(pilha)-1, -1, -1):
        print(pilha[i])
    print('\n')
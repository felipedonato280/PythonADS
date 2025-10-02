def criar_fila():
    fila = []
    return fila

def enfileirar(fila, entrada):
    fila.append(entrada)

def desenfileirar(fila):
    return fila.pop(0)

def mostrar_fila(fila):
    print(f"{fila}\n")
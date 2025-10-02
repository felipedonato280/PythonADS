def pesquisa_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(lista[meio])
        if valor == lista[meio]:
            return meio + 1
        elif valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1
    return 0

arquivo = open("C:/Users/felip/Desktop/ADS/Algoritmos/Pesquisa/palavras.txt", "r")
palavras = arquivo.readlines()

for i in range(len(palavras)):
    palavras[i] = palavras[i].rstrip()
arquivo.close()

while True:
    palavra = input("Palavra a pesquisar: ")
    pos = pesquisa_binaria(palavras, palavra)
    print(pos)
def pesquisa_linear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i+1
    return 0

arquivo = open("C:/Users/felip/Desktop/ADS/Algoritmos/Pesquisa/palavrasDesord.txt", "r")
palavras = arquivo.readlines()

for i in range(len(palavras)):
    palavras[i] = palavras[i].rstrip()
arquivo.close()

while True:
    palavra = input("Palavra a pesquisar: ")
    pos = pesquisa_linear(palavras, palavra)
    print(pos)
import time

def bubblesorte (lista):
    n = len(lista)

    for i in range(1, n+1):
        houve_troca = False
        for j in range(0, n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                houve_troca = True
        if houve_troca == False:
            break

arquivo = open("C:/Users/felip/Desktop/ADS/Algoritmos/ordenacao/Teste1.txt", "r")
palavras = arquivo.readlines()

for i in range(len(palavras)):
    palavras[i] = palavras[i].rstrip()
arquivo.close()

t1 = time.time()
bubblesorte(palavras)
t2 = time.time()

print(t2 - t1)
print(palavras)
from funcionamento_programa import *

print("Bem Vindo a Livraria!\n")
print("O que deseja fazer?\n")

print("Digite 1 para Receber livro:")
print("Digite 2 para ler livro:")
print("Digite 3 para mostrar livros em espera:")
print("Digite 4 para mostrar livros lidos:")
print("Digite 5 para sair:")

op = int(input("Escolha uma opção (1-5): "))

livros = []
livros_lidos = []

while op != 5:
    match op:
        case 1:
            novo_livro = input("\nQual o nome do livro? ")
            receber(livros, novo_livro)
        case 2:
            print(f"\nLivro lido {livros[len(livros)-1]}")
            print("...")
            adiciona_lidos(livros_lidos, livros)
            ler(livros)
        case 3:
            print(f"\nlivros em espera {', '.join(livros)}")
        case 4:
            print(f"\nlivros lidos {', '.join(livros_lidos)}")
        case _:
            print("\nOP INVALIDA!!!")

    op = int(input("Escolha uma opção (1-5): ")) 

print("Programa encerrado")
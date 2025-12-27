while True:
    Argolas = int(input("Qual a quantidade de argolas? "))

    def Calcula_Hanoi(n):
        if n == 1:
            return 1
        return 2 * Calcula_Hanoi(n - 1) + 1

    print(Calcula_Hanoi(Argolas))
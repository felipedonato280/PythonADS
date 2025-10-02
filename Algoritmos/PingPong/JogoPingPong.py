from funcionamentoPingPong import *

print("Bem vindo ao PingPong!\n")

participantes = list(map(str,input("Quais os Participantes? ").split(" ")))

rodadas = int(input("\nQuantas rodadas tera cada o jogo? "))

fila, restantes, jogador1, jogador2 = criar_fila(participantes)

while len(fila) >= 2:

    jogador1, jogador2, restantes = proxima_partida(fila) #Chama a funcao proxima partida para poder atualizar os valores dentro do while

    print(f"\nJogadores desta partida: {jogador1} vs {jogador2}") #Mostra os primeiros jogadores

    if len(restantes) > 1:
        texto_restantes = ', '.join(restantes[:-1]) + " e " + restantes[-1]
    elif len(restantes) == 1:
        texto_restantes = restantes[0]
    else:
        texto_restantes = "ninguém"
        
    print(f"Os próximos serão: {texto_restantes} respectivamente\n") #Mostra os proximos da fila

    rodadas_ganhas_jog_1, rodadas_ganhas_jog_2 = 0, 0

    for i in range(rodadas):
        pontos1, pontos2 = map(int, input("Qual a pontuaçao da rodada? ").split(" "))
        if pontos1 > pontos2:
            rodadas_ganhas_jog_1 += 1
        elif pontos2 > pontos1:
            rodadas_ganhas_jog_2 += 1
        else:
            print("⚖️ Empate na rodada! Ninguém ganha ponto.")

    if rodadas_ganhas_jog_1 > rodadas_ganhas_jog_2:
        print(f"🏆 {jogador1} venceu a partida!")
        enfileirar(fila, jogador2)
        desenfileirar(fila)
    elif rodadas_ganhas_jog_1 < rodadas_ganhas_jog_2:
        print(f"🏆 {jogador2} venceu a partida!")
        enfileirar(fila, jogador1)
        desenfileirar(fila)
    else:
        print("🤝 A partida terminou empatada!")

    continuar = input("\nDeseja continuar o jogo? (s/n): ").strip().lower()
    if continuar == "n" or continuar == "N":
        print("🏁 Jogo encerrado!")
        break

if len(fila) < 2:
    print("⚠️ Não há jogadores suficientes para continuar!")
import java.util.Scanner;
import java.util.Random;

public class JogoAdivinhe {
    int numeroSecreto;
    boolean finalizado;
    int tentativas;
    private final int LIMITE_TENTATIVAS = 10;
    int dificuldade;

    public JogoAdivinhe(){
        Random random = new Random();

        // implementei o atributo dificuldade, pois quanto maior o tamanho do random, mais dificil fica de acertar
        // Para melhorias futuras fica melhor assim.

        this.dificuldade = 101;
        this.numeroSecreto = random.nextInt(1, dificuldade);
        this.tentativas = 0;
        this.finalizado = false;
    }

    public void mostrarBoasVindas(){
        System.out.println("Boas-vindas ao jogo do adivinhe!");
    }

    public int lerTeclado(Scanner input){
        int palpite;

        do{
            System.out.println("Qual o seu palpite? numeros de 1 a " + (dificuldade - 1));
            // Mostra dificuldade - 1 para ficar de 1 a 100, ja que o random nao pega o ultimo numero, tive que colocar de 1 a 101
            palpite = input.nextInt();

            if(palpite < 1 || palpite >= dificuldade){
                System.out.println("Valor inválido! Tente novamente.");
            }

        }while(palpite < 1 || palpite >= dificuldade);

        return palpite;
    }

    public void processarPalpite(int palpite){
        tentativas++;

        if(palpite == numeroSecreto){
            finalizado = true;
            System.out.println("Parabéns, você me venceu");
            System.out.println("Tentativa(s): " + tentativas);
        }
        else if(tentativas >= LIMITE_TENTATIVAS){
            finalizado = true;
            System.out.println("Eu venci");
            System.out.println("Você chegou ao limite de " + LIMITE_TENTATIVAS + " tentativas");
            System.out.println("O número secreto era: " + numeroSecreto);
        }
        else{
            if(palpite < numeroSecreto){
                System.out.println("Putz, o número secreto é MAIOR!");
            }
            else{
                System.out.println("Putz, o número secreto é MENOR!");
            }

            int restante = LIMITE_TENTATIVAS - tentativas;
            System.out.println("Restam: " + restante + " tentativa(s)");
        }
    }

    public boolean estaFinalizado(){
        return finalizado;
    }

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);

        JogoAdivinhe jogo = new JogoAdivinhe();

        jogo.mostrarBoasVindas();

        while (!jogo.estaFinalizado()) {
            int palpite = jogo.lerTeclado(input);
            jogo.processarPalpite(palpite);
        }

        input.close();
    }
}
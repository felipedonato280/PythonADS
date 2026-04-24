package bpm;

import java.util.Scanner;

public class BPM {
    
    String nome;
    int bpm;
    
    public BPM(String nome, int bpm){
        if(nome != null){
            this.nome = nome;
        }else{
            System.out.println("Nome vazio");
            this.nome = "Nome nao informado";
        }
        
        if(bpm > 0){
            this.bpm = bpm;
        }else{
            System.out.println("BPM invalido");
        }
    }
    
    public BPM(){
        
    }
    
    public String verificaBatimentos(){
        if(bpm > 0){
            if(bpm < 60){
            return "Bradicardia (muito baixo)";
            }
            else if(bpm > 100){
                return "Taquicardia (muito alto)";
            }
            else{
                return "Normal";
            }
        }else{
            return "Erro";
        }
    }
    
    public void lerTeclado(Scanner input){
        do{
            System.out.println("Qual o seu nome? ");
            nome = input.nextLine();
        }while(nome.isEmpty());
        
        do{
            System.out.println("Qual o seu BPM? ");
            bpm = input.nextInt();
        }while(bpm < 0);
    }
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        BPM bpm01 = new BPM();
        bpm01.lerTeclado(input);
        
        //BPM bpm02 = new BPM(null, -8);
        
        System.out.println(bpm01.verificaBatimentos());
        //System.out.println(bpm02.verificaBatimentos());
    }
}
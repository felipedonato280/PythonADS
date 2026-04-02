public class Data {
    int dia;
    int mes;
    int ano;

    // Criando o metodo construtor da classe

    public Data(int dia, int mes, int ano){

        if(mes >= 1 && mes <= 12){
            this.mes = mes;
        }
        else{
            System.out.println("O mes é invalido");
            this.mes = 1; //mes padrao
        }

        int diasMes[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        if(dia >= 1 && dia <= diasMes[this.mes]){
            this.dia = dia;
        }
        else{
            System.out.println("Dia invalido");
            this.dia = 1;
        }

        if(ano >= 0 && ano <= 2026){
            this.ano = ano;
        }
        else{
            System.out.println("Ano invalido!");
        }
    }

    // Fazendo uma sobrecarga de metodo

    public Data(int dia, int mes){
        this.dia = dia;
        this.mes = mes;
    }

    public String escreverAbreviado(){
        if (ano == 0)
            return dia + "/" + mes;

        return dia + "/" + mes + "/" + ano;
    }

    public String escreverExtenso(){
        String meses[] = {"", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"};

        return dia + " de " + meses[mes] + " de " + ano;
    }

    public static void main(String[]args){

        Data hoje = new Data(11,10,2026);

        //Data hoje = new Data(11,3,2026);
        //Data amanha = new Data(12,3);
        //
        //System.out.println(hoje.escreverAbreviado());
        //System.out.println(amanha.escreverAbreviado());
        //
        //hoje.dia = 15;
        //hoje.mes = 4;
        //hoje.ano = 2026;

        System.out.println(hoje.escreverAbreviado());
        System.out.println(hoje.escreverExtenso());

        Data aulasPOO[] = new Data[5];

        aulasPOO[0] = new Data(1, 4, 2026);
        aulasPOO[1] = new Data(8, 4, 2026);
        aulasPOO[2] = new Data(15, 4, 2026);
        aulasPOO[3] = new Data(22, 4, 2026);
        aulasPOO[4] = new Data(29, 4, 2026);

        System.out.printf("A avaliação ficou marcada para %s \n", aulasPOO[3].escreverExtenso());
        System.out.println("As aulas de POO em abril serão nas seguintes datas");

        for(int i = 0; i < aulasPOO.length; i++){
            System.out.printf("%s\n", aulasPOO[i].escreverAbreviado());
        }
    }
}
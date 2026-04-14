public class Venda {

    String nomeCliente;
    float total;
    Produto itens[];
    int indice = 0;

    public Venda(String nomeCliente){
        if(nomeCliente != null && !nomeCliente.isEmpty()){
            this.nomeCliente = nomeCliente;
        }
        else{
            System.out.println("Nome do cliente invalido");
        }

        itens = new Produto[100];
        total = 0;
    }

    public void adicionarProdutos(Produto prod){
        itens[indice] = prod;
        total += prod.precoVenda;

        indice++;
    }

    public String imprimirNota(){
        String saida = "";

        saida += "COMPRADOR: " + nomeCliente + "\n";
        saida += "\n" + "PRODUTOS DO PEDIDO" + "\n" + "\n";

        for(int i = 0; i < indice; i++){
            saida += (i+1) + ": " + itens[i].nome + "\n";
        }

        saida += "\n" + "VALOR TOTAL: " + String.format("%.2f", total) + " RS";

        return  saida;
    }

    public static void main(String[] args){
        Produto prod01 = new Produto(101, "Coca Lata", "Bebidas", 2f);
        Produto prod02 = new Produto(102, "Leite", "Bebidas", 1.50f, 6.50f);
        Produto prod03 = new Produto(103, "Doritos", "Salgadinhos", 3f, 12.50f);
        Produto prod04 = new Produto(104, "Oreo", "Bolachas", 1.20f, 3f);
        Produto prod05 = new Produto(105, "Ovos", "Outros", 1.99f, 11.99f);
        Produto prod06 = new Produto(106, "Maça", "Frutas", 5.40f, 13f);
        Produto prod07 = new Produto(107, "Carne", "Carnes", 25.50f, 42.80f);
        Produto prod08 = new Produto(108, "Água", "Bebidas", 0.20f, 1.50f);

        Venda venda01 = new Venda("Felipe");

        venda01.adicionarProdutos(prod02);
        venda01.adicionarProdutos(prod03);
        venda01.adicionarProdutos(prod04);
        venda01.adicionarProdutos(prod05);
        venda01.adicionarProdutos(prod08);
        venda01.adicionarProdutos(prod06);

        System.out.println(venda01.imprimirNota());
    }
}
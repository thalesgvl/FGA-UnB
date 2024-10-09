import javax.swing.JOptionPane;

public class Ex014 
{
    public static void inserirVet2(float vet[])
    {
        for (int i = 0; i < vet.length; i++) {
            String numStr = JOptionPane.showInputDialog("Informe os elementos do vetor [" + i + "]: ");
            float num = Float.parseFloat(numStr);
            vet[i] = num;
        }
    }

    public static void calcularMultVet(float vet1[], float vet2[], int tam)
    {
        float vet3[] = new float[tam];
        float produto = 0;

        for (int i = 0; i < tam; i++) 
        {
            vet3[i] = vet1[i] * vet2[i];
            produto += vet3[i];
        }

        String resposta = "O produto dos vetores é: " + produto;
        JOptionPane.showMessageDialog(null, resposta);
    }
    
    public static void main(String[] args) 
    {
        String tamStr = JOptionPane.showInputDialog("Qual o tamanho do vetor?: ");
        int tam = Integer.parseInt(tamStr);
        float vet1[] = new float[tam];
        float vet2[] = new float[tam];
        
        inserirVet2(vet1);
        inserirVet2(vet2);
        calcularMultVet(vet1, vet2, tam);
    }
}
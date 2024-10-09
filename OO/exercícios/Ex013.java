import javax.swing.JOptionPane;

public class Ex013 
{

	public static void inserirVet(int vet[])
	{
		for (int i = 0; i < vet.length; i++) 
		{
			String numStr = JOptionPane.showInputDialog("Informe os elementos do vetor [" + i + "]: ");
			int num = Integer.parseInt(numStr);
			vet[i] = num;
		}
	}

	public static void somarVet(int vet1[], int vet2[], int tam)
	{
		int vet3 [] = new int[tam];

		String resposta = "A soma dos vetores é: [";

        for (int i = 0; i < tam; i++) 
		{
            vet3[i] = vet1[i] + vet2[i];
            if (i < tam -1)
			{
            	resposta += vet3[i] + ", ";
            }
			else 
			{
            	resposta += vet3[i];
            }
        }
        resposta += "]";

        JOptionPane.showMessageDialog(null, resposta);
	}
	public static void main(String[] args) 
	{
		String tamStr = JOptionPane.showInputDialog("Qual o tamanho do vetor?: ");
		int tam = Integer.parseInt(tamStr);
		int vet1 [] = new int[tam];
		int vet2 [] = new int[tam];
		
		inserirVet(vet1);
		inserirVet(vet2);
		somarVet(vet1, vet2, tam);
	}

}

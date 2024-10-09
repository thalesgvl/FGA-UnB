import javax.swing.JOptionPane;

public class Ex016 
{
    public static void inserirMat(int m, int n, int matriz[][])
    {
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                String valorStr = JOptionPane.showInputDialog("Informe o valor para M1[" + (i + 1) + "][" + (j + 1) + "]: ");
                matriz[i][j] = Integer.parseInt(valorStr);
            }
        }
    }

    public static int[][] calcularSomaMat(int matriz1[][], int matriz2[][], int m, int n)
    {
        int matrizSoma[][] = new int[m][n];

        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                matrizSoma[i][j] = matriz1[i][j] + matriz2[i][j];
            }
        }
        return matrizSoma; // Retorna a matriz soma
    }

    public static void exibirMat(int matriz[][], int m, int n)
    {
             String resultado = "M1 + M2 = \n";
             for (int i = 0; i < m; i++) 
             {
                 for (int j = 0; j < n; j++) 
                 {
                     resultado += matriz[i][j] + " ";
                 }
                 resultado += "\n";
             }
     
             JOptionPane.showMessageDialog(null, resultado);    
    }
	
	public static void main(String[] args) 
    {
		
        String mStr = JOptionPane.showInputDialog("Digite o número de linhas das matrizes: ");
        int m = Integer.parseInt(mStr);

        String nStr = JOptionPane.showInputDialog("Digite o número de colunas das matrizes: ");
        int n = Integer.parseInt(nStr);
        

        int matriz1[][] = new int[m][n];
        int matriz2[][] = new int[m][n];

        inserirMat(m, n, matriz1);
        inserirMat(m, n, matriz2);
        int matrizSoma[][] = calcularSomaMat(matriz1, matriz2, m, n);
        exibirMat(matrizSoma, m, n);
    }
}


import javax.swing.JOptionPane;

public class Ex017 
{
    public static void inserirMat2(int M[][], int m, int n)
    {
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                String valorStr = JOptionPane.showInputDialog("Informe o valor para M1[" + (i + 1) + "][" + (j + 1) + "]: ");
                M[i][j] = Integer.parseInt(valorStr);
            }
        }
    }

    public static int[][] calcularMultMat(int M1[][], int M2[][], int m, int n)
    {
        int result[][] = new int[m][m];  

        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < m; j++) 
            {
                for (int k = 0; k < n; k++) 
                {
                    result[i][j] += M1[i][k] * M2[k][j];
                }
            }
        }
        return result;
    }

    public static void mostrarMat(int M[][], int m, int n) 
    {
        String resposta = "Resultado da Multiplicação: \n";
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                resposta += M[i][j] + " ";
            }
            resposta += "\n";
        }

        JOptionPane.showMessageDialog(null, resposta);
    }
	public static void main(String[] args) 

    {
        String mStr = JOptionPane.showInputDialog("Informe o número de linhas das matrizes: ");
        int m = Integer.parseInt(mStr);

        String nStr = JOptionPane.showInputDialog("Informe o número de colunas das matrizes: ");
        int n = Integer.parseInt(nStr);

        int M1[][] = new int[m][n];
        int M2[][] = new int[n][m];

        inserirMat2(M1, m, n);
        inserirMat2(M2, m, n);
        int M3[][] = calcularMultMat(M1, M2, m, n);
        mostrarMat(M3, m, n);
    }
}
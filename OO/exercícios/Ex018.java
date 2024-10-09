import javax.swing.JOptionPane;

public class Ex018 
{
    public static void inserirMat(int matriz[][], int m, int n)
    {
        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                String valorStr = JOptionPane.showInputDialog("Informe o valor para M [" + (i + 1) + "][" + (j + 1) + "]: ");
                matriz[i][j] = Integer.parseInt(valorStr);
            }
        }
    }

    public static int[][] transporMat(int matriz[][], int m, int n)
    {
        int matrizTransposta[][] = new int[n][m];

        for (int i = 0; i < m; i++) 
        {
            for (int j = 0; j < n; j++) 
            {
                matrizTransposta[j][i] = matriz[i][j];
            }
        }
        return matrizTransposta;
    }

    public static void mostrarMatT(int matrizTransposta[][], int m, int n)
    {
        String resultado = "A matriz transposta é:\n";
        for (int i = 0; i < n; i++) 
        {
            for (int j = 0; j < m; j++) 
            {
                resultado += matrizTransposta[i][j] + " ";
            }
            resultado += "\n";
        }
        JOptionPane.showMessageDialog(null, resultado);

    }

	public static void main(String[] args) 
    {
        String mStr = JOptionPane.showInputDialog("Digite o número de linhas da matriz: ");
        int m = Integer.parseInt(mStr);

        String nStr = JOptionPane.showInputDialog("Digite o número de colunas da matriz: ");
        int n = Integer.parseInt(nStr);

        int matriz[][] = new int[m][n];

        inserirMat(matriz, m, n);
        int MT[][] = transporMat(matriz, m, n);
        mostrarMatT(MT, m, n);
    }
}
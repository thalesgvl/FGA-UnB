import javax.swing.JOptionPane;

public class Ex007 
{
	public static void verificaPar(int num)
	{
		if (num % 2 == 0) 
		{
			JOptionPane.showMessageDialog(null, "O número: " + num + ". É par!");
		}
		else 
		{
			JOptionPane.showMessageDialog(null, "O número: " + num + ". É ímpar!");
		}
	}

	public static void main(String[] args) 
	{
		String numStr = JOptionPane.showInputDialog("Digite um número: ");
		int num = Integer.parseInt(numStr);
		
		verificaPar(num);
	}

}

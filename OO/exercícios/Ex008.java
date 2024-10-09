import javax.swing.JOptionPane;

public class Ex008 
{
	public static void somar(int a, int b)
	{
		int soma = a + b;
		JOptionPane.showMessageDialog(null,"A soma entre: " + a + " e " + b + " é igual a: " + soma + ".");
	}

	public static void subtrair(int a, int b)
	{
		int subt = a - b;
		JOptionPane.showMessageDialog(null,"A subtração entre: " + a + " e " + b + " é igual a: " + subt + ".");
	}

	public static void multiplicar(int a, int b)
	{
		int mult = a * b;
		JOptionPane.showMessageDialog(null,"A multiplicação entre: " + a + " e " + b + " é igual a: " + mult + ".");
	}
	
	public static void dividir(int a, int b)
	{
		float div = (float)a / b;
		JOptionPane.showMessageDialog(null,"A divisão entre: " + a + " e " + b + " é igual a: " + div + ".");
	}

	public static void potencia(int a, int b)
	{
		int pot = (int) Math.pow(a, b);
		JOptionPane.showMessageDialog(null,"O resultado de " + a + " elevado a " + b + " é: " + pot + ".");
	}



	public static void main(String[] args) 
	{
			//Crie um programa que seja capaz de fazer a leitura de dois valores inteiros a e b, e realize as seguintes operações:
			//A+B, A-B, A*B, A/B, A^B.
			
			String aStr = JOptionPane.showInputDialog("Digite um valor para 'a': ");
			int a = Integer.parseInt(aStr);
			
			String bStr = JOptionPane.showInputDialog("Digite um valor para 'b': ");
			int b = Integer.parseInt(bStr);
			
			
			String opStr = JOptionPane.showInputDialog("-=-=- Escolha uma operação: -=-=-" + "\n" +
													   "1 - Adição" + "\n" +
													   "2 - Subtração" + "\n" +
													   "3 - Multiplicação" + "\n" +
													   "4 - Divisão" + "\n" +
													   "5 - Potenciação");
			int op = Integer.parseInt(opStr);
			
			
			switch (op) 
			{
			case 1:
				somar(a, b);
				break;
			case 2:
				subtrair(a, b);
				break;
			case 3:
				multiplicar(a, b);
				break;
			case 4:
				dividir(a, b);
				break;
			case 5:
				potencia(a, b);
				break;
			default:
				JOptionPane.showMessageDialog(null,"Opção inválida.");
				break;	
			
			}
		}
	}


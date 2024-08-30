import javax.swing.JOptionPane;

public class Ex001 {

	public static void main(String[] args) {
	
		String valorStr,
		       gorjetaStr;
		
		float valorFloat,
		      gorjetaFloat,
		      valorGorjeta,
		      valorTot;
		
		valorStr = JOptionPane.showInputDialog("Digite o valor total da conta: " );
		valorFloat = Float.parseFloat(valorStr);
		
		gorjetaStr = JOptionPane.showInputDialog("Digite a porcentagem de gorjeta que deseja deixar (por exemplo, 15 para 15%): ");
		gorjetaFloat = Float.parseFloat(gorjetaStr);
		
		valorTot = valorFloat + (valorFloat * (gorjetaFloat/100));
		valorGorjeta = valorFloat * (gorjetaFloat / 100);
		
		String formattedGorjeta = String.format("%.2f", valorGorjeta);
		String formattedTotal = String.format("%.2f", valorTot);
		
		JOptionPane.showMessageDialog(null, "Valor da gorjeta: " + formattedGorjeta);
		JOptionPane.showMessageDialog(null, "Total a ser pago: " + formattedTotal);
		
		}
	}
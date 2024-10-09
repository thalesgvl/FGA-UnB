import javax.swing.JOptionPane;

public class Ex009 
{
	public static void calcularMedia2(float n1, float n2, float n3, float peso1, float peso2, float peso3)
	{
		float somaPesos = peso1 + peso2 + peso3;
		float mediaP = (((n1 * peso1) + (n2 * peso2) + (n3 * peso3)) /somaPesos) * 10;
		
		JOptionPane.showMessageDialog(null,"Média ponderada: " + mediaP);
		
		if (mediaP >= 90 && mediaP <= 100) 
		{
		    JOptionPane.showMessageDialog(null, "Menção: A");
		} 
		else if (mediaP >= 80 && mediaP <= 89) 
		{
		    JOptionPane.showMessageDialog(null, "Menção: B");
		} 
		else if (mediaP >= 70 && mediaP <= 79) 
		{
		    JOptionPane.showMessageDialog(null, "Menção: C");
		} 
		else if (mediaP >= 60 && mediaP <= 69) 
		{
		    JOptionPane.showMessageDialog(null, "Menção: D");
		}
		 else if (mediaP < 60) 
		 {
		    JOptionPane.showMessageDialog(null, "Menção: F");
		} 
		else 
		{
		    JOptionPane.showMessageDialog(null, "Menção inválida");
		}
	}

	public static void main(String[] args) 
	{
		float n1,
		  n2,
		  n3;
	
		float peso1,
		  peso2,
		  peso3;
			
		String strN1 = JOptionPane.showInputDialog("Nota 1: ");
		n1 = Float.parseFloat(strN1);
		String strP1 = JOptionPane.showInputDialog("Peso da nota 1: ");
		peso1 = Float.parseFloat(strP1);

		
		String strN2 = JOptionPane.showInputDialog("Nota 2: ");
		n2 = Float.parseFloat(strN2);
		String strP2 = JOptionPane.showInputDialog("Peso da nota 2: ");
		peso2 = Float.parseFloat(strP2);

		
		String strN3 = JOptionPane.showInputDialog("Nota 3: ");
		n3 = Float.parseFloat(strN3);
		String strP3 = JOptionPane.showInputDialog("Peso da nota 3: ");
		peso3 = Float.parseFloat(strP3);

		calcularMedia2(n1, n2, n3, peso1, peso2, peso3);
	}
}
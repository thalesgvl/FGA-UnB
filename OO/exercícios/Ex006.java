import javax.swing.JOptionPane;
public class Ex006 
{
	public static void calcularIMC(float fAltura, float fPeso)
	{
		//método imc
			
		float imc = fPeso / (fAltura * fAltura);
		String situacao;
			
		if(imc < 18.5) 
		{
			situacao = " Abaixo do peso ideal.";
		}
		else if (imc > 18.5 && imc < 24.5) 
		{
			situacao = " Peso ideal.";
		}
		else if (imc > 24.5 && imc < 30) 
		{
			situacao = " Sobrepeso.";
		}
		else
			situacao = " Obesidade.";
		
		// output				
		String resposta = String.format("Seu IMC é: %.2f. Sua situação é: %s", imc, situacao);
        JOptionPane.showMessageDialog(null, resposta);
						
	}

	public static void main(String[] args) 
	{

		//declaração var
		
		String strAltura, strPeso;
		float fAltura, fPeso;
		
		//interação / interface
		
		strPeso = JOptionPane.showInputDialog("Informe o peso (Kg): ");
		strAltura = JOptionPane.showInputDialog("Informe a altura(m): ");
		
		//type-casting, down-casting
		
		fPeso = Float.parseFloat(strPeso);
		fAltura = Float.parseFloat(strAltura);

		calcularIMC(fAltura, fPeso);
	}
}
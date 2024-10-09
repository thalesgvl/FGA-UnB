import java.util.Random;
import javax.swing.JOptionPane;

public class Ex011 
{
    public static void encontrarNum()
    {

        Random random = new Random();
	
    int numeroAleatorio = random.nextInt(10) + 1;
    int tentativas = 0;
    int palpite = 0;

    JOptionPane.showMessageDialog(null, "Adivinhe o número entre 1 e 10.");

    do {
        String palpiteString = JOptionPane.showInputDialog("Tentativa " + (tentativas + 1) + ":");

            palpite = Integer.parseInt(palpiteString);
            tentativas++;

            if (palpite < numeroAleatorio) 
            {
                JOptionPane.showMessageDialog(null, "Tente novamente. O número é maior.");
            } 
            else if (palpite > numeroAleatorio) 
            {
                JOptionPane.showMessageDialog(null, "Tente novamente. O número é menor.");
            } 
            else 
            {
                JOptionPane.showMessageDialog(null, "Parabéns! Você acertou o número " + numeroAleatorio + " em " + tentativas + " tentativas.");
            }
        } while (palpite != numeroAleatorio);
    }

	public static void main(String[] args) 
    {
	    encontrarNum();
    }
}
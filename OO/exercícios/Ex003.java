import javax.swing.JOptionPane;

public class Ex003 
{
    public static void adicionar(String[] lista, int i)
    {
        if (i >= lista.length) 
        {
            JOptionPane.showMessageDialog(null, "A lista de tarefas está cheia. Não é possível adicionar mais tarefas.");
            return;
        }

        String tarefa = JOptionPane.showInputDialog("Digite a descrição da tarefa: ");
                lista[i] = tarefa;
                JOptionPane.showMessageDialog(null, "Tarefa adicionada com sucesso!");
    }

    public static void listar(String[] lista, int i)
    {
        StringBuilder listaTarefas = new StringBuilder("Lista de Tarefas:\n");
                for (int i1 = 0; i1 < i; i1++) 
                {
                    listaTarefas.append(i1 + 1).append(". ").append(lista[i1]).append("\n");
                }
                JOptionPane.showMessageDialog(null, listaTarefas.toString());
    }

    public static void concluir(String[] lista, int i)
    {
        if (i == 0) 
        {
            JOptionPane.showMessageDialog(null, "Nenhuma tarefa para concluir.");
            return;
        }

        StringBuilder listaTarefas = new StringBuilder("Qual tarefa deseja concluir?: \n");
        for (int i1 = 0; i1 < i; i1++) 
        {
            listaTarefas.append(i1 + 1).append(". ").append(lista[i1]).append("\n");
        }
        String opcConcluirStr = JOptionPane.showInputDialog(listaTarefas.toString());
        int opcConcluirInt = Integer.parseInt(opcConcluirStr);
        
        for (int v = 0; v < lista.length; v++) 
        {
            if (v == opcConcluirInt-1) 
            {
                lista[v] = lista[v] + " FEITO!";
                
            }
        }
    }

    public static void main(String[] args) {

        String[] lista = new String[10];
        int i = 0;

        do {
            String opcao = JOptionPane.showInputDialog(null, "Comandos disponíveis:\r\n"
                    + "- \"adicionar\" para adicionar uma nova tarefa\r\n"
                    + "- \"listar\" para listar as tarefas\r\n"
                    + "- \"concluir\" para marcar uma tarefa como concluída\r\n");

            if (opcao.equals("adicionar")) 
            {
                adicionar(lista, i);
                i++;
            }

            else if (opcao.equals("listar")) 
            {
                listar(lista, i);
            }
            
            else if (opcao.equals("concluir")) 
            {
                concluir(lista, i);
            }
            else 
            {
                JOptionPane.showMessageDialog(null, "Comando inválido. Tente novamente.");
            }

        } while (!"sair".equals(JOptionPane.showInputDialog("Deseja sair do programa? (Digite \"sair\" para sair)")));
    }
}

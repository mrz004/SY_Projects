package project;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.CountDownLatch;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.GridBagConstraints;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Quiz {

  private class GUI extends JFrame {
    String question, options[];
    JLabel questionLabel;
    JButton[] buttons = new JButton[4];
    String opNames[] = { "A.", "B.", "C.", "D." };
    private CountDownLatch latch;
    private int choice;

    private class ClickeHandler implements ActionListener {
      @Override
      public void actionPerformed(ActionEvent e) {
        JButton btn = (JButton) e.getSource();
        String str = btn.getText().substring(3);
        for (int i = 0; i < GUI.this.options.length; i++)
          if (GUI.this.options[i].equals(str))
            GUI.this.choice = i;

        GUI.this.latch.countDown();
      }
    }

    private void setQuestion(int qn) {
      questionLabel.setText("Q " + qn + ". " + question);
      for (int i = 0; i < options.length; i++)
        buttons[i].setText(this.opNames[i] + " " + options[i]);
    }

    int updateQuestion(int qn, String[] question) {
      this.latch = new CountDownLatch(1);
      this.question = question[0];
      this.options = getOptions(question);
      setQuestion(qn);
      try {
        this.latch.await();
        return choice;
      } catch (InterruptedException e) {
        e.printStackTrace();
      }
      return -1;
    }

    String[] getOptions(String[] question) {
      String[] options = new String[4];
      for (int i = 1, j = 0; j < 4; i++, j++)
        options[j] = question[i];
      return options;
    }

    GUI() {
      this.setTitle("Quiz Game");

      JPanel contentPanel = new JPanel();
      contentPanel.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
      this.add(contentPanel);
      this.questionLabel = new JLabel();
      for (int i = 0; i < buttons.length; i++) {
        buttons[i] = new JButton();
        buttons[i].addActionListener(new ClickeHandler());
      }

      contentPanel.setLayout(new GridBagLayout());
      GridBagConstraints constraints = new GridBagConstraints();
      constraints.gridx = 0;
      constraints.gridy = 0;
      constraints.ipadx = 10;
      constraints.ipady = 5;
      constraints.insets = new Insets(20, 10, 10, 20);

      constraints.gridwidth = 2;
      contentPanel.add(this.questionLabel, constraints);

      constraints.gridwidth = 1;
      for (int i = 0; i < buttons.length / 2; i++)
        for (int j = 0; j < 2; j++) {
          constraints.gridy = i + 1;
          constraints.gridx = j;
          if (j == 1)
            constraints.anchor = GridBagConstraints.EAST;
          else
            constraints.anchor = GridBagConstraints.WEST;
          contentPanel.add(buttons[i * 2 + j], constraints);
        }

      this.setSize(720, 480);
      this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      this.setVisible(true);
    }
  }

  private class ResultView extends JFrame {

    static int arraySum(int[] arr) {
      int sum = 0;
      for (int i : arr)
        sum += i;
      return sum;
    }

    ResultView(int[] wins) {
      this.setTitle("Result Window");
      this.setLayout(new GridBagLayout());
      GridBagConstraints constraints = new GridBagConstraints();
      constraints.gridx = 0;
      constraints.gridy = 0;
      constraints.insets = new Insets(20, 0, 50, 0);
      constraints.fill = GridBagConstraints.HORIZONTAL;
      this.add(new JLabel("You got " + arraySum(wins) + " correct answers!", JLabel.CENTER), constraints);

      constraints.insets = new Insets(20, 20, 10, 20);
      constraints.fill = GridBagConstraints.NONE;
      for (int i = 0; i < wins.length / 2; i++)
        for (int j = 0; j < 2; j++) {
          constraints.gridx = j;
          constraints.gridy = i + 1;

          int index = i * 2 + j;
          int elem = wins[index];
          this.add(new JLabel("Ans. " + (index + 1) + " : " + (elem == 1 ? "Correct" : "Wrong")), constraints);
        }

      this.setSize(720, 480);
      this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      this.setVisible(true);
    }
  }

  public static void main(String[] args) throws FileNotFoundException {
    int[] wins = new int[10];
    int choice;
    Random rnd = new Random();
    File file = new File("q.txt");
    Scanner sc = new Scanner(file);
    String[][] questions = new String[20][6];
    for (int i = 0; i < 20; i++) {
      for (int j = 0; j < 6; j++) {
        if (sc.hasNextLine())
          questions[i][j] = sc.nextLine();
      }
    }

    GUI gui = new Quiz().new GUI();

    for (int i = 0; i < 10; i++) {
      int rand = rnd.nextInt(20);
      choice = gui.updateQuestion(i + 1, questions[rand]);
      System.out.println("choice: " + questions[rand][choice + 1] + " ans: " + questions[rand][5]);
      if (questions[rand][choice + 1].equals(questions[rand][5])) {
        wins[i] = 1;
      } else {
        wins[i] = 0;
      }
    }
    gui.dispose();
    new Quiz().new ResultView(wins);
    // System.out.println("The total number of time you win : " + arraySum(wins));
    for (int i = 0; i < 10; i++) {
      System.out.print(
          "Ans. " + (i + 1) + " : " + (wins[i] == 1 ? "Correct!" : "Wrong!") + ((i + 1) % 4 == 0 ? "\n" : "\t\t\t\t"));

    }
  }
}

package project;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;
import java.util.Scanner;

public class Quiz {

  static int arraySum(int[] arr) {
    int sum = 0;
    for (int i : arr) sum += i;
    return sum;
  }

  public static void main(String[] args) throws FileNotFoundException {
    int[] wins = new int[10];
    int choice;
    File file = new File("q.txt");
    Scanner sc = new Scanner(file);
    Scanner con = new Scanner(System.in);
    String[][] questions = new String[20][6];
    for (int i = 0; i < 20; i++) {
      for (int j = 0; j < 6; j++) {
        if (sc.hasNextLine()) questions[i][j] = sc.nextLine();
      }
    }
    for (int i = 0; i < 10; i++) {
      Random rnd = new Random();
      int rand = rnd.nextInt(6);
      System.out.println("Q." + (i + 1) + ")" + questions[rand][0]);
      System.out.println("(1)" + questions[rand][1] + "\t\t\t\t\t" + "(2)" + questions[rand][2]);
      System.out.println("(3)" + questions[rand][3] + "\t\t\t\t\t" + "(4)" + questions[rand][4]);
      System.out.println();
      choice = con.nextInt();
      if (questions[rand][choice].equals(questions[rand][5])) {
        wins[i] = 1;
      } else {
        wins[i] = 0;
      }
    }
    System.out.println("The total number of time you win : " + arraySum(wins));
    for (int i = 0; i < 10; i++) {
      System.out.print("Ans. " + (i+1) + " : " + (wins[i] == 1 ? "Correct!" : "Wrong!") + ((i+1)%4==0?"\n":"\t\t\t\t"));

    }
  }
}

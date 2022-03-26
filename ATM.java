package project;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Objects;
import java.util.Scanner;



public class ATM {
    static ManegeFile manegeFile;

    static {
        try {
            manegeFile = new ManegeFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    static Scanner sc = new Scanner(System.in);

    static void applyNew() throws IOException {
        User temp = new User();
        sc.nextLine();
        System.out.print("Enter you name : ");
        temp.name = sc.nextLine();
        System.out.print("Enter you password : ");
        temp.pass = sc.nextLine();
        System.out.print("Enter the amount you want to initially deposit : ");
        temp.balance = sc.nextLong();

        System.out.format("You have entered the following values :\n\t-Name: %s\n\t-Account number: %s\n\t-password: %s\n\t-money to deposit: %s\nEnter (y) to creat account: ", temp.name, temp.accountNumber, temp.pass, temp.balance);
        char confirm = sc.next().charAt(0);
        if (confirm == 'y'){
            manegeFile.userData.add(temp);
        }
    }

    public static void main(String[] args) throws IOException {
        User u = new User();
        u.setValues("asd", "pass", 1000);

        System.out.println("Welcome,\n\tThank you for visiting our ATM.\nHow can we help you!\n");
        do {
            System.out.println("\nChose a action to proceed\n\t1. Balance enquiry\n\t2. Withdraw money\n\t3. Apply for new account\n\t0. Exit");
            char choice = sc.next().charAt(0);
            switch (choice) {
                case '0' -> manegeFile.exit(0);
                case '1' -> System.out.println("case 1");
                case '2' -> System.out.println("case 2");
                case '3' -> applyNew();
                default -> System.out.println("Wrong choice!");
            }
        } while (true);
    }
}

class User{
    public String name;
    public long accountNumber;
    public String pass;
    public long balance;
    private static long ANCount = 1000000000;

    public User() {
        this.accountNumber = ANCount;
        ANCount++;
    }

    public void setValues(String name, String pass, long balance){
        this.name = name;
        this.pass = pass;
        this.balance = balance;
    }

}

class ManegeFile {
    File file = new File("user");
    ArrayList<User> userData = new ArrayList<>();


    public ManegeFile() throws IOException {
        if (!file.exists()){
            if (!file.createNewFile()){
                System.out.println("!Unable to create the file: " + file.getName() + "\n");
            }
            else {
                System.out.println("File \"" + file.getName() + "\" crated successfully." + "\n");
                // TODO: 22-Feb-22 Add some default accounts for demo purpose
            }

        }
        else {
            Scanner fileReader = new Scanner("user");
            String s;
            while (fileReader.hasNextLine()){
                User temp = new User();
                s = fileReader.nextLine();
                if (Objects.equals(s, "{")){
                    temp.name = fileReader.nextLine();
                    temp.accountNumber = Long.parseLong(fileReader.nextLine());
                    temp.pass = fileReader.nextLine();
                    temp.balance = Long.parseLong(fileReader.nextLine());
                }
                boolean add = userData.add(temp);
                if (add){
                    System.out.println("User added successfully.");
                }
                else{
                    System.out.println("Unable to add user!\nplease try again.");
                }
            }
        }
    }

    public void exit(int status) throws IOException {
        FileWriter fileWriter = new FileWriter("user");
        if (userData.size()>0){
            fileWriter.write(String.valueOf(userData.get(userData.size()-1).accountNumber));
        }
        for (User i : userData) {
            addUser(i);
        }
        // TODO: 23-Feb-22 complete the methode by appending all the users in the file.

        System.exit(status);
    }

    public void addUser(User x) throws IOException {
        FileWriter fileWriter = new FileWriter("user", true);
//        String s = x.name + '|' + x.accountNumber + '|' + x.pass + '|' + x.balance;
        fileWriter.write("{\r\n");
        fileWriter.write(x.name + "\r\n");
        fileWriter.write(String.valueOf(x.accountNumber) + "\r\n");
        fileWriter.write(x.pass + "\r\n");
        fileWriter.write(String.valueOf(x.balance) + "\r\n");
        fileWriter.write("}\r\n");
        fileWriter.close();
// System.out.println("\n\nWrote to the file successfully\n");
    }
}

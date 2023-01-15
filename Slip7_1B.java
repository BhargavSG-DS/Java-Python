import java.io.*;

class Cricket {
  String Name;

  int Total_runs;

  int Notout;

  int Inning;

  float avg;

  void accept() {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    try {
      System.out.print("Enter Name of Player : ");

      Name = br.readLine();

      System.out.print("Enter Total Runs of Player : ");

      Total_runs = Integer.parseInt(br.readLine());

      System.out.print("Enter Name of Tixes Not out : ");

      Notout = Integer.parseInt(br.readLine());

      System.out.print("Enter Innings played by players : ");

      Inning = Integer.parseInt(br.readLine());
    } catch (Exception e) {}
  }

  void average() {
    avg = Total_runs / Inning;

    System.out.println(
      "Name : " +
      Name +
      "\nTotal runs : " +
      Total_runs +
      "\nAvergae : " +
      avg +
      "\nInning : " +
      Inning
    );
  }
}

public class Slip7_1B {

  public static void main(String args[]) {
    float max = 0;

    int n;

    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    try {
      System.out.print("How many Players : ");

      n = Integer.parseInt(br.readLine());

      Cricket ob1[] = new Cricket[n];

      for (int i = 0; i < n; i++) {
        ob1[i] = new Cricket();

        ob1[i].accept();
      }

      for (int i = 0; i < n; i++) {
        ob1[i].average();
      }

      for (int i = 0; i < n; i++) {
        if (max < ob1[i].avg) {
          max = ob1[i].avg;
        }
      }

      System.out.println("-----------------------------\nMax avg : " + max);
    } catch (Exception e) {
      System.out.println("Error........." + e);
    }
  }
}

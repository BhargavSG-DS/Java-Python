import java.io.DataInputStream;

class Slip13_1B {

    public static void main(String args[]){

        String str;

        DataInputStream dr = new DataInputStream(System.in);

        try {

            System.out.print("Enter Username : ");

            str = dr.readLine();

            System.out.print("\"Hello, " + str.toUpperCase() + ", nice to meet you!\"");

        } catch (Exception e) {}

    }

}
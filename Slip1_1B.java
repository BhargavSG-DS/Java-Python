import java.io.*;

public class Slip1_1B {
    public static void main(String[] args) throws IOException {
        System.out.println("reading file...");
        FileReader fileReader = new FileReader("src/test#1.txt");
        // enter your source file location
        FileWriter fileWriter = new FileWriter("src/testoutput.txt");
        // enter your destination file location
        int data = fileReader.read();
        System.out.println("writing file...");
        while (data != -1){
            String content = String.valueOf((char)data);
            if(Character.isAlphabetic(data)) {
                fileWriter.append(content);
            }else if(content.equals(" ")){
                fileWriter.append(" ");
            }
            data = fileReader.read();
        }
        System.out.println("\nCOPY FINISHED SUCCESSFULLY...");
        fileWriter.close();
        fileReader.close();
    }
}
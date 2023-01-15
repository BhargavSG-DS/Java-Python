import java.io.File;

class Slip8_1B {

    public static void main(String[] args) {

        File file = new File("src/");

        String[] fileList = file.list();

        for(String str : fileList) {

            if(str.endsWith(".txt")){

                System.out.println(str);

            }

        }

    }

}
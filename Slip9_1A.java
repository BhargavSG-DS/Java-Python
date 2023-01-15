import java.io.*;

public class Slip9_1A {

    public static void main(String[] args) {

        int num = 4;

        for (int i=0;i<num;i++){

            for(int j=0;j<=i;j++){

                if (i<2){

                    if ((i+j)%2==0){

                        System.out.print("1 ");

                    }else{

                        System.out.print("0 ");

                    }

                }else{

                    if ((i+j)%2==0){

                        System.out.print("0 ");

                    }else{

                        System.out.print("1 ");

                    }

                }

            }System.out.println();

        }

    }

}
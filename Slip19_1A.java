import java.util.*;

class Slip19_1A{
    public void Fibonacci(int num){
        int a = 0;
        int b = 1;
        int temp;
        for (int i =0 ;i<num;i++){
            System.out.print(b + " ");
            temp = a + b;
            a = b;
            b = temp;
        }

    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Slip19_1A obj = new Slip19_1A();
        obj.Fibonacci(n);
    }
}
import java.util.*;

class Slip16_1A{
    public int dsum(int num){
        if (num == 0){
            return 0;
        }
        int sum = num%10;
        num = num/10;
        sum += dsum(num);
        return sum;

    }
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Slip16_1A obj = new Slip16_1A();
        System.out.print(obj.dsum(n));
    }
}
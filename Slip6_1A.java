import java.util.*;
class ZeroException extends Exception{
    ZeroException(){
        super("Number is 0");
    }
}
class Slip6_1A{
    public static void main(String[] args) {
        int r,sum=0,temp;
        try{
            Scanner sc=new Scanner(System.in);
            int n=sc.nextInt();
            sc.close();
            if(n==0){
                throw new ZeroException();
            }
            else{
                temp=n;
                while(n>0){
                    r=n%10;
                    sum=(sum*10)+r;
                    n=n/10;
                }
                if(temp==sum)
                System.out.println("palindrome number "+temp);
                else
                System.out.println("not palindrome number");
            }
               
        }catch (Exception e){
            System.out.println(e);
        }
    }
}
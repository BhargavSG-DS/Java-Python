import java.io.*;

class Slip25_1A

{

public static void main(String ar[])throws IOException

{

BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

System.out.println("enter the string ");


String str=br.readLine();

String temp=str;

StringBuffer sb=new StringBuffer(str);

sb.reverse();

str=sb.toString();

if(temp.equalsIgnoreCase(str))

System.out.println("the string is palindrome");

else

System.out.println("the string is not palindrome");

}

}
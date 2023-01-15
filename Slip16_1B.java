import java.util.*;

class Slip16_1B

{

static String[] str=new String[5];

static Scanner sc=new Scanner(System.in);

static ArrayList<String>list=new ArrayList<String>();

public static void main(String args[])

{

for(int i=0;i<str.length;i++)

{ 

System.out.print("please insert employee name of index of["+i+"] :");

str[i]=sc.next();

list.add(str[i]);

}

Collections.sort(list);

System.out.println(list);

}

}
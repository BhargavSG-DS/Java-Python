import java.io.*;

import java.util.*;

class Slip13_1A

{

public static void main(String arg[])

{

Scanner sc=new Scanner(System.in);

System.out.println("enter the limit of array list");

int n=sc.nextInt();

ArrayList al=new ArrayList();

System.out.println("enter the elements of arry list");

for(int i=0;i<n;i++)

{

String el=sc.next();

al.add(el);

}

System.out.println("the original array list is :"+al);

Collections.reverse(al);

System.out.println("the original reverse array list is :"+al);

}

}


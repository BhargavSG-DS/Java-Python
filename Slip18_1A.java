import java.io.*;

import java.util.*;

class areaCalculation

{

void area(int r)

{

System.out.println("Area of circle="+(3.14*r*r));

}

float area(int b,float h)

{

return b*h/2;

}

double area(float l,float rb)

{

return l+rb;

}

}

class Slip18_1A

{

public static void main(String args[])

{

int r,b,l,rb;

float h;

Scanner sc=new Scanner(System.in);

System.out.print("Enter rdius :");

r=sc.nextInt();

System.out.print("Enter base :");

b=sc.nextInt();

System.out.print("Enter height :");

h=sc.nextFloat();

System.out.print("Enter lenght :");

l=sc.nextInt();

System.out.print("Enter breadth :");

rb=sc.nextInt();

areaCalculation ac=new areaCalculation();

ac.area(r);

System.out.println("area of triangle ="+ac.area(b,h));

System.out.println("area of rectangle ="+ac.area(l,rb));

}

}
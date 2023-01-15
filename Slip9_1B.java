import java.io.*;

class invaliddetails extends Exception{}

class Slip9_1B{

    static int n;

    public static void main( String args[]){

        DataInputStream dr = new DataInputStream(System.in);

        try {

            System.out.print("********* Do you Want to Validate ********* \n1. Mobile Number Press : 1 \n2. PAN Card Press : 2 \nEnter Number : ");

            n = Integer.parseInt(dr.readLine());

            switch(n){

                case 1 :

                System.out.print("Enter Mobile Number : ");

                Long num = Long.parseLong(dr.readLine());

                    if(num.toString().matches("(0/91)?[7-9][0-9]{9}")){

                        System.out.print("Enter Valid Mobile Number..!");

                    }else{

                        throw new invaliddetails();

                    }

                break;

                case 2 :

                System.out.print("Enter PAN Number : ");

                String str= dr.readLine();

                if(str.matches("[A-Z]{5}[0-9]{4}[A-Z]{1}")){

                    System.out.print("Enter Valid PAN CARD Number..!");

                }else{

                    throw new invaliddetails();

                }

                break;

                default :

                    throw new invaliddetails();

            }

        } catch (invaliddetails nz) {

            System.out.println("You Enter Invalid Details...!");

        }

        catch (NumberFormatException e){

            System.out.println("You Enter Invalid Details...!");

        }

        catch(Exception e){}

    }

}
import javax.swing.*;
import java.awt.*;
class Slip7_1A
{
	//Driver function
	public static void main(String args[])
	{
		//Create a frame
		JFrame frame=new JFrame("Slip7 -Q1 -A");
		frame.setSize(500,500);
		frame.getContentPane().setBackground(Color.RED);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
		frame.setLayout(null);
		//Create a Label
		JLabel label=new JLabel();
		label.setBounds(0,100,500,50);
		frame.add(label);
		//Write text to the label
		String str="Dr. D Y Patil College";
		label.setText(str);
        label.setFont(new Font("Arial",Font.BOLD,20));
		//Display the frame
		frame.setVisible(true);
	}
}
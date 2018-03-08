import java.util.Scanner;
public class OneChicken {
    public static void main(String[] args) {
        Scanner scan = new Scanner (System.in);
        int guests = scan.nextInt();
        int chicken = scan.nextInt();

        if (guests > chicken) {
        	if (guests-chicken==1) System.out.println("Dr. Chaz needs 1 more piece of chicken!");
        	else System.out.println("Dr. Chaz needs " + (guests-chicken) +" more pieces of chicken!");
        }
        else {
        	if (chicken-guests ==1) System.out.println("Dr. Chaz will have 1 piece of chicken left over!");
        	else System.out.println("Dr. Chaz will have "+(chicken-guests)+" pieces of chicken left over!");
        }
  	}
}


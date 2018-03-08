import java.util.Scanner;
public class MixedFractions {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        while(true) {
        	int n = scan.nextInt();
        	int m = scan.nextInt();

        	if (n==0 && m==0) break;

        	System.out.println(n/m +" " + n%m+" / "+m);
        }
    }
}

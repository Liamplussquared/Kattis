import java.util.Scanner;
public class Filip {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int m = scan.nextInt();

		//reverse
		String temp =n%10+""+(n/10)%10+""+n/100;
		n = Integer.parseInt(temp);
		temp = m%10+""+(m/10)%10+""+m/100;
		m = Integer.parseInt(temp);

		System.out.println(Math.max(n,m));
    }
}

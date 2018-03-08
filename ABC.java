import java.util.*;
public class ABC {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int array[] = new int[3];
        for(int i = 0;i<3; i++) {
        	array[i] = scan.nextInt();
        }
        Arrays.sort(array);
        scan.nextLine();
        String abc  = scan.nextLine();
		for(int i = 0; i<3; i++) {
			if(abc.charAt(i)=='A') System.out.print(array[0] +" ");
			else if(abc.charAt(i)=='B') System.out.print(array[1] + " ");
			else System.out.print(array[2] + " ");
		}
    }
}

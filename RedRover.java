import java.util.Scanner;
public class RedRover {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //need to find longest repeated substring in input
        String decoded = scan.nextLine();
        int shortestlength = decoded.length();

        for(int i = 0; i < decoded.length()-1; i++) {
        	for(int j = i+1; j< decoded.length(); j++) {
        		String code = decoded.substring(i, j+1);
        		int length = decoded.replaceAll(code,"M").length() + code.length();
        		if (length < shortestlength)
        			shortestlength = length;
        	}
        }
        System.out.println(shortestlength);

    }
}

import java.util.Scanner;
import java.util.Arrays;
public class ClosingTheLoop {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = Integer.parseInt(scan.nextLine());
        int testcase = 1;
        while (n>0) {

        	int s = Integer.parseInt(scan.nextLine());
        	String segments = scan.nextLine();
        	String[] words = segments.split(" ");
        	//get count of how many R, B to find size for arrays

        	int r = 0, b=0;
        	for(int i = 0; i < words.length; i++) {
        		if(words[i].matches(".*R.*"))
        			r++;
        		else
        			b++;
        	}
        	//System.out.println("RED " + r + " BLUE " + b);
        	if(r == 0 | b ==0) {
        		System.out.println("Case #" + testcase + ": 0");
        		testcase++;
        		n--;
        	}
        	else{

        		int rarr[] = new int[r];
        		int barr[] = new int[b];

				//FILL INT ARRAYS WITH LENGTHS
        		int rc = 0;
        		int bc = 0;
        		for(int i = 0; i < words.length; i++) {
        			if(words[i].matches(".*R.*")) {
        				rarr[rc] = Integer.parseInt(words[i].substring(0,words[i].length()-1));
        				rc++;
        			}

        			else {
        				barr[bc] = Integer.parseInt(words[i].substring(0,words[i].length()-1));
        				bc++;
        			}
        		}
        		Arrays.sort(rarr);
        		Arrays.sort(barr);
				//System.out.println(rarr[1]);
				int min = Math.min(r,b); //print out highest limit sum of lenths...
				//System.out.println(min);
				int sum = 0;
				for(int i = min; i > 0; i--) {
					sum+=rarr[r-1];
					r--;
					sum--;
					sum+=barr[b-1];
					b--;
					sum--;
				}

				System.out.println("Case #"+testcase+": "+sum);
				testcase++;
				n--;
        	}
        }
    }
}

import java.util.Scanner;
public class StackingCups {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        //colour radius or diamter colour as input
        String cups[] = new String[Integer.parseInt(scan.nextLine())];
        for(int i = 0; i < cups.length; i++) {
        	cups[i] = scan.nextLine();
        }

        //need to find proper size
        double sizes[] = new double[cups.length];
        for (int i = 0; i < cups.length; i++) {
        	if(cups[i].matches(".*[0-9]+")) {
        		String seperated[] = cups[i].split(" ");
        		sizes[i]=2.0 *Double.parseDouble(seperated[1]);
        	}
        	else {
        		String split[]=cups[i].split(" ");
        		sizes[i] = (Double.parseDouble(split[0]));
        	}

        //	System.out.println(sizes[i]);
        }

        //now have to order --INSERTION SORT
        double temp;
        String temp2;
        for(int i = 1; i < cups.length; i++) {
				int j = i;
				temp = sizes[i];
				temp2 = cups[i];
				while (j > 0 && temp < sizes[j-1]) {
					sizes[j] = sizes[j-1];
					cups[j] = cups [j-1];
					j--;
				}
				sizes[j] = temp;
				cups[j] = temp2;
        	}

       for (int i = 0; i < cups.length; i++) {
       		if(cups[i].matches("[a-z]+.*")) {
       			String s1[] = cups[i].split(" ");
       			System.out.println(s1[0]);
       		}
       		else{
       			String s2[] = cups[i].split(" ");
       			System.out.println(s2[1]);
       		}
       }
  	}
}


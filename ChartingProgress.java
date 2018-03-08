import java.util.*;


public class ChartingProgress {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        ArrayList<String> graph = new ArrayList<>();

        while(scan.hasNext()) {
        	while (scan.hasNext()) {
        		String row = scan.nextLine();

        		if(row.isEmpty()) { //space between inpouts
        			break;
        		}

        		graph.add(row);
        	}
        	int total = 0; //tracks how many columns in

        	for(String row : graph) {
        		char[] log = row.replace("*", ".").toCharArray();

        		int stars = row.length() - row.replace("*", "").length(); //total length - number of stars

        		for(int i = 0; i < stars; i++) {
        			log[row.length() -1 - total++] = '*'; //moves in left
        		}
        		System.out.println(new String(log)); //making String out of char array!
        	}
        	System.out.println();
       		 }
        }
    }



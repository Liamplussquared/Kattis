import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;
import java.util.ArrayList;
public class Peragram {
    public static void main(String[] args) {
        //Using ArrayList... dynamic arrays that can grow as needed
        //more accessible than Linked Lists and less limited than arrays
        Kattio scan = new Kattio(System.in);
        ArrayList oddcharacters = new ArrayList();
        String input = scan.getWord();

        //want to loop through input and remove
        for(int i = 0; i < input.length(); i++) {
        	if (oddcharacters.contains(input.substring(i,i+1))) { //ONLY REMOVED IF HAS PAIR
        		oddcharacters.remove(oddcharacters.indexOf(input.substring(i,i+1)));
        	}
        	else {
        		oddcharacters.add(input.substring(i, i+1));
        	}
        }
        if (oddcharacters.size()==0) {
        	System.out.println("0");
        }
        else {
        	System.out.println(oddcharacters.size() - 1); //a single character is a palindrome
        }
    }
}


class Kattio extends PrintWriter {
    public Kattio(InputStream i) {
	super(new BufferedOutputStream(System.out));
	r = new BufferedReader(new InputStreamReader(i));
    }
    public Kattio(InputStream i, OutputStream o) {
	super(new BufferedOutputStream(o));
	r = new BufferedReader(new InputStreamReader(i));
    }

    public boolean hasMoreTokens() {
	return peekToken() != null;
    }

    public int getInt() {
	return Integer.parseInt(nextToken());
    }

    public double getDouble() {
	return Double.parseDouble(nextToken());
    }

    public long getLong() {
	return Long.parseLong(nextToken());
    }

    public String getWord() {
	return nextToken();
    }



    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
	if (token == null)
	    try {
		while (st == null || !st.hasMoreTokens()) {
		    line = r.readLine();
		    if (line == null) return null;
		    st = new StringTokenizer(line);
		}
		token = st.nextToken();
	    } catch (IOException e) { }
	return token;
    }

    private String nextToken() {
	String ans = peekToken();
	token = null;
	return ans;
    }
}


import java.util.*;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;
public class CompoundWords {
    public static void main(String[] args) {
        Kattio scan = new Kattio(System.in);
        //Using Set... collections that can not contain duplicates!
        ArrayList<String> list = new ArrayList<>();
        Set<String> set = new TreeSet<>(); //

        while(scan.hasMoreTokens()) {
        	list.add(scan.getWord());
        }
        for(int i = 0; i < list.size(); i++) {
        	for(int j = 0; j < list.size(); j++) {
        		if (i!=j) set.add(list.get(i)+list.get(j));
        	}
        }

        for(String i: set) {
        	System.out.println(i); //prints out each element of set... don't need to know bounds
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

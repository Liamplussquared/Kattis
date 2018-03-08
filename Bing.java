import java.util.Scanner;
import java.util.ArrayList;
public class Bing {
	public static void main(String args[]) {
		new Bing().trie();
	}


	public  void trie() {
		Scanner scan = new Scanner(System.in);
		int numWords = Integer.parseInt(scan.nextLine());
		Tree root = new Tree(' ');
		Tree[] roots = new Tree[26]; //alphabet

		for(int i = 0; i < numWords; i++) {
			String word = scan.nextLine();
			System.out.println(root.add(word,0)-1);
		}
	}

	private class Tree {
		char letter;
		int count = 0;
		Tree[] others = new Tree[26]; //tree under every root

		public Tree(char c) {
			letter = c;
		}

		public int add(String s, int index) {
			count++;
			if (index == s.length()) {
				return count;
			}
			char c = s.charAt(index);
			if(others[c-'a'] == null) {
				others[c - 'a'] = new Tree(c);
			}
			return others[c-'a'].add(s,index+1);
		}
	}
}
import java.util.Scanner;
public class TrollHunt {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int bridges = scan.nextInt()-1;
       	int groups = scan.nextInt() / scan.nextInt();
        if(bridges%groups==0) System.out.println(bridges / groups);
        else System.out.println(bridges/groups + 1);
    }
}

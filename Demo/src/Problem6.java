
public class Problem6 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i,j;
		int odd=1;
		int noOfspace=2;
		for (i=1;i<=3;i++) {
			for (j=1;j<=noOfspace;j++) {
				System.out.print(" ");
			}
		    for (j=1;j<=odd;j++) {
		    	System.out.print("*");
		    }
		    System.out.println();
		    odd=odd+2;
		    noOfspace=noOfspace-1;
		}

	}

}

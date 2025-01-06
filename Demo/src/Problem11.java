
public class Problem11 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i,j;
		int k=0;
		for(i=1;i<=3;i++) {
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
		for (i=1;i<=3;i++) {
			int noOfspace1=0;
			int odd1=5;
			for (i=1;i<=3;i++) {
				for(j=1;j<=noOfspace1;j++) {
					System.out.print(" ");
				}
				for (j=1;j<=odd1;j++) {
					System.out.print("*");
				}
				System.out.println();
				noOfspace1=noOfspace1+1;
				odd1=odd1-2;
		}
		}
		}
	}
}

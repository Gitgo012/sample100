
public class Problem9 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i,j;
		int noOfspace=0;
		int odd=5;
		for (i=1;i<=3;i++) {
			for(j=1;j<=noOfspace;j++) {
				System.out.print(" ");
			}
			for (j=1;j<=odd;j++) {
				System.out.print("*");
			}
			System.out.println();
			noOfspace=noOfspace+1;
			odd=odd-2;
		}

	}

}

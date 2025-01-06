public class Problem5
{
    public static void main(String args[]) {
    	int odd=1;
    	int i,j;
    	int noOfspace=3;
        for(i=1;i<=4;i++) {
        	for(j=1;j<=noOfspace;j++) {
        		System.out.print(" ");
        	}
        	int k=0;
        	for(j=1;j<=odd;j++) {
        		if (j<=i) {
        			k=k+1;
        		}
        		else {
        			k=k-1;
        		}
        		System.out.print(k);        			
        	}
            System.out.println();
            odd=odd+2;
            noOfspace=noOfspace-1;
        }
}
}
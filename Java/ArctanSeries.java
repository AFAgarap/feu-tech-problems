public class ArctanSeries{
	public static void main(String[]args){
		double x = new java.util.Scanner(System.in).nextDouble();
		int k = new java.util.Scanner(System.in).nextInt();
		double answer = x;
		for(int i = 1, j = 1; i <= k; i++, j+=2){
			if(i == 1){
				answer -= Math.pow(x, (j + 2)) / (j + 2);
				System.out.print("if: ");
			}else if(i % 2 == 0){
				answer += Math.pow(x, j) / j;
				System.out.print("else if (even): ");
			}else if(i % 2 != 0){
				answer -= Math.pow(x, j) / j;
				System.out.print("else if (odd): ");
			}
			System.out.println(answer);
System.out.println("j: " + j);
		}
		System.out.println("Answer: " + answer);
	}
}

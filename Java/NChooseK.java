public class NChooseK{
	public static void main(String[]args){
		int n = new java.util.Scanner(System.in).nextInt();
		int k = new java.util.Scanner(System.in).nextInt();
		System.out.println(factorial(n) / (factorial(k) * factorial(n - k)));
	}
	private static int factorial(int n){
		return (n > 0) ? n * factorial(n - 1) : 1;		
	}
}

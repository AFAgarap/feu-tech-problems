public class Cigarettes{
	public static void main(String[] args) {
		int n = new java.util.Scanner(System.in).nextInt();
		int k = new java.util.Scanner(System.in).nextInt();
		int x = 0, total = n;
		while(true){
			x = n / k;
			total += x;
			if (x / k == 0) break;
			else n = x;
		}
		System.out.println(total);
	}
}

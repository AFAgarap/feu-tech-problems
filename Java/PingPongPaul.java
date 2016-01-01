public class PingPongPaul{
	public static void main(String[]args){
		java.util.Scanner in = new java.util.Scanner(System.in);
		int n = in.nextInt(); int p = in.nextInt(); int q = in.nextInt();
		System.out.println((((p + q) / n) % 2 == 0) ? "paul" : "opponent");
	}
}

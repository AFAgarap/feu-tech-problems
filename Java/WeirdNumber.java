public class WeirdNumber{
	public static void main(String[]args){
		int n = new java.util.Scanner(System.in).nextInt();
		System.out.println(n % 2 != 0 || n >= 5 && n <= 20 ? "Weird" : "Not Weird");
	}
}
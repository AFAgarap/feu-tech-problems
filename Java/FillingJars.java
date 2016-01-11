public class FillingJars{
	public static void main(String[] args) {
		int answer = 0, n = input("Enter n: "), m = input("Enter m: ");
		for (int i = 0; i < m; i++) {
			answer += (((input("Enter b: ") - input("Enter a: ")) + 1) * input("Enter k: "));
		}
		System.out.println(answer / n);
	}

	public static int input(String message){
		System.out.print(message);
		return new java.util.Scanner(System.in).nextInt();
	}
}
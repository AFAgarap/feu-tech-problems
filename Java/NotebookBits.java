public class NotebookBits{
	public static void main(String[] args) {
		int x = new java.util.Scanner(System.in).nextInt();
		int total = 0;
		for (int i = 1, j = 0; j < x; j++){
			if (j % 2 != 0) i++;
			total += i;
		}
		System.out.println(total);
	}
}
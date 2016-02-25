public class Kriti{
	public static void main(String[] args) {
		java.util.Scanner in = new java.util.Scanner(System.in);

		int numString = in.nextInt();
		
		String[] arr = new String[numString];
		
		for (int i = 0; i < arr.length; i++) {
			arr[i] = in.next();
		}

		int numQuery = in.nextInt();
		
		int[] count = new int[numQuery];
		
		int l = 0, r = 0;
		String s = "";

		for (int x = 0; x < numQuery; x++) {
			l = Integer.parseInt(in.next());
			r = Integer.parseInt(in.next());
			s = in.next();

			int counter = 0;

			for (int y = (l - 1); y < r; y++){
				if (s.equals(arr[y])) counter++;
			}
			count[x] = counter;
		}

		for (int x = 0; x < count.length; x++) {
			System.out.println(count[x]);
		}
	}
}
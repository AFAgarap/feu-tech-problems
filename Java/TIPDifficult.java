public class TIPDifficult{
	public static void main(String[] args) {
		/*long start = System.nanoTime();*/
		String line1 = "", line2 = "", line3 = "";
		for (int i = 1, j = 8; i < 10; i++, j-=2) {
			for (int k = i; k <= (i + j); k++){
				line1 += k < (i + j) ? " " : i;
			}
			// line1 += i;
			line2 += (i + j);
			line3 += line1 + " = " + line2 + "\n";
		}
		System.out.println(line3);
		/*long end = System.nanoTime();
		long totalTime = end - start;
		System.out.println(totalTime);*/
	}
}


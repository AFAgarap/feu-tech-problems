// Prints the given letter n times
// Where n is the preceding number to the letter
public class AlphaNumeric{
	public static void main(String[] args) {
		String line = new java.util.Scanner(System.in).next();
		for (int i = 0; i < line.length(); i++) {
			if (Character.isDigit(line.charAt(i)) && !Character.isDigit(line.charAt(i + 1))){
				for (int j = 0; j < Character.getNumericValue(line.charAt(i)); j++) {
					System.out.print((line.charAt(i + 1)));
				}
			}
			System.out.println();
		}
	}
}

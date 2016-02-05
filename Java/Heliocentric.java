public class Heliocentric{
	public static void main(String[] args) {
		int earthDays = new java.util.Scanner(System.in).nextInt();
		int marsDays = new java.util.Scanner(System.in).nextInt();
		int counter = 0;
		while(true){
			if (marsDays % 687 == 0 && earthDays % 365 == 0) break;
			earthDays++; marsDays++; counter++;
		}
		System.out.println(counter);
	}
}
public class Subsequence{
	public static void main(String[]args){
		java.util.Scanner in = new java.util.Scanner(System.in);

		java.util.List <String> strings = new java.util.ArrayList <String> ();

		String string;
		while ((string = in.nextLine()).length() > 0){
			strings.add(string);
		}

		String beale = "", key = "";

		for (int i = 1; i < strings.size(); i++){
			beale = "";
			for (int j = 0; j < strings.get(i - 1).length(); j++){
				if (strings.get(i).indexOf(strings.get(i - 1).charAt(j)) != -1){
					beale += strings.get(i - 1).charAt(j);
				}
			}
			strings.set((i), beale);
		}

		for (int i = 0; i < beale.length(); i++){
			if (key.indexOf(beale.charAt(i)) == -1){
				key += beale.charAt(i);
			}
		}

		System.out.printf("Length of longest common subsequence: %d\n", key.length());
	}
}

/**
*	Implementation of the first-in, first-out scheduling algorithm.
*/

public class FIFO {
	public static void main(String[] args) {
		int temp = 0;
		int size = input("How many processes will you enter? ");

		int [][] process = new int[size][6];

		for (int index = 0; index < size; index++) {
			process[index][0] = input("Enter arrival time for job #" + String.valueOf(index) + ": ");
			process[index][1] = input("Enter service time for job #" + String.valueOf(index) + ": ");
			System.out.println("================================");
		}

		for (int index = 0; index < size - 1; index++) {
			for (int j = 0; j < size - index - 1; j++) {
				if (process[j][0] > process[j + 1][0]) {
					temp = process[j][0];
					process[j][0] = process[j + 1][0];
					process[j + 1][0] = temp;
					
					temp = process[j][1];
					process[j][1] = process[j + 1][1];
					process[j + 1][1] = temp;
				}
			}
		}

		for (int index = 0; index < size; index++) {
			if (index == 0) {
				process[index][2] = 0;
			} else if (index != 0 && process[index - 1][3] < process[index][0]) {
				process[index][2] = process[index][0];
			} else if (index != 0 && process[index - 1][3] >= process[index][0]) {
				process[index][2] = process[index - 1][3];
			}
			process[index][3] = process[index][2] + process[index][1];
			process[index][4] = (index == 0 ) ? 0 : process[index][2] - process[index][0];
			process[index][5] = process[index][3] - process[index][0];
		}

		for (int index = 0; index < size; index++) {
			System.out.println(process[index][0] + " : " + process[index][1] + " : " + process[index][2] + " : " + process[index][3] + " : " + process[index][4] + " : " + process[index][5]);
		}
	}

	public static int input(String message) {
		System.out.print(message);
		int number = new java.util.Scanner(System.in).nextInt();
		return number;
	}
}
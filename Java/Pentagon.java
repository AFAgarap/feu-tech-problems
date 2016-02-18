public class Pentagon{
	public static void main(String[] args) {
		int[] arr = inputNumbers();
		int lowest = getLowest(arr) * -1, sum = getSum(arr), negative = 0;
		
		while(checkForNegativeNumbers(arr)){
			arr = subtractLowest(arr, getLowest(arr) * -1);
		}

		for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
			if (i == arr.length - 1) System.out.println();
		}
	}
	
	static int[] inputNumbers(){
		java.util.Scanner in = new java.util.Scanner(System.in);
		int[] arr = new int[5];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = in.nextInt();
		}
		return arr;
	}
	
	static int getSum(int[] arr){
		int sum = 0;
		for (int i = 0; i < arr.length; i++) {
			sum += arr[i];
		}
		return sum;
	}
	
	static int getLowest(int[] arr){
		int lowest = Integer.MAX_VALUE;

		for (int i = 0; i < arr.length; i++) {
			if (arr[i] < lowest) lowest = arr[i];
		}
		return lowest;
	}

	static int[] subtractLowest(int[] arr, int lowest){
		int index = 0, neighborOne = 0, neighborTwo = 0;
		int[] retArr = arr;
		for (int i = 0; i < arr.length; i++) {
			if (Math.abs(arr[i]) == lowest) {
				index = i;
				arr[i] *= -1;
				break;
			}
		}
		switch(index){
			case 0:
				neighborOne = 1; neighborTwo = 4;
				break;
			case 1:
				neighborOne = 0; neighborTwo = 2;
				break;
			case 2:
				neighborOne = 1; neighborTwo = 3;
				break;
			case 3:
				neighborOne = 2; neighborTwo = 4;
				break;
			case 4:
				neighborOne = 0; neighborTwo = 3;
				break;
		}
		retArr[neighborOne] -= arr[index];
		retArr[neighborTwo] -= arr[index];
		return retArr;
	}

	static boolean checkForNegativeNumbers(int[] arr){
		for (int i = 0; i < arr.length; i++){
			if (arr[i] < 0) return true;
		}
		return false;
	}
}
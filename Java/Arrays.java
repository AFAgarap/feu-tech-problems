public class Arrays{
	
	private int[] arr = new int[50];

	private int arrSize = 10;

	public void generateArray(){
		for(int i = 0; i < arrSize; i++){
			arr[i] = (int)(Math.random() * 10) + 10;
		}
	}
	
	public void printArray(){
		System.out.println("----------");
		for(int i = 0; i < arrSize; i++){
			System.out.print("| " + i + " | ");
			System.out.println(arr[i] + " |");
			System.out.println("----------");
		}
	}

	public int getValueAtIndex(int index){
		if(index < arrSize) return arr[index];
		return 0;
	}
	
	public boolean isInArray(int searchVal){
		for(int i = 0; i < arrSize; i++){
			if(searchVal == arr[i]) return true;
		}
		return false;
	}
	
	public void deleteElement(int index){
		if(index < arrSize){
			for(int i = index; i < (arrSize - 1); i++){
				arr[i] = arr[i + 1];
			}
		}
		arrSize--;
	}

	public void addElement(int value){
		if(arrSize < 50){
			arr[arrSize] = value;
			arrSize++;
		}
	}
	
	public String searchValue(int value){
		boolean valueInArray = false;
		String indicesWithValue = "";
		System.out.print("The value was found at the following: ");
		for(int i = 0; i < arrSize; i++){
			if(arr[i] == value){
				valueInArray = true;
				System.out.print(i + " ");
				indicesWithValue += i + " ";
			}
		}
		if(!valueInArray){
			indicesWithValue = "None";
			System.out.print(indicesWithValue);
		}
		System.out.println();
		return indicesWithValue;
	}

	public static void main(String[]args){
		Arrays newArr = new Arrays();
		newArr.generateArray();
		newArr.printArray();
		System.out.println("Value @ index 3: " + newArr.getValueAtIndex(3));
		System.out.println("Is 18 in array? " + newArr.isInArray(18));
		newArr.deleteElement(4);
		newArr.printArray();
		newArr.addElement(95);
		newArr.printArray();
		newArr.searchValue(17);
	}
}

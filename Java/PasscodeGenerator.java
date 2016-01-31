public class PasscodeGenerator{
	public static void main(String[]args) throws java.io.IOException{
		java.io.File file = new java.io.File("passcodes.txt");
		java.io.Writer writer = new java.io.FileWriter(file);
		for (int w = 0; w < 10; w++){
			for (int x = 0; x < 10; x++){
				for (int y = 0; y < 10; y++){
					for (int z = 0; z < 10; z++){
						writer.write(w + "" + x + "" + y + "" + z + "\n");
					}
				}
			}
		}
		writer.flush();
		writer.close();
	}
}

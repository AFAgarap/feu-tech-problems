public class Euler {
	public static void main(String[] args) {
		float x, y, m, i, dy_dx, delta_y;
		x = input("Enter value for x: ");
		y = input("Enter value for f(x): ");
		m = input("Approximate what? [f(x)] : ");
		i = input("Enter increment: ");

		while (x <= m) {
			dy_dx = F(x, y);
			delta_y = find_delta_y(dy_dx, i);
			System.out.printf("x: %.6f\ty: %.6f\tdy/dx: %.6f\tΔy: %.6f%n", x, y, dy_dx, delta_y);
			y += delta_y;
			x += i;
		}
	}

	static float input(String message) {
		float number;
		System.out.print(message);
		number = new java.util.Scanner(System.in).nextFloat();
		return number;
	}

	static float F(float x, float y) {
		return (2 * x) + (2 * y);
	}

	static float find_delta_y(float dy_dx, float i) {
		return dy_dx * i;
	}
}
#include <iostream>
#include <string>

float F(float x, float y);
float find_delta_y(float dy_dx, float i);
float input(std::string message);

int main() {
	// m = upper bound
	// i = increment
	float x, y, m, i, dy_dx, delta_y;
	x = input("Enter value for x: ");
	y = input("Enter value for f(x): ");
	m = input("Approximate what? [f(x)] : ");
	i = input("Enter increment: ");

	while (x <= m) {
		dy_dx = F(x, y);
		delta_y = find_delta_y(dy_dx, i);
		std::cout << "x: " << x << "\ty: " << y << "\tdy/dx: " << dy_dx << "\tΔy: " << delta_y << std::endl;
		y = y + delta_y;
		x = x + i;
	}
}

float F(float x, float y) {
	return (2.0 * x) + (2.0 * y);
}

float find_delta_y(float dy_dx, float i) {
	return dy_dx * i;
}

float input(std::string message) {
	float number;
	std::cout << message;
	std::cin >> number;
	return number;
}
def main():
    x = float(input("Enter value for x: "))
    y = float(input("Enter value for f(x): "))
    m = float(input("Approximate what? [f(x)] : "))
    i = float(input("Enter increment: "))
    delta_y = 0
    dy_dx = 0

    while x <= m:
        dy_dx = F(x, y)
        delta_y = find_delta_y(dy_dx, i)
        print("x:{}\ty:{}\tdy/dx:{}\tΔy:{}".format(x, y, dy_dx, delta_y))
        y = y + delta_y
        x = x + i


def F(x, y):
    return x - (2 * y) + 2


def find_delta_y(dy_dx, i):
    return dy_dx * i


if __name__ == "__main__":
    main()

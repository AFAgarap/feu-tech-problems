def main():
    n = input("Enter n: ")
    k = input("Enter k: ")
    print factorial(n) / (factorial(k) * factorial(n - k))


def factorial(n):
    return n * factorial(n - 1) if (n > 0) else 1


main()

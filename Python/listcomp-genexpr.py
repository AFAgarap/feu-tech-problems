#!/usr/bin/env python3

def main():
    # list comprehensions are greedy
    total = sum([num * num for num in range(0, 101)])
    print(total)

    # generator expressions are lazy
    total = sum(num * num for num in range(0, 101))
    print(total)

    # identifier
    print(id(3))
    c = 3
    print(id(c))

main()

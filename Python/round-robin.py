#!/usr/bin/env python3

import math

def main():
    quantum = int(input("Enter time quantum: "))
    size = int(input("How many processes will you enter? "))
    process = set_processes(size)
    process.sort()
    cycles = get_cycles(process, quantum)
    print(process)
    print(cycles)

def set_processes(size):
    process = []
    for index in range(0, size):
        process.append([
            int(input("Enter arrival time for P#{}: ".format(index + 1))),
            int(input("Enter service time for P#{}: ".format(index + 1)))
        ])
    return process

def get_cycles(process, quantum):
    cycles = []
    for index in range(0, len(process)):
        cycles.append(math.ceil((process[index][1] / quantum) + (process[index][1] % quantum)))
    return cycles

if __name__ == '__main__':
    main()

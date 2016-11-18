#!/usr/bin/env python3

def main():
    quantum = int(input("Enter time quantum: "))
    size = int(input("How many processes will you enter? "))
    process = set_processes(size)
    process.sort()
    process = get_cycles(process, quantum)
    print(process)

def set_processes(size):
    process = []
    for index in range(0, size):
        process.append([
            int(input("Enter arrival time for P#{}: ".format(index + 1))),
            int(input("Enter service time for P#{}: ".format(index + 1)))
        ])
    return process

def get_cycles(process, quantum):
    for index in range(0, len(process)):
        process[index].append((process[index][1] / quantum) + (process[index][1] % quantum))
    return process

if __name__ == '__main__':
    main()

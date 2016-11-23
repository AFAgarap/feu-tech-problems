#!/usr/bin/env python3

import math

def main():
    import os; os.system('clear')
    # quantum = int(input("Enter time quantum: "))
    # size = int(input("How many processes will you enter? "))
    # process = set_processes(size)
    quantum = 2
    process = [ [7, 9], [4, 4], [6, 3], [1, 2] ]
    process.sort()
    cycle = get_cycle(process[-1][1], quantum)
    print(get_queue(process=process, cycle=cycle, quantum=quantum))

def set_processes(size):
    process = []
    for index in range(0, size):
        process.append([
            int(input("Enter arrival time for P#{}: ".format(index + 1))),
            int(input("Enter service time for P#{}: ".format(index + 1)))
        ])
    return process

def get_cycle(process, quantum):
    cycle = math.floor((process / quantum) + (process % quantum))
    return cycle

def get_queue(process, cycle, quantum):
    queue = []
    for index in range(0, cycle):
        for element in range(0, len(process)):
            if not queue:
                queue.append(process[element][0])
                result = get_finished_time(burst_time=process[element][1], quantum=quantum, starting_time=queue[element])
                process[element][1], finished_time = result[0], result[1]
                queue[element] = [queue[element], finished_time]
            elif queue:
                if (process[element][0] <= queue[element - 1][1]):
                    queue.append(queue[element - 1][1])
                    result = get_finished_time(burst_time=process[element][1], quantum=quantum, starting_time=queue[element])
                    process[element][1], finished_time = result[0], result[1]
                    queue[element] = [queue[element], finished_time]
                elif (process[element][0] > queue[element - 1][1]):
                    queue.append(process[element][0])
                    result = get_finished_time(burst_time=process[element][1], quantum=quantum, starting_time=queue[element])
                    process[element][1], finished_time = result[0], result[1]
                    queue[element] = [queue[element], finished_time]
    return process, queue

def get_finished_time(burst_time, quantum, starting_time):
    if burst_time >= quantum:
        finished_time = starting_time + quantum
        burst_time -= quantum
    elif burst_time < quantum and burst_time != 0:
        finished_time = starting_time + burst_time
        burst_time -= burst_time
    return burst_time, finished_time

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import math

def main():
    quantum = int(input("Enter time quantum: "))
    size = int(input("How many processes will you enter? "))
    process = set_processes(size)
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
                result = get_finished_time(burst_time=process[element][1], quantum=quantum, starting_time=queue[index])
                process[element][1] = result[0]
                queue[index] = [queue[index], result[1]]
                print(queue)
                print(process)
            elif queue:
                if (process[element][0] <= queue[index - 1][1]):
                    pass
                elif (process[element][0] > queue[index - 1][1]):
                    pass
            # if process[element][1] >= quantum:
            #     queue[index].append(queue[index][0] + quantum)
            #     process[element][1] -= quantum
            # elif process[element][1] < quantum and process[element][1] != 0:
            #     queue[index].append(queue[index][0] + process[element][1])
            #     process[element][1] -= process[element][1]
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

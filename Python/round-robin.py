#!/usr/bin/env python3

import math


def main():
    import os

    os.system("clear")
    quantum = int(input("Enter time quantum: "))
    size = int(input("How many processes will you enter? "))
    process = set_processes(size)
    process.sort()
    process_temp = list(process)
    process_temp.sort(key=lambda x: x[1])
    cycle = get_cycle(process_temp[-1][1], quantum)
    process, queue = get_queue(process=process, cycle=cycle, quantum=quantum, size=size)
    print(process)
    print(queue)


def set_processes(size):
    process = []
    for index in range(0, size):
        process.append(
            [
                int(input("Enter arrival time for P#{}: ".format(index + 1))),
                int(input("Enter service time for P#{}: ".format(index + 1))),
            ]
        )
    return process


def get_cycle(process, quantum):
    cycle = math.floor((process / quantum) + (process % quantum))
    return cycle


def get_queue(process, cycle, quantum, size):
    queue = []
    for index in range(0, cycle):
        for element in range(0, len(process)):
            if not queue or (
                queue
                and queue.__len__() < size
                and process[element][0] > queue[element - 1][1]
            ):
                starting_time = process[element][0]
            elif (
                queue
                and queue.__len__() < size
                and process[element][0] <= queue[element - 1][1]
            ):
                starting_time = queue[element - 1][1]
            elif queue and queue.__len__() >= size and process[element][1] != 0:
                starting_time = (
                    queue[-1][1] if index == 1 else queue[queue.__len__() - 1][1]
                )
            else:
                continue
            result = get_finished_time(
                burst_time=process[element][1],
                quantum=quantum,
                starting_time=starting_time,
            )
            process[element][1], finished_time = result[0], result[1]
            queue.append([starting_time, finished_time])
    return process, queue


def get_finished_time(burst_time, quantum, starting_time):
    finished_time = 0
    if burst_time >= quantum:
        finished_time = starting_time + quantum
        burst_time -= quantum
    elif burst_time < quantum and burst_time != 0:
        finished_time = starting_time + burst_time
        burst_time -= burst_time
    return burst_time, finished_time


if __name__ == "__main__":
    main()

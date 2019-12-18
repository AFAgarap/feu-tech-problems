#!/usr/bin/env python3

# Author : A.F. Agarap
# Shortest Job First algorithm

jobs = []

size = int(input("How many processes will you enter? "))

for index in range(0, size):
    jobs.append(
        [
            (int(input("Enter arrival time for job #{}: ".format(index + 1)))),
            (int(input("Enter service time for job #{}: ".format(index + 1)))),
        ]
    )

jobs.sort(key=lambda x: x[1])

for index in range(0, len(jobs)):
    if index == 0:
        jobs[index].append(0)
    else:
        jobs[index].append(
            jobs[index - 1][3]
            if (jobs[index - 1][3] > jobs[index][0])
            else jobs[index][0]
        )
    jobs[index].append(jobs[index][2] + jobs[index][1])

for index in range(0, len(jobs)):
    if index == 0:
        jobs[index].append(0)
    else:
        jobs[index].append(jobs[index][2] - jobs[index][0])

for index in range(0, len(jobs)):
    jobs[index].append(jobs[index][3] - jobs[index][0])

print("\nGantt chart:\n")
for index in range(0, len(jobs)):
    if jobs[index][2] == jobs[index - 1][3]:
        for index2 in range(0, jobs[index][3] - jobs[index - 1][3]):
            print(" - ", end="")
        print(jobs[index][3], " ", end="")
    elif jobs[index][2] != jobs[index - 1][3] or i == 0:
        print(jobs[index][2], end="")
        for index2 in range(0, jobs[index][3] - jobs[index][2]):
            print(" - ", end="")
        print(jobs[index][3], " ", end="")

print("\n\nAT\tBT\tST\tFT\tWT\tTAT")
for index in range(0, len(jobs)):
    print(
        "{}\t{}\t{}\t{}\t{}\t{}".format(
            jobs[index][0],
            jobs[index][1],
            jobs[index][2],
            jobs[index][3],
            jobs[index][4],
            jobs[index][5],
        )
    )

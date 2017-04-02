#!/usr/bin/env python3

import sys

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

def main():
    c = Coordinate(10, 34)
    z = Coordinate(0, 0)
    print(c.distance(z))
    print(c)

if __name__ == '__main__':
    status = main()
    sys.exit(status)

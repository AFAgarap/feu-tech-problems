#!/usr/bin/python3.6

# Copyright 2017 Abien Fred Agarap
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Quadratic Spline Interpolation"""

__version__ = "0.1.0"
__author__ = "Abien Fred Agarap"


def main():

    x = [1, 2, 3, 4, 5]
    y = [3, 6, 9, 12, 15]
    n = 4

    # uncomment for user input
    # x = []; y = []
    # n = int(input('Enter n: '))
    # for index in range(n):
    # 	x.append(int(input('Enter x_{}: '.format(index))))
    # 	y.append(int(input('Enter y_{}: '.format(index))))
    c = list(y)
    a = []
    b = []
    for index in range((n - 1), -1, -1):
        a.append(c[index] - c[index - 1])
    for index in range((n - 1), -1, -1):
        b.append(2 * c[index - 1] - 2 * c[index])
    a = a[::-1]
    b = b[::-1]
    b[-1] = 0
    print(a)
    print(b)
    for index in range(n):
        print(
            "S_{}(x) = {} + {}x + {}x^2 for x ∈ [{}, {}]".format(
                index, y[index], b[index], a[index], x[index], x[index + 1]
            )
        )


if __name__ == "__main__":
    main()

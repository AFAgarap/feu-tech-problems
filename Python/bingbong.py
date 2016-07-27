#!/usr/bin/env python
# Prints "bing" if number is divisible by 3
# Prints "bong" if number is divisible by 5
# Prints "bingbong" if number is divisible by 15
print(list(map(lambda x: "bing" if (x % 3 == 0) else ("bong" if (x % 5 == 0) else ("bingbong" if (x % 15 == 0) else x)), list(range(1, 10)))))

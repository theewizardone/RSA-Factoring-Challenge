#!/usr/bin/python3

import sys
import math

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    exit(1)

file_path = sys.argv[1]

with open(file_path, "r") as file:
    num = int(file.readline().rstrip('\n'))
    i = 2
    num_sroot = int(math.sqrt(num))

    while i <= int(math.sqrt(num)):
        if num % i == 0:
            print("{}={}*{}".format(num, int(num / i), i))
            break
        i += 1

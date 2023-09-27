#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    exit(1)

file_path = sys.argv[1]

with open(file_path, "r") as file:
    for line in file:
        num = int(line.rstrip('\n'))

        for i in range(2, num):
            if num % i == 0:
                print("{}={}*{}".format(num, int(num / i), i))
                break

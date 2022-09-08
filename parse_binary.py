#!/usr/bin/python3

# ./parse_binary.py finput.txt [output file name]

import sys


def parse():
    with open(sys.argv[1], "r+") as finput, open(sys.argv[2] if len(sys.argv) >= 3 else sys.argv[1] + ".out", "w+") as foutput:
        line = finput.read()
        txt = line.strip()
        nums = txt.split(' ')
        out = ""
        for num in nums:
            out += num[6:] + " " + num[4:6] + " " + num[2:4] + " " + num[0:2] + " "
        foutput.write(out)
        print(out)


if __name__ == '__main__':
    parse()

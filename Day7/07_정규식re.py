# re = 정규식
import re

with open('files/uscons.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if re.search('^[0-9]+', line):
            print(line)
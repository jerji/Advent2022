#!/usr/bin/python3

score = 0

with open('input1.txt') as f:
    content = f.readlines()
    for index, line in enumerate(content):
        if index%3 != 0:
            continue
        first = line.strip()
        second = content[index + 1].strip()
        third = content[index + 2].strip()
        common = ord(list(set(first).intersection(second, third))[0])
        if common > 96:
            common -= 96
        else:
            common -= 38
        score += common
        print(common , list(set(first).intersection(second,third))[0])
print(score)

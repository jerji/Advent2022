#!/usr/bin/python3

score = 0

with open('input1.txt') as f:
    for line in f:
        first_half = line[:int(len(line.strip())/2)] 
        second_half = line[int(len(line.strip())/2):].strip()
        common = ord(list(set(first_half).intersection(second_half))[0])
        if common > 96:
            common -= 96
        else:
            common -= 38
        score += common
        print(common , list(set(first_half).intersection(second_half))[0])
print(score)

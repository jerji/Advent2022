#!/usr/bin/python3

total = 0

with open('input.txt') as f:
    for line in f:
        ranges = line.strip().split(',')
        range1ends = ranges[0].split('-')
        range2ends = ranges[1].split('-')
        range1 = {*range(int(range1ends[0]),int(range1ends[1])+1)}
        range2 = {*range(int(range2ends[0]),int(range2ends[1])+1)}
        intersec = range1.intersection(range2)
        if intersec == range1 or intersec == range2:
            print(intersec,range1,range2)
            total +=1

print(total)

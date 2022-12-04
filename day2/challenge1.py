#!/usr/bin/python3

#Shapes:
rock = 1
paper = 2
scissors = 3

#Conditions
lost = 0
draw = 3
win = 6

#Opponent sets
#A = rock
#B = paper
#C = scissors

#My sets
#X = rock
#Y = paper
#Z = scissors

score = 0

def calculate_score(my_move, your_move):
    round_score = 0
    if my_move == 'X':
        round_score = 1
        if your_move == 'A':
            round_score += 3
        if your_move == 'C':
            round_score += 6
    if my_move == 'Y':
        round_score = 2
        if your_move == 'A':
            round_score += 6
        if your_move == 'B':
            round_score += 3
    if my_move == 'Z':
        round_score = 3
        if your_move == 'B':
            round_score += 6
        if your_move == 'C':
            round_score += 3
    return round_score

with open('input1.txt') as f:
    for line in f:
        items = line.strip().split()
        round_score = calculate_score(items[1].strip(),items[0].strip())
        score += round_score
        print('Score for {line} is {score} and total score is {total}'.format(line=line.strip(),score=round_score,total=score)) 

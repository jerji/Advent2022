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
#X = lose
#Y = draw
#Z = win

score = 0

def calculate_score(result, your_move):
    round_score = 0
    if result == 'X':
        if your_move == 'A':
            #need to play scisors
            round_score = 3
        if your_move == 'B':
            #need to play rock
            round_score = 1
        if your_move == 'C':
            #need to play paper
            round_score = 2
    if result == 'Y':
        if your_move == 'A':
            #need to play rock
            round_score = 4
        if your_move == 'B':
            #need to play paper
            round_score = 5
        if your_move == 'C':
            #need to play scisors
            round_score = 6
    if result == 'Z':
        if your_move == 'A':
            #need to play paper
            round_score = 8
        if your_move == 'B':
            #need to play scisors
            round_score = 9
        if your_move == 'C':
            #need to play rock
            round_score = 7

    return round_score

with open('input1.txt') as f:
    for line in f:
        items = line.strip().split()
        round_score = calculate_score(items[1].strip(),items[0].strip())
        score += round_score
        print('Score for {line} is {score} and total score is {total}'.format(line=line.strip(),score=round_score,total=score)) 

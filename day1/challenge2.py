#!/usr/bin/python3

elves_array = []
max_elf = (0,0) #elf, amount

with open('input1.txt') as f:
    current_calories = 0
    index = 0
    for line in f:
        if line.strip() == '':
            elves_array.append(current_calories)
            if current_calories > max_elf[1]:
                max_elf = (index,current_calories)
            print(index,current_calories)
            current_calories = 0
            index += 1
        else:
            current_calories += int(line.strip())
elves_array.sort(reverse=True)
print(elves_array[0] + elves_array[1] + elves_array[2])

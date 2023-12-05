total_points = 0

def play(card):
    divider = card.index("|")
    winning_numbers = card[2:divider]
    card_numbers = card[divider+1:]
    matches = -1
    for w in winning_numbers:
        if w in card_numbers:
            matches += 1
    if matches == -1:
        return 0
    else:
        return pow(2,matches)

def clean_list(list):
    for i,v in enumerate(list):
        if v == '': list.pop(i)
    return list

with open('inputs/input04.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]

for line in input_list:
    total_points += play(clean_list(line))

print(total_points)

total_scratchcards = 0
card_winnings = []
matches = []
copies = []

def play(card):
    #print(card)
    divider = card.index("|")
    winning_numbers = card[2:divider]
    #print(winning_numbers)
    card_numbers = card[divider+1:]
    #print(card_numbers)
    matches = -1
    for w in winning_numbers:
        if w in card_numbers:
            matches += 1
    if matches == -1:
        return 0
    else:
        return matches+1

def clean_list(list):
    for i,v in enumerate(list):
        if v == '': list.pop(i)
    return list

with open('inputs/input04.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]

for i, line in enumerate(input_list):
    matches.append(play(clean_list(line)))
    copies.append(0)

for cn, m in enumerate(matches):
    total_scratchcards += (copies[cn]+1)
    if m > 0 or cn < len(copies):
        end = cn+m+1
        if end > len(copies): end = len(copies)
        for n in range(cn+1,end):
            copies[n] += copies[cn]+1
print(total_scratchcards)

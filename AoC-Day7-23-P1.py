ordered = []
high_card = []
one_pair = []
two_pair = []
three_kind = []
full_house = []
four_kind = []
five_kind = []
cards = "23456789TJQKA"
conversion = {
    "2":"10",
    "3":"11",
    "4":"12",
    "5":"13",
    "6":"14",
    "7":"15",
    "8":"16",
    "9":"17",
    "T":"18",
    "J":"19",
    "Q":"20",
    "K":"21",
    "A":"22"
}

def convert(s):
    converted = ""
    for c in s:
        converted += conversion[c]
    return int(converted)

def numeric_value(n):
    return n[2]

def define_hands():
    for h in input_list:
        counts = []
        counted = 0
        h.append(convert(h[0]))
        for c in cards:
            found = h[0].count(c)
            if found > 0:
                counts.append(found)
                counted += found
            if counted == 5:
                if counts.count(1) == 5:
                    high_card.append(h)
                elif counts.count(2) == 1 and counts.count(1) == 3:
                    one_pair.append(h)
                elif counts.count(2) == 2 and counts.count(1) == 1:
                    two_pair.append(h)
                elif counts.count(3) == 1 and counts.count(1) == 2:
                    three_kind.append(h)
                elif counts.count(2) == 1 and counts.count(3) == 1:
                    full_house.append(h)
                elif counts.count(4) == 1 and counts.count(1) == 1:
                    four_kind.append(h)
                elif counts.count(5) == 1:
                    five_kind.append(h)
                else:
                    print("Uh oh")
                break

def order():
    ordered = []
    if len(high_card) > 0: 
        high_card.sort(key=numeric_value)
        ordered += high_card
    if len(one_pair) > 0: 
        one_pair.sort(key=numeric_value)
        ordered += one_pair
    if len(two_pair) > 0: 
        two_pair.sort(key=numeric_value)
        ordered += two_pair
    if len(three_kind) > 0: 
        three_kind.sort(key=numeric_value)
        ordered += three_kind
    if len(full_house) > 0: 
        full_house.sort(key=numeric_value)
        ordered += full_house
    if len(four_kind) > 0: 
        four_kind.sort(key=numeric_value)
        ordered += four_kind
    if len(five_kind) > 0:
        five_kind.sort(key=numeric_value) 
        ordered += five_kind
    return ordered   

with open('inputs/input07.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]

define_hands()
ordered = order()

total = 0
for i,o in enumerate(ordered):
    total += int(o[1]) * (i+1)
print(total)

"""print("high", high_card)
print("one", one_pair)
print("two", two_pair)
print("three", three_kind)
print("full", full_house)
print("four", four_kind)
print("five", five_kind)"""
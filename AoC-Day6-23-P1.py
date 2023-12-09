time = []
distance = []
ways_to_win = []
margin = 1

def clean_list(list):
    clean = []
    for v in list:
        if v != '': clean.append(v)
    return clean[1:]

def calculate(i):
    wins = 0
    for h in range(int(time[i])):
        time_remaining = int(time[i])-h
        speed = h
        d = time_remaining*speed
        if d > int(distance[i]):
            wins +=1
    return wins

with open('inputs/input06.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]
time = clean_list(input_list[0])
distance = clean_list(input_list[1])

for i in range(len(time)):
    ways_to_win.append(calculate(i))
for w in ways_to_win:
    margin = margin * w

print(margin)
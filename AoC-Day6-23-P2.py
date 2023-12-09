time = []
distance = []
ways_to_win = []
margin = 1
true_time = ''
true_distance = ''

def clean_list(list):
    clean = []
    for v in list:
        if v != '': clean.append(v)
    return clean[1:]

def calculate():
    wins = 0
    for h in range(int(true_time)):
        time_remaining = int(true_time)-h
        speed = h
        d = time_remaining*speed
        if d > int(true_distance):
            wins +=1
    return wins

with open('inputs/input06.txt') as i: input = i.read().splitlines()
input_list = [line.strip().split(" ") for line in input]
time = clean_list(input_list[0])
distance = clean_list(input_list[1])
for t in time:
    true_time += t
for d in distance:
    true_distance += d
margin = calculate()

print(margin)
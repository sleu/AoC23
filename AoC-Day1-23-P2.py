sum = 0
word_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open('inputs/input01.txt') as i:
    read_list = i.read().splitlines()
for l in read_list:
    for word, num in {"one": "o1ne", "two": "t2wo", "three": "th3ree", "four": "fo4ur", "five": "fi5ve", "six": "si6x", "seven": "se7ven", "eight": "ei8ght", "nine": "ni9ne"}.items():
        l = l.replace(word, num)
    numbers = [int(i) for i in l.replace(word, num) if i.isdigit()]
    value = str(numbers[0]) + str(numbers[-1])
    sum += int(value)
    print(sum)
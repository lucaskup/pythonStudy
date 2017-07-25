import string, random

vowels = 'aeiouy'
consonants = 'qwrtpsdfghjklzxcvbnm'
letters = vowels + consonants

options = ['','','']
for i in range(3):
    options[i] = input("Please, enter 'v' for vowel, 'c' for consonants or 'l' for any letter: ")

def generate():
    name = ['','','']
    for i in range(3):
        if options[i] == 'v':
            name[i] = random.choice(vowels)
        elif options[i] == 'c':
            name[i] = random.choice(consonants)
        elif options[i] == 'l':
            name[i] = random.choice(letters)
        else:
            name[i] = options[i]
    return name[0]+name[1]+name[2]

for i in range(20):
    print(generate())

# Transfer time: 0.25
# Consecutive button: 0.25

numbers_to_letters = {
    '1': ['voicemail'],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '*': '+',
    '0': '_',
    '#': 'home'
}

one_to_one = {
    'home': ('#', 0.0),
    '+': ('*', 0.0),
    '_': ('0', 0.0),
    'voicemail': ('1', 0.0),
    'a': ('2', 0.0),
    'b': ('2', 0.25),
    'c': ('2', 0.5),
    'd': ('3', 0.0),
    'e': ('3', 0.25),
    'f': ('3', 0.5),
    'g': ('4', 0.0),
    'h': ('4', 0.25),
    'i': ('4', 0.5),
    'j': ('5', 0.0),
    'k': ('5', 0.25),
    'l': ('5', 0.5),
    'm': ('6', 0.0),
    'n': ('6', 0.25),
    'o': ('6', 0.5),
    'p': ('7', 0.0),
    'q': ('7', 0.25),
    'r': ('7', 0.5),
    's': ('7', 0.75),
    't': ('8', 0.0),
    'u': ('8', 0.25),
    'v': ('8', 0.5),
    'w': ('9', 0.0),
    'x': ('9', 0.25),
    'y': ('9', 0.5),
    'z': ('9', 0.75)
}

"""
# add time between pressing different buttons
def diff_key_time(inp):
    t = 0
    # current index of number in st
    curr_key = one_to_one[inp[0]][0]
    # compare every function
    for letter in inp[1:]:
        # check if each letter is stored in corresponding buttons
        new_key = one_to_one[letter]
        if new_key[0] != curr_key:
            curr_key = new_key[0]
            t += 0.25
    return t


# add 2s for every capital letter
def add_cap_time(inp):
    return sum([2 for letter in inp if letter.isupper()])

def same_key_pause(inp):
    t = 0
    # current index of number in st
    curr_key = one_to_one[inp[0]][0]
    # compare every function
    for letter in inp[1:]:
        # check if each letter is stored in corresponding buttons
        new_key = one_to_one[letter]
        if new_key[0] == curr_key:
            t += 0.5
        else:
            curr_key = new_key[0]
    return t
"""
# add letters corresponding to


# print(same_key_pause("aaicbbbbbb"))

# calculate total time for input
def calculate_time(inp):
    
    t = add_cap_time(inp)
    inp = inp.lower()

    for letter in inp:
        t += one_to_one[letter][1]

    t += (diff_key_time(inp) + same_key_pause(inp))
    
    return t

# get minimum time
def calculate_min_string_time(strings):

    min_time = 10**9
    min_strings = []

    for s in strings:
        s = s[:-1]
        t = addTime(s) 

        if t < min_time:
            min_time = t
            min_strings = [s]

        elif t == min_time:
            min_strings.append(s)

    return min_strings, min_time

def addTime(string):
    previousKey = string[0].lower()
    t = 0 

    for index, char in enumerate(string): 
        if char.isupper():
            t += 2 
        
        char = char.lower()

        if one_to_one[char][0] != one_to_one[previousKey][0]: 
            t += 0.25
        if one_to_one[char][0] == one_to_one[previousKey][0] and index != 0: 
            t += 0.5 

        t += one_to_one[char][1]

        previousKey = char 
    
    return t

if __name__ == "__main__":
    for i in range(1, 5):
        with open(f"Test{i}.txt", "r", encoding='utf-8') as file:
            print(calculate_min_string_time(file))
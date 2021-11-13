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

# PART 1 -----------------------
def calculate_total_time(string):
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

# get the string that takes the least time to print
def get_min_string_time(strings):

    min_time = 10**9
    min_strings = []

    for s in strings:
        s = s[:-1]
        t = calculate_total_time(s)

        if t < min_time:
            min_time = t
            min_strings = [s]

        elif t == min_time:
            min_strings.append(s)

    return min_strings, min_time
# END PART 1 ----------------------

# BEGIN PART 2---------------------

if __name__ == "__main__":
    for i in range(1, 5):
        with open(f"Test{i}.txt", "r", encoding='utf-8') as file:
            print(get_min_string_time(file))

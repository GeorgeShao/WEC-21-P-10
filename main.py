# Transfer time: 0.25
# Consecutive button: 0.25

test_text = "Lorem ipsum dolor sit amet. Id odio animi 33 unde nobis ex nisi itaque. Aut repellat quod sed porro maxime qui fuga placeat est autem reiciendis in odit odit aut voluptatem consectetur. In galisum tempore aut libero veritatis et quam sunt qui cumque autem. Rem error rerum vel fugit harum ad consectetur quidem eos atque maiores ut mollitia ipsam. Et quasi repellat eum voluptatem corrupti nam quasi quod ut alias blanditiis. A sequi aperiam sit culpa nisi id libero explicabo sed libero dolore et explicabo excepturi. Eos autem quia ut consectetur excepturi in minima voluptas est pariatur facilis. Non obcaecati mollitia quo labore maxime quo voluptate dolorum ut quae sint cum omnis perspiciatis aut molestiae dolores. Est voluptatem perferendis vel molestias accusamus ex numquam modi in adipisci odit. Ab debitis cumque eos reprehenderit enim est iusto obcaecati et perspiciatis quam id dolores iure ut quia ipsa."

numbers_to_letters = {
    '1': ["voicemail"],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '*': ['*'],
    '0': ['_'],
    '#': ["#"]
}

one_to_one = {
    "#": ['#', 0.0],
    '*': ['*', 0.0],
    "voicemail": ['1', 0.0],
    '_': ['0', 0.0],
    'a': ['2', 0.0],
    'b': ['2', 0.25],
    'c': ['2', 0.5],
    'd': ['3', 0.0],
    'e': ['3', 0.25],
    'f': ['3', 0.5],
    'g': ['4', 0.0],
    'h': ['4', 0.25],
    'i': ['4', 0.5],
    'j': ['5', 0.0],
    'k': ['5', 0.25],
    'l': ['5', 0.5],
    'm': ['6', 0.0],
    'n': ['6', 0.25],
    'o': ['6', 0.5],
    'p': ['7', 0.0],
    'q': ['7', 0.25],
    'r': ['7', 0.5],
    's': ['7', 0.75],
    't': ['8', 0.0],
    'u': ['8', 0.25],
    'v': ['8', 0.5],
    'w': ['9', 0.0],
    'x': ['9', 0.25],
    'y': ['9', 0.5],
    'z': ['9', 0.75]
}

# BEGIN PART 1 --------------------
# calculates the total time it takes to type a string
def calculate_total_time(string):
    previousKey = string[0].lower()
    time = 0

    for index, char in enumerate(string):
        # add the time from holding a key for an uppercase letter
        if char.isupper():
            time += 2

        # set all characters to lowercase for easier handling
        char = char.lower()

        # add the time from switching between different keys
        if one_to_one[char][0] != one_to_one[previousKey][0]:
            time += 0.25
        
        # add the time from typing consecutive letters on the same key
        if one_to_one[char][0] == one_to_one[previousKey][0] and index != 0:
            time += 0.5

        # add the time from typing each key
        time += one_to_one[char][1]

        # set the previous key to the current key
        previousKey = char

    return time

# gets the string that takes the least time to type
def get_min_string_time(strings):

    min_time = float('inf')
    min_strings = []

    # iterates through the strings and calculates the time it takes to type each string 
    for s in strings:
        s = s.strip()
        t = calculate_total_time(s)

        # If the time taken is smaller than minimum, update the minimum
        if t < min_time:
            min_time = t
            min_strings = [s]

        # If time is equal to the minimum append string 
        elif t == min_time:
            min_strings.append(s)

    return min_strings, min_time
# END PART 1 --------------------

# BEGIN PART 2 --------------------
# changes the dictionary to remap the broken character
def changeDict(broken):
    # first, make a list of all the broken letter
    lBroke = numbers_to_letters[broken]
    lReMap = ["#", '*', "voicemail", '_']

    for i in range(len(lBroke)):
        one_to_one[lBroke[i]] = one_to_one[lReMap[i]]
        one_to_one[lReMap[i]] = [one_to_one[lReMap[i]][0], 0.25]
# END PART 2 --------------------

if __name__ == "__main__":
    print("--Part 1--")
    for i in range(1, 5):
        with open(f"Test{i}.txt", "r", encoding='utf-8') as file:
            print(get_min_string_time(file))
    print("--Part 2--")
    with open("Part2.txt", "r") as file:
        for line in file:
            broken_key = line.strip()
            break
        changeDict(broken_key)
        print("aaa", calculate_total_time("abcabcabc"))
        print(get_min_string_time(file))
    
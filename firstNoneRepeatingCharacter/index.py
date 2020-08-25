def firstNotRepeatingCharacter(s):

    map = {}
    for i,letter in enumerate(s):
        if letter in map:
            map[letter] = False
        else:
            map[letter] = i

    lowest = None
    lowest_letter = "_"
    for letter in map:
        if map[letter] is not False and (lowest is None or map[letter] < lowest):
            lowest = map[letter]
            lowest_letter = letter

    return lowest_letter

print(firstNotRepeatingCharacter("z"))
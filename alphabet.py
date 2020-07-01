from collections import deque


def reverseString(str):
    reversed = deque([])
    letter_list = list(str)
    for letter in letter_list:
        reversed.appendleft(letter)
    reversed_string = "".join(reversed)
    return reversed_string


print(reverseString("abcdef"))


def CanYouSpell(letter_list, name):
    name = name.lower()
    for character in name:
        if character in letter_list:
            letter_list.remove(character)
        else:
            return "NO"
    return "YES"


print(CanYouSpell(["y", "n", "p", "l", "n"], "Lynn"))
print(CanYouSpell(["y", "n", "p", "l"], "lynn"))



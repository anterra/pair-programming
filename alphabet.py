# Given a string, write a function to reverse it. Do this using a loop, if possible.

from collections import deque


def reverseString(str):
    reversed = deque([])
    letter_list = list(str)
    for letter in letter_list:
        reversed.appendleft(letter)
    reversed_string = "".join(reversed)
    return reversed_string


print(reverseString("abcdef"))

# Sal's classroom has a bag of alphabet magnets. She wants to know if she can spell her friend's name
# using the letters in the bag. Write a function that will take a list of letters and a name and
# print out yes if the name can be spelled and no otherwise.


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

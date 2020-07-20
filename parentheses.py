""" The parentheses have to be "balanced" to be valid. For example, ()(()) is balanced, but ()()) is not balanced.
Also, )((()) is not balanced. (Think mathematics.)
Write a function that takes a string and returns True if the string's parentheses are balanced, False if they are not."""


def check_balance(my_string):
    open_pairs = 0
    for char in my_string:
        if char == "(":
            open_pairs += 1
        if char == ")":
            if open_pairs > 0:
                open_pairs -= 1
            else:
                return False
    if open_pairs == 0:
        return True
    else:
        return False


print(check_balance("(()()))(())"))

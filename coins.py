import math

# Given enough pennies (1 cent), nickels (5 cents), dimes (10 cents) and quarters (25 cents),
# how many ways can you make change?


# first version, just nickels and pennies:
def ways(cents):
    counter = 2  # assumes cases of all pennies, and max nickels
    max_nickels = math.floor(cents/5)

    for i in range(1, max_nickels):
        num_nickels_pennies = cents % (i*5)
        counter += 1
    return counter


# scaled version:
def ways2(cents):
    max_quarters = math.floor(cents / 25)
    max_dimes = math.floor(cents / 10)
    max_nickels = max_dimes*2

    counter = 0
    for x in range(max_quarters+1):
        for i in range(max_dimes+1):
            for j in range(max_nickels+1):
                pennies = cents - (25*x) - (10*i) - (5*j)
                if pennies >= 0:
                    print(x, i, j, pennies)
                    counter += 1
                else:
                    pass

    return counter


print("counter: ", ways2(100), "ways")

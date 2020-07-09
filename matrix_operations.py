# A. [4]
# B. no solution
# C. [-2, 3] [1, 1.5] [2, 1] [4, 0] [0, 2]... infinite solutions, its describing a line
# D. [-2, 3]
# E. no solution
# F. [0, 2] [2, 0] [1, 1]
# G. [8, 6] 1 solution only
# H. [4, 4, -2] infinite solutions?
# I. [8, -2] 1 solution only


# The data for this problem are the numbers 2, 7, 1, 5, and 10.
#
# We want to know which of the numbers from 0 to 10 (by tenths) gives the smallest result when we do the following:
#
# For each of the numbers in the data, subtract the candidate number and then square the result,
# then add up these numbers.


tenths = [x/10 for x in range(1, 100)]
my_list = [2, 7, 1, 5, 10]


def check_num(num_list, tenth_list):
    results = {}
    for num in tenth_list:
        each_list = []
        for num2 in num_list:
            operation = (num2 - num)**2
            each_list.append(operation)
            result = sum(each_list)
            results[num] = result
    print(results)
    return min(results, key=results.get)


print(check_num(my_list, tenths))

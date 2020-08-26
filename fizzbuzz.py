# FizzBuzz

for n in range(1, 101):
    output = ""
    if not n % 3:
        output += "Fizz"
    if not n % 5:
        output += "Buzz"
    if output == "":
        output = str(n)
    print(output)


# def fizzbuzz(args):
#     # for n in range(1, 101)
#     for n in range(1, 101):
#         output = ""
#         for i in range(len(args)):
#             if not n % args[i][0]:
#                 output += args[i][1]
#             if output == "":
#                 output = str(n)
#         print(output)


# print(fizzbuzz([(3, "fizz"), (5, "buzz"), (10, "jazz")]))

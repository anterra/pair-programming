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

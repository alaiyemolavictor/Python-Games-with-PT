number = int(input("Enter a number = "))

print("The numbers from", number, "down to zero are:")

number -= 1
while number >= 0:
    print(number)
    number -= 1

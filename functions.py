#Function for Addition
# def add_nums ():
#     fnum = int(input("Enter first number:"))
#     snum = int(input("Enter second number:"))
#     sum = fnum + snum
#     print("The sum of ", fnum, "and", snum, "is", sum)

#add_nums()

#Function for Subtraction
# def sub_nums ():
#     fnum = int(input("Enter first number:"))
#     snum = int(input("Enter second number:")) 
#     sub = fnum - snum
#     print("The sub of ", fnum, "and", snum, "is", sub)   

#sub_nums()

#Function for Multiplication
# def multi_nums ():
#     fnum = int(input("Enter first number:"))
#     snum = int(input("Enter second number:"))
#     Multi = fnum * snum
#     print("The Multi of", fnum, "and", snum, "is", Multi)

#multi_nums()

#Function for Division
# def div_nums():
#     fnum = int(input("Enter first number:"))
#     snum = int(input("Enter second number:"))
#     Div = fnum / snum
#     print("The Div of ", fnum, "and", snum, "is", Div)

#div_nums()


# def mult_nums(a,b):
#     sum = a * b
#     return sum

# a = 'i'
# b = 6
# c = str(input("Enter a word:"))

#  print(mult_nums(a, b))
#  print(mult_nums(b,c))


# def add_nums (a,b):
#     sum = a + b
#     return sum

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))

# print(add_nums(a,b))


import modules as mod
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

sum = mod.add_nums(a, b)
print("The addition of ", a, "and", b, "is",sum)

sub = mod.sub_nums(a, b)
print("The substraction of ", a,"and", b, "is",sub)

div = mod.div_nums(a, b)
print("The division of ", a,"and" ,b, "is",div)

mult = mod.mult_nums(a, b)
print("The multiplication of ", a,"and", b, "is",mult)
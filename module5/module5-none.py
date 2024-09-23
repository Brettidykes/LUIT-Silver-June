#functions can typically:
#1. Cause some effect
#2. Return a meaningful value

print('hello')

length = len('hello')

number = input('what is the number?')

print_return = print('Hello world')
print(print_return)

x = None

if x:
    print("None is true")
elif x is False:
    print("None is False")
else:
    print("None is not True, or False, None is just None")
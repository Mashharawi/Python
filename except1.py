a = 2
b = 0
try:
    c = a/b
except ZeroDivisionError:
    print("Numbers cannot be divided by zero. Please change the value of b")
except NameError:
    print("The formula seem to be wrong")

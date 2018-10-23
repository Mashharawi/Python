""" This script made by Mohammed Mashharawi 2018
It will convert string ti integer datatype """
strings = ["10", "20", "30"]
integers = []
for i in strings:
    integers.append(int(i))
print("integer   ",integers)

s=["1000","30000","5000","7000"]
intmy = [int(i) for i in s]
print(intmy)

fmy = [float(i) for i in s]
print("float  ",fmy)

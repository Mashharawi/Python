age = float(input("Enter your age: "))
if age < 14 : print ("You're under 14 - too young for a license")
elif age >= 14 and age < 17: print("Subject of your state of residence")
elif age >= 17 and age < 18: print ("Qualifies for a driver's license in US")
else: #we can use here elif also but else more elegenat
    print ("Qualifies for a driver's license in every country")

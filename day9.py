#task1 bus pass eligibility

age = int(input("enter you age : "))

if age < 5:
    print ("free tickect")
elif age >= 60:
    print ("senior citizen discount")
else:
    print ("full fare")

#task2 meal time checker

time = int(input("enter the time(0-23): "))

if time == 8:
    print("it's a breakfast time")
elif time == 13:
    print("it's lunch time")
elif time == 20:
    print("it's dinner time")
else:
    print("it's not a meal time")

#task3   library membership

age = int(input("enter your age: "))

if age < 18:
    print("student membership")
elif age >= 60:
    print("senior citizen membership")
else:
    print("Regular membership")
#task1 multiple of 3

for i in range (1,11):
    print("3 *",i, "=",3*1)

#task2 countdown

for i in range (10,0,-1):
    print(f"countdown: {i}")

print("Happy new year!!")

#task3 Ticket booking simulation

tickets =10

while tickets > 0:
    tickets = tickets-1
    print("tickets remaining:", tickets)

print("house full!")

#task4  

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
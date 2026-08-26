items = ["apple","banana","orange","mango","grapes"]

items.append("watermelon")
print(items)

items.insert(1,"kiwi")
print(items)

items.pop(2)
print(items)

#task2

numbers = [45,12,78,23,9,56]

numbers.sort(reverse=True)
print("desending order : ",numbers)

numbers.reverse()
print("after reverse : ",numbers)

#task 3
marks = [78,45,92,67,55,88,34,76]
print(marks)

marks.append(81)
print(marks)

marks.insert(2,95)
print(marks)

marks.remove(min(marks))
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)

print(min(marks))
print(max(marks))
print(len(marks))
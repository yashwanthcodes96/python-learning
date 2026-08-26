fruits =("apple","banana","orange","mango","grapes")
fruits1 =("watermelon","muskmelon","blueberry")
combined_fruits = fruits+fruits1

print(fruits)
print(fruits[2:4])
print(combined_fruits)


#task2

my_fruits = {"apple","banana","mango"}
friends_fruits = {"apple","orange","grapes"}
union_fruits = my_fruits | friends_fruits
intersection_fruits = my_fruits & friends_fruits
difference_fruits = my_fruits - friends_fruits
my_fruits.add("watermelon")
my_fruits.remove("apple")
my_fruits.discard("kiwi")

print(union_fruits)
print(intersection_fruits)
print(difference_fruits)
print(my_fruits)


#task3

items = ["apple","banana","apple","orange"]
items_tuple = tuple(items)
items_set = set(items)
items_set.add("mango")

print(items_tuple)
print(items_set)

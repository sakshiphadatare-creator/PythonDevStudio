import random
fruits = ["apple", "cherry", "pear", "Kivi", "Pomegranate", "apple"]
print(fruits[0])   #positive indexing starts 0

print(fruits[-1]) #Negative indexing starts from -1

fruits[0] = "Mango"   #modify the list using indexing.
print(fruits)

fruits.append("Apple")  #Add the items at the end of the list.
print(fruits)

fruits.extend(["cherry", "Orange", "Banana"]) #Add the list of items at the end of the list.
print(fruits)

fruits.insert(1,"CHERRY") #Insert the items by indexing through.
print(fruits)

fruits.remove("CHERRY") #Remove the specific items from the list.remember you put a (values) under the parenthesis.
print(fruits)             #Raises ValueError if there is no such items int list.

fruits.pop(1)  #Pop() Remove the specific items from the list but indexing through.(index)
print(fruits)   #raises IndexError if index is outside the range.

fruits.sort()  # sort the list ascending or descending order.
print("Sorted : ",fruits)

fruits.reverse()  #Reverse the list.
print("Reverse :", fruits)

fruits.sort(reverse=True)  #Reverse the list by using sort(),reverse the list.
print("Reverse with sort :", fruits)

fruits.sort(reverse=False)  #Reverse the list by using sort(), as it is list ascending order sort.
print("Reverse with sort :", fruits)

print(fruits.count('apple')) #Count how many times given items is repeated and return count as integer.

print(fruits.index("Banana"))  #Indebtify the position of Given item (index)
list_int = [1,2,3,4]
a=random.choices(list_int,k=2)
print("list : ",a)

fruits.clear()  # remove the all items from the list.
print("Clear : ",fruits)

del fruits[:]
print("Delect : ",fruits)





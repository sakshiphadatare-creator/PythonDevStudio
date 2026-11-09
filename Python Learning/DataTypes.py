print("-------------------- List ---------------------")
'''Definition of list: list is mutable data type, it's elements can be changed or removed.
   Element in the list can be accesses using indexing and also support slicing.
   For example, list could be used to store fruit, such as banana, apple, cherry, mango or items'''

mylist = ["sakshi", 1234, "pranav", "Akash", "Sanka", (2, 3, 1, 5), {"name": "sakshi"},12, 9.09]
print(mylist[:3])   #return 0 to 3 but 3 is not include
print(mylist[::3])
print(mylist[1::3]) # skip the one by another
print(mylist[::-1]) # reverse the list

#change the value
mylist[3] = "Abhi"
print(mylist)

#insert the whole list in the position
add_num = [11, 2, 13, 4, 5, 6]
mylist[4] = add_num
print(mylist)

#Extend the list
mylist.extend(add_num)
print(mylist)

#Append the list means add the element end of the list
mylist.append(1042)
print(mylist)

#Insert the value in to the specific position
mylist.insert(1,5000)
print(mylist)

#Remove the element to the list
mylist.remove("pranav")
print(mylist)

#pop function removes random values. One value at a time.
mylist.pop()
print(mylist)

#Count function, count the values to the list.
mylist.count(1234)
print(mylist)

#index function used to return the index of the specific value.
ind = mylist.index("sakshi")
print(ind)
print(mylist.index(1234))

#sort function is used for sorting the list, like ascending or descending order
add_num.sort()
print(add_num)

#reverse function is used for reversing the list.
add_num.reverse()
print(add_num)
print(mylist.reverse())

#copy function used for copy the given list.
mylist2 = mylist.copy()
print(mylist2)

# Clear the whole list.
mylist.clear()
print(mylist)

#let's create the list of tuples.
position1 = [(2, 4), (4, 6), (6, 8)]
position1[1] = (10, 12)
print(position1)
print(position1[0])


print("-------------------- Tuple ---------------------")
'''definition of tuple: once tuple created, it's elements cannot be changed or removed, making tuples immutable
    Tuple supports slicing or elements accessed using indexes similar to the list.
    tuples are often used to represent fixed collection of items such as coordinates and return values from functions.
    For example, tuple store values like coordinates, 12 comma 6 which remain constant.'''

#let's see how to create tuple
position = (2,5,6)   # starts with 0
print(position)

#slicing
print(position[1])

print("-------------------- Dictionary ---------------------")
''' definition of dictionary: So,Dictionary in Python is a mutable and unordered Collection of items.
    each item of dictionary is a key value pair, where is key is unique within the dictionary.
    So dictionary is often used to store data in a way that allows for quick retrieval based on keys.'''

#let's see how to create dictionary.
weeks = {
    "sun" : "sunday",
    "mon" : "monday",
    "tue" : "tuesday",
    "wed" : "wednesday",
    "thu" : "thursday",
    "fri" : "friday",
    "sat" : "saturday",
}
print(weeks.get("tue","Not valid"))
print(weeks.get("tus","Not valid"))

month = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
    "Num" : 18
}

print(month["Num"])

year = {
    "weeks" : {"sun" : "sunday","mon" : "monday","tue" : "tuesday",
             "wed" : "wednesday","thu" : "thursday","fri" : "friday","sat" : "saturday"},
    "month" : {"Jan" : "January","Feb" : "February",
            "Mar" : "March","Apr" : "April",
            "May" : "May","Jun" : "June",
            "Jul" : "July","Aug" : "August",
            "Sep" : "September","Oct" : "October",
            "Nov" : "November","Dec" : "December",
            "Num" : 18}
}
print(year["weeks"]["sun"])
print(year["month"]["Mar"])
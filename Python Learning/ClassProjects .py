print("-------------------- First Class Level Project ---------------------")

no1 = input("Enter the first number: ")
no2 = input("Enter the second number: ")
result = int(no1) + int(no2)
print(result)

result = float(no1) - float(no2)
print(result)

result = int(no1) * int(no2)
print(result)

result = float(no1) / float(no2)
print(result)

print("-------------------- Second Class Level Project ---------------------")

my_dic = {
    "name" : "Sakshi",
    "age" : 19,
    "class" : "BSc.Data Science",
    "color" : "Blue",
    "place" : "Bangalore",
    "person" : "Prashant",
    "friend" : "Pranav",
    "Subject" : "Mathematics",
    "Job" : "Data Scientist"
}
print(my_dic.get("friend","Not valid"))
print(my_dic.get("Friend","Not valid"))
print(my_dic.get("name"))
print(my_dic["age"])
print(my_dic.get("class"))
print(my_dic.get("Job"))



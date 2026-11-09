from bs4 import BeautifulSoup
#import lxml

with open ("website.html") as file:
    contents = file.read()
    #print(contents)
soup = BeautifulSoup(contents, "html.parser")  # we can also write features:"lxml"
# print(soup.title)  # this statement gives us whole title name with content.
# print(soup.title.name)   #This gives us title name.
# print(soup.title.string)  # this gives us string
# print(soup.a) # it's gives us  first anchor tag
# print(soup.prettify()) # prettify version where everything's  all indented properly and easier to read.
all_anchor_tags = soup.find_all(name="a")  # Name of the tag
print(all_anchor_tags) # this line of code gives us all the anchor tags.
for tag in all_anchor_tags:
    #print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1",id="name")
print(heading)

section_heading = soup.find(name="h3",class_="heading")    #you don't write class because it already reserved. instead of class we use class_
print(section_heading.getText())
print(section_heading.get("class"))

name =  soup.select_one(selector="#name")  # (In id we use # symbol)It will give us first matching items in a list (select will give us all of the matching items in a list)
print(name)

heading = soup.select_one(selector=".heading")  # (In class we use .(Dot symbol))
print(heading)

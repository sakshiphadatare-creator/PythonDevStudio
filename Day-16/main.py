# from turtle import Turtle,Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# # timmy.color("chartreuse2")
# # timmy.shapesize(20)
# timmy.color("coral")
# timmy.forward(100) # positive 100 move forward but -100 move backward
#
# screen_view = Screen()
# print(screen_view.canvheight)  # object.attribute
# screen_view.exitonclick()  # object.method

from prettytable import PrettyTable
# table = PrettyTable()
# # table.add_column("Name",["Sakshi", "Pranav", "Kiran", "Prashant"]),
# # table.add_column("Course",["BSc.Data Science", "BSc.Data Science", "12th Science", "MSc.Com Science"])
# table.add_column("Pokémon name",["Pikachu", "Squirtle", "Charmander"])  #align = "l", "c", "r"
# table.add_column("Type",["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)

student = PrettyTable()
student.add_column("Student ID",[101,102,103,104])
student.add_column("Name",["Sakshi", "Srushti", "Ankita", "Prajakta"])
student.add_column("Age", [18,19,18,20])
student.add_column("Attendance",["A+", "B", "A", "O+"])
student.align = "l"
print(student)
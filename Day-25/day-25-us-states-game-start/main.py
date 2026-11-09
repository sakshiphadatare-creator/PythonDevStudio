import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()   # convert the state column into the list
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",prompt="What's another state's name?").title()

    # If answer_data is one of the states in all states of the 50_states.csv
        # If they got it right:
    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_states]
        # missing_state = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        print(missing_state)
        new_data = pd.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        # Create a turtle to write the name of the state at the state's x and y coordinates
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())

        t.write(answer_state)











# t.write(state_data.state.item())      #Return the first element of the underlying data as a
# #Get x y coordinate on click python turtle.
# def get_mouse_coordinates(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_coordinates)

#
# # screen.exitonclick()
from turtle import Screen, shape, mainloop, Turtle
import pandas as pd

screen = Screen()
screen.title("U.S States Quiz")
screen.addshape("usmap.gif")
shape("usmap.gif")
states_left = True

states = pd.read_csv("50states.csv")
states_list = states.state.to_list()
while states_left:
    states_left = len(states_list)
    answer = screen.textinput(
        title=f"{50-states_left}/50 States Left",
        prompt="Enter the name of a state in the US",
    ).title()
    if answer in states_list:
        state_name = Turtle()
        state_name.hideturtle()
        state_name.penup()
        answer_row = states[states.state == answer]
        x = int(answer_row.x)
        y = int(answer_row.y)
        state_name.goto(x, y)
        state_name.write(f"{answer}", align="center", font=("Courier", 10, "normal"))
        states_list.remove(answer)
    else:
        pass
mainloop()

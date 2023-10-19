from turtle import Screen, shape, mainloop, Turtle
import pandas as pd

screen = Screen()
screen.title("U.S States Quiz")
screen.addshape("usmap.gif")
shape("usmap.gif")

states = pd.read_csv("50states.csv")
states_list = states.state.to_list()
guessed = []
while len(guessed) < 50:
    answer = screen.textinput(
        title=f"{len(guessed)}/50 States Left",
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
        state_name.write(answer, align="center", font=("Courier", 6, "normal"))
        guessed.append(answer)
    elif answer == "Exit":
        unguessed = []
        for state in states_list:
            if state not in guessed:
                unguessed.append(state)
        pd_unguessed = pd.DataFrame(unguessed)
        pd_unguessed.to_csv("./results.csv")
        break

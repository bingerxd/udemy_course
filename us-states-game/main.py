import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

data = pandas.read_csv("50_states.csv")
guessed_states = 0
amount_of_state = 50
game_is_on = True

states = []
for state in data["state"]:
    states.append(state)

while game_is_on:

    text_answare = screen.textinput(title=f"States correct: {guessed_states}/{amount_of_state}", prompt="What's another state's name?").title()

    for state in data["state"]:
        if text_answare == state:
            coor = data[data.state == text_answare]
            turtle.goto(int(coor.x), int(coor.y))
            turtle.write(f"{state}")
            guessed_states += 1
            states.remove(state)

    if text_answare == "Exit":
        game_is_on = False
        with open("states_to_learn.csv", mode="w") as data:
            for st in states:
                data.write(st)
                data.write("\n")

    if guessed_states == 50:
        game_is_on = False

screen.exitonclick()
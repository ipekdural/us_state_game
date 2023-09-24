from turtle import Turtle, Screen
from time import sleep
import pandas


def game():
    screen.clear()
    state_turtle = Turtle()
    state_turtle.shape("blank_states_img.gif")

    guessed_states = []
    data = pandas.read_csv("50_states.csv")
    states_list = data["state"].to_list()
    screen.tracer(0)
    while len(guessed_states) < 50:

        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guessed",
                                        prompt="What is another state's name?").title()
        if answer_state.lower() == "exit":
            missing_states = []
            for state in states_list:
                if state not in guessed_states:
                    missing_states.append(state)
            for missing_state in missing_states:
                missing_state_data = data[data.state == missing_state]
                pen = Turtle()
                pen.hideturtle()
                pen.penup()
                pen.color("red")
                pen.goto(int(missing_state_data.x), int(missing_state_data.y))  # we should convert it to integer
                pen.write(f"{missing_state}", align="center", font=("Courier", 8, "bold"))
            missing_states_df = pandas.DataFrame(missing_states)
            missing_states_df.to_csv("missing_states.csv")
            screen.update()
            pen2 = Turtle()
            pen2.hideturtle()
            pen2.penup()
            pen2.color("#6499E9")
            pen2.goto(250, 270)
            pen2.write(f"Press 'r' to replay!", align="center", font=("Courier", 15, "bold"))
            pen2.color("#D83F31")
            pen2.goto(-250, 270)

            pen2.write(f"Press 'q' to exit!", align="center", font=("Courier", 15, "bold"))
            screen.listen()
            screen.onkey(exit, "q")
            screen.onkey(game, "r")
            break
        if answer_state in states_list:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]  # data is stored as strings
            pen = Turtle()
            pen.hideturtle()
            pen.penup()
            pen.color("green")
            pen.goto(int(state_data.x), int(state_data.y))  # we should convert it to integer
            pen.write(f"{answer_state}", align="center", font=("Courier", 8, "bold"))

        sleep(0.3)


screen = Screen()
screen.addshape("blank_states_img.gif")
screen.title("U.S. State Game")
game()
screen.exitonclick()

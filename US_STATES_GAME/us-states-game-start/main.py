import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


score = 0
game_is_on = True
guesses = 0
guessed_states = []
while game_is_on:
    answer_state = screen.textinput(title=f"{score}/50", prompt="What's another state's name?").title()
    states = pandas.read_csv("50_states.csv")
    states_list = states.state.to_list()
    guessed_states.append(answer_state)
    if answer_state == "Exit":
        missing_states = [state for state in states_list if state not in guessed_states]
        # for state in states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
    if answer_state in states_list:
        score += 1
        guesses += 1
        state_row = states[states.state == answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        new_icon = turtle.Turtle()
        new_icon.hideturtle()
        new_icon.penup()
        new_icon.goto(x_cor, y_cor)
        new_icon.color("black")
        new_icon.write(f"{answer_state}", align="center", font=("Arial", 6, "bold"))

    else:
        guesses += 1

    if score == 50:
        you_win_sign = turtle.Turtle()
        you_win_sign.hideturtle()
        you_win_sign.color("black")
        you_win_sign.write(f"YOU'RE PERFECT!\nYour score was {score}/50", align="center",
                           font=("Arial", 20, "bold"))
        game_is_on = False
    if guesses == 50 and score != 50:
        game_over_sign = turtle.Turtle()
        game_over_sign.hideturtle()
        game_over_sign.color("black")
        game_over_sign.write(f"GAME OVER!\nYour score was {score}/50", align="center", font=("Arial", 20, "bold"))
        game_is_on = False










# keeps screen open
turtle.mainloop()





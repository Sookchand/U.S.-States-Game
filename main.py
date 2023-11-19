import pandas
import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
t = Turtle()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

df = pd.read_csv("50_states.csv")
data_dict = df.to_dict()
all_states = df.state.to_list()

guessed_states = []  # Initialize a list to store guessed states
correct_guesses = 0  # Initialize a counter for correct guesses

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guess the state: {correct_guesses}/{50}",
                                    prompt="What's another states name?").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        tim = Turtle()
        tim.penup()
        tim.hideturtle()
        state_data = df[df.state == answer_state]
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        tim.goto(x_cor, y_cor)
        tim.write(answer_state)
        correct_guesses += 1
        screen.title(f"Guess the state: {correct_guesses}/{50}")

# screen = Screen()
# t = Turtle()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.bgpic(image)

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"Guess the state: {correct_guesses}/{50}",
#                                     prompt="What's another states name?").title()
#     if answer_state == "exit":
#         break
#
#     if answer_state not in guessed_states:  # Check if the state has not been guessed before
#         x_coordinate = df.loc[df["state"] == answer_state, "x"].item()
#         y_coordinate = df.loc[df["state"] == answer_state, "y"].item()
#         t.hideturtle()
#         t.penup()  # Lift the pen to prevent drawing a trail
#         t.goto(x_coordinate, y_coordinate)
#         t.pendown()  # Lower the pen to start drawing again
#         t.write(answer_state, align="center", font=("Arial", 8, "normal"))
#         guessed_states.append(answer_state)  # Add the guessed state to the list
#         correct_guesses += 1  # Increment the correct guesses counter
#
#         # Update the message in the title bar
#         screen.title(f"Guess the state: {correct_guesses}/{50}")
#     else:
#         screen.textinput(title="Already guessed", prompt=f"You've already guessed {answer_state}")
#
#   learn_state = set(all_states) - set(guessed_states)
#   with open("unguess_states.csv", "w", newline="") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     for state in learn_state:
#         csv_writer.writerow([state])
# # Display a final message at the end of the game
# screen.textinput(title="Game Over", prompt=f"You guessed {correct_guesses} out of 50 states correctly!")
#
# screen.mainloop()

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
correct_answers = []

# Use a loop to allow the user to keep guessing
while len(correct_answers) < 50:

    # Ask for an answer
    # Keep track of score
    # Convert answer to title case
    answer_state = screen.textinput(title=f"States guessed: {len(correct_answers)}/50",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missed_states = []
        for state in all_states:
            if state not in correct_answers:
                missed_states.append(state)
        missed_states_df = pd.DataFrame(missed_states)
        missed_states_df.to_csv("missed_states.csv")
        break

    # Check if the guess is among the 50 States
    if answer_state in all_states:
        # Record correct answers in a list
        correct_answers.append(answer_state)
        score = len(correct_answers)
        # Write correct answers to the map
        state_data = data[data.state == answer_state]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(answer_state)

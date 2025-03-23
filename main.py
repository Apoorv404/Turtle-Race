from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtles in all_turtle:
        turtles.forward(randint(0,10))
        if turtles.xcor() > 230:
            is_race_on = False
            winning_color = turtles.pencolor()
            if user_bet == winning_color:
                print(f"You've won! {winning_color} is the winner.")
            else:
                print(f"You've lost! {winning_color} is the winner.")

screen.exitonclick()
import random
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bot = screen.textinput(title="Make your bot", prompt="Which turtle will win the race? Enter a color. ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# posy = -70
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    # posy += 30
    all_turtle.append(new_turtle)

if user_bot:
    is_race_on = True
while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bot == winning_color:
                print(f"You've Win! The {winning_color} is the Winning color.")
            else:
                print(f"You've lose! The {winning_color} is the Winning color.")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()

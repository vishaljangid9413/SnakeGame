from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from snake_Scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# ye ham ek object bana rahe h har ek particular class ke function ke liye
snakes = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snakes.up, key="Up")
screen.onkey(fun=snakes.down, key="Down")
screen.onkey(fun=snakes.left, key="Left")
screen.onkey(fun=snakes.right, key="Right")

game_is_on = True
# this loop is for moving our snake
while game_is_on:
    # ye function screen ko baar baar update karte rahega
    screen.update()
    # ye snake ki speed ko slow karne ke liye
    time.sleep(0.1)
    snakes.move()

    # agar snake aur food ke beech 15 se kam distance ho to
    # detect collision with food
    if snakes.head.distance(food) < 15:
        # food ek nayi jagah pohoch jaye
        food.refresh()
        # snake apne aap ko extend kar le
        snakes.extend()
        # scoreboard increase ho jaye 1 se
        scoreboard.increase_score()

    # detect collision with wall
    # snakes class ke head function ke x coordinates agar given coordinates se kam ya zyada h
    if snakes.head.xcor() > 290 \
            or snakes.head.xcor() < -290 \
            or snakes.head.ycor() > 290 \
            or snakes.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snakes.reset_snake()

    # detect collision with tail
    # ek loop chalaya ki blocks me ek ek block ko check kiya jayega
    # blocks ke andar slice method use karke ham first index se loop chalu karenge
    for block in snakes.blocks[1:]:
        if snakes.head.distance(block) < 10:
            scoreboard.reset_scoreboard()
            snakes.reset_snake()


screen.exitonclick()


























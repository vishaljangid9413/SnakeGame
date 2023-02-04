from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        # yaha ek file kholenge data ke naam se
        with open("snake_data.txt") as data:
            # aur use read karke uska data highscore me daal denge
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    # this function write print score on screen
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.highscore}", align="center", font=("Arial", 15, "normal"))


    # ye score reset karne  me kaam ata h
    def reset_scoreboard(self):
        # agar score ki value highscore se zyada h
        if self.score > self.highscore:
            # to highscore ke andar score ki value save ho jayegi
            self.highscore = self.score
            # aur ek nayi file khole usme ye value save kar di jayegi
            with open("snake_data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        # aur fir se score ki value reset ho jayegi
        self.score = 0
        # aur jaise jaise point padhenge waise waise score fir se badhta jayega update_scoreboard() se
        self.update_scoreboard()

    # this function increase the score
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

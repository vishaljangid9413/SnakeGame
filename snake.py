from turtle import Turtle

the_snake = Turtle()
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTENCE = 20

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]

     # ye ek naya snake banayega
    def create_snake(self):
        # this loop is for creating a snake
        for position in STARTING_POSITION:
            self.add_block(position)

    # ye ek naya block banyega
    def add_block(self, position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    # ye function naye block ko last me laga dega
    def extend(self):
        # add_block ke andar blocks ki last index value pass karwa di
        # aur naye block ko kaha ki last index par apni position lele
        self.add_block(self.blocks[-1].position())

    def move(self):
        # ab hamara snake chalne laga h lekin ab hame ise kahi modna ho
        # to iska jo pehla block h sirf wo mudega aur baaki bache hue blocks sidhe badhte rahenge
        # to is dikkat ko dur karne ke liye hame aise code likhenge jisse ki
        # jo last wala block h wo apne se aage wale ko follow karte hue uski jagah par aajaye
        # aisa karne se saare block apne se aage wale ko follow karenge aur
        # jab ham first wale block ko ghumanaye to saare blocks bhi ghum jayenge

        # niche loop blocks ki length - 1  se 0 tak chalega wo bhi -1 ke gape se
        for block_num in range(len(self.blocks) - 1, 0, -1):
            # jo loop me current block chal raha h uske agle wale block ke coordinates h
            new_x = self.blocks[block_num - 1].xcor()
            new_y = self.blocks[block_num - 1].ycor()
            # aur jo loop me currrent block h wo apne se agle block ke coordinates par chala jayega
            self.blocks[block_num].goto(new_x, new_y)
        self.blocks[0].forward(MOVE_DISTENCE)

    def up(self):
        # ye code ye bol raha ki agar hamne UP key dabayi h to ham DOWN key ka us nahi kar sakte
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        # ye code ye bol raha ki agar hamne LEFT key dabayi h to ham RIGHT key ka us nahi kar sakte
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        # ye code ye bol raha ki agar DOWN UP key dabayi h to ham UP key ka us nahi kar sakte
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # ye code ye bol raha ki agar hamne RIGHT key dabayi h to ham LEFT key ka us nahi kar sakte
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # agar snake kahi takraye to use reset kar denge
    def reset_snake(self):
        # isse snake ek nayi jagah pohoch jayega jo ki screen se bahar kahi hogi
        for blk in self.blocks:
            blk.goto(1000, 1000)
        # aur fir purana sab clear ho jayega
        self.blocks.clear()
        # aur ek naya snake ban jayega
        self.create_snake()
        # snake ka head blocks ka first index ban jayega
        self.head = self.blocks[0]
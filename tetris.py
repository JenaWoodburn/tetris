import turtle
import time
import random

# Create game window
wn = turtle.Screen()
wn.title("TETRIS")
wn.bgcolor(0.4,0.4,0.4) #mid-grey
wn.setup(width=600, height=800)
wn.tracer(0)

delay = 0.05

#define class Shape
class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.colour = random.randint(1,7)

        #large square shape
        self.shape = [[1,1], 
                      [1,1]]
        
        square = [[1,1],
                  [1,1]]
        
        h_line = [[1,1,1,1]]

        v_line = [[1],
                  [1],
                  [1],
                  [1]]
        
        left_l = [[1,0,0,0],
                  [1,1,1,1]]

        right_l = [[0,0,0,1],
                   [1,1,1,1]]

        left_s = [[1,1,0],
                  [0,1,1]]

        right_s = [[0,1,1],
                   [1,1,0]]

        t = [[0,1,0],
             [1,1,1]]
        
        shapes = [square, h_line, v_line, left_l, right_l, left_s, right_s, t]

        self.shape = random.choice(shapes)

        self.height = len(self.shape)
        self.width = len(self.shape[0])

    # move shape left
    def move_left(self, grid):
        #check shape isn't already on left edge
        if self.x > 0:
            #check cell to the left is empty
            if grid[self.y][self.x-1] == 0:
                #clear shape's current cell
                self.erase_shape(grid)
                #clear shape's current cell
                #move left by 1
                self.x -= 1

    # move shape right
    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1

    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]) == 1:
                    grid[self.y + y][self.x + x] = self.colour

    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]) == 1:
                    grid[self.y + y][self.x + x] = 0

    def can_move(self, grid):
        result = True
        for x in range(self.width):
            #check bottom row
            if (self.shape[self.height-1][x] == 1):
                #if cell below a filled-in cell is not empty
                if (grid[self.y + self.height][self.x + x] != 0):
                    #can't move
                    result = False
        return result

 


# Define grid to display shapes on
grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0],
    [3,0,2,6,0,1,0,1,4,5,6,4]
]

len_x = len(grid[0])
len_y = len(grid)

#pen settings, defines grid cells' size
pen = turtle.Turtle()
pen.penup()
pen.speed()
pen.shape("square")
pen.setundobuffer(None)
pen.shapesize(stretch_wid=1.5, stretch_len=1.5) # Default pen size is 20x20, set to 30x30

#how to draw the grid
def draw_grid(pen: turtle.Turtle, grid: list[list[int]]):
    pen.clear()
    # Starting coordinates
    top = 350
    left = -165
    # Shapes will be one of these colours
    colours = ["black", "lightblue", "darkblue", "orange", "yellow", "green", "purple", "red"]

    # Loop through the grid and draw each cell
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 30)
            screen_y = top - (y * 30)
            colour = colours[grid[y][x]]
            pen.color(colour)
            pen.goto(screen_x,screen_y)
            pen.stamp()

def check_grid(grid):
    #check if any row is full
    #start at bottom and work up as rows above full rows need to be copied downwards
    y = 23
    while y > 0:
        is_full = True
        #if any cell contains 0, row is not full, break
        for x in range (0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        # if row is full
        if is_full:
            # for each row above it
            for copy_y in range(y, 0, -1):
                # copy each cell in that row into the row below
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

#create initial shape
shape = Shape()
grid[shape.y][shape.x] = shape.colour

#draw the grid
draw_grid(pen, grid)

# left and right movement
wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_right(grid), "d")

#draw shape; keep shape falling until it's stopped by bottom of screen or another shape; create new shape
while True:
    wn.update()

    #basic falling action of shape
    #if shape has reached the bottom row it stays there, create new shape
    if shape.y + shape.height - 1 == 23:
        shape = Shape()
        check_grid(grid) 
    #check if cells below shape are empty
    elif shape.can_move(grid): 
        #if so, clear existing shape position
        shape.erase_shape(grid)
        #update shape's coords (y+1) 
        shape.y += 1

        #fill it in
        shape.draw_shape(grid)

    else:
        shape = Shape()
        check_grid(grid)
        
    draw_grid(pen, grid)

    time.sleep(delay)
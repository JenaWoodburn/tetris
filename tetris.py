import turtle

# Create game window
wn = turtle.Screen()
wn.title("TETRIS")
wn.bgcolor(0.4,0.4,0.4) #mid-grey
wn.setup(width=600, height=800)
wn.tracer(0)

#define class Shape
class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.colour = 4

    # move shape left
    def move_left(self, grid):
        #check shape isn't already on left edge
        if self.x > 0:
            #check cell to the left is empty
            if grid[self.y][self.x-1] == 0:
                #clear shape's current cell
                grid[self.y][self.x] = 0
                #clear shape's current cell
                #move left by 1
                self.x -= 1

    # move shape right
    def move_right(self, grid):
        #check shape isnt' already on right edge
        if self.x < (len(grid[0]) - 1):
            # check cell to the right is empty
            if grid[self.y][self.x+1] == 0:
                #clear shape's current cell
                grid[self.y][self.x] = 0
                #move right by 1
                self.x += 1


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
    [0,0,0,0,0,0,0,0,0,0,0,0]
]

#pen settings, defines grid cells' size
pen = turtle.Turtle()
pen.penup()
pen.speed()
pen.shape("square")
pen.shapesize(stretch_wid=1.5, stretch_len=1.5) # Default pen size is 20x20, set to 30x30

#how to draw the grid
def draw_grid(pen: turtle.Turtle, grid: list[list[int]]):
    pen.clear()
    # Starting coordinates
    top = 350
    left = -165
    # Shapes will be one of these colours
    colours = ["black", "light blue", "dark blue", "orange", "green", "purple", "red"]

    # Loop through the grid and draw each cell
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 30)
            screen_y = top - (y * 30)
            colour = colours[grid[y][x]]
            pen.color(colour)
            pen.goto(screen_x,screen_y)
            pen.stamp()

#create initial shape
shape = Shape()
grid[shape.y][shape.x] = shape.colour

#draw the grid
draw_grid(pen, grid)

# left and right movement
wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_right(grid), "d")

#keep shapes falling until they are stopped, create new shapes
while True:
    wn.update()

    #basic falling action of shape
    #if shape has reached the bottom row it stays there, create new shape
    if shape.y == 23:
        shape = Shape()
    #check if cell below shape is empty
    elif grid[shape.y + 1][shape.x] == 0:
        #if so, clear existing shape position
        grid[shape.y][shape.x] = 0
        #update shape's coords (y+=1) 
        shape.y += 1
        #fill it in
        grid[shape.y][shape.x] = shape.colour
    else:
        shape = Shape()
        
    draw_grid(pen, grid)
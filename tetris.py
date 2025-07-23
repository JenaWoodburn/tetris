import turtle

# Create game window
wn = turtle.Screen()
wn.title("TETRIS")
wn.bgcolor(0.4,0.4,0.4) #mid-grey
wn.setup(width=600, height=800)
wn.tracer(0)

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

# Draw shapes
pen = turtle.Turtle()
pen.penup()
pen.speed()
pen.shape("square")
pen.shapesize(stretch_wid=1.5, stretch_len=1.5) # Default pen size is 20x20, set to 30x30

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

draw_grid(pen, grid)

while True:
    wn.update()
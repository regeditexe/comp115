import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle named "artist"
artist = turtle.Turtle()
artist.speed("fastest")  # Set the drawing speed

# Customizing the pen
artist.pensize(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw a colorful spiral
for i in range(360):
    artist.color(colors[i % len(colors)])  # Cycle through colors
    artist.forward(i)  # Move forward
    artist.left(59)  # Turn left

# Hide the turtle cursor
artist.hideturtle()

# Save the drawing as an image (optional)
# turtle.getcanvas().postscript(file="spiral.eps")

# Keep the window open until manually closed
turtle.done()

# Import necessary modules
from turtle import Turtle, Screen  # Import Turtle and Screen classes from the turtle module
import random  # Import the random module
import tkinter as tk  # Import the tkinter module as tk for creating GUI dialogs
from tkinter import messagebox, simpledialog  # Import specific functions from tkinter for creating message boxes and dialogs

# Function to display message box
def show_message(message):
    # Create a hidden Tkinter window
    root = tk.Tk()
    root.withdraw()
    # Bring the Tkinter window to the front
    root.attributes("-topmost", True)
    # Ensure that the Tkinter window receives focus
    root.after(0, lambda: root.focus_force())
    # Show an information message box with the specified message
    messagebox.showinfo("Race Result", message)

# Function to display play again message box
def play_again():
    # Show a yes/no message box and return True if "Yes" is clicked, False otherwise
    play = messagebox.askyesno("Play Again", "Do you want to play again?")
    return play

# Function to simulate the race
def race():
    # Loop indefinitely
    while True:
        # Iterate over each turtle in the list
        for turtle in all_turtles:
            # Generate a random distance for the turtle to move forward
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)  # Move the turtle forward by the random distance
            # Check if the turtle has crossed the finish line
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()  # Get the color of the winning turtle
                # Show a message indicating whether the user has won or lost
                if winning_color == user_bet:
                    show_message(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    show_message(f"You've lost! The {winning_color} turtle is the winner!")
                reset_race()  # Reset the race by moving the turtles back to their initial positions
                return  # Exit the race function

# Function to reset the race by moving the turtles back to their initial positions
def reset_race():
    for turtle, y_position in zip(all_turtles, y_positions):
        turtle.goto(x=-230, y=y_position)  # Move each turtle back to its initial position
        turtle.showturtle()  # Make each turtle visible again

# Initialize screen and turtles
screen = Screen()  # Create a screen object
screen.setup(width=500, height=400)  # Set up the screen dimensions
user_bet = simpledialog.askstring(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")  # Prompt the user to enter their bet
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # Define the colors for the turtles
y_positions = [-70, -40, -10, 20, 50, 80]  # Define the initial y positions for the turtles
all_turtles = []  # Create an empty list to store the turtles

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")  # Create a new turtle object
    new_turtle.penup()  # Lift the pen to prevent drawing
    new_turtle.color(colors[turtle_index])  # Set the color of the turtle
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Move the turtle to its initial position
    all_turtles.append(new_turtle)  # Add the turtle to the list of all turtles

# Stylish and colorful finishing line
finish_line = Turtle()  # Create a new turtle for the finishing line
finish_line.penup()  # Lift the pen to prevent drawing
finish_line.goto(230, -150)  # Move the turtle to the starting position of the finishing line
finish_line.color("white", "lightgreen")  # Set the color of the finishing line
finish_line.pendown()  # Lower the pen to start drawing
finish_line.begin_fill()  # Begin filling the shape
finish_line.forward(10)  # Draw the first side of the finishing line
finish_line.left(90)  # Turn the turtle left
finish_line.forward(300)  # Draw the second side of the finishing line
finish_line.left(90)  # Turn the turtle left
finish_line.forward(10)  # Draw the third side of the finishing line
finish_line.left(90)  # Turn the turtle left
finish_line.forward(300)  # Draw the fourth side of the finishing line
finish_line.end_fill()  # End filling the shape

# Start the race
race()

# Check if the user wants to play again
while play_again():
    race()

#Himel Sarder
#Dept. of CSE, BSFMSTU
#Gmail - info.himelcse@gmail.com
#Linedin - https://www.linkedin.com/in/himel-sarder/

screen.exitonclick()  # Keep the window open until the user closes it

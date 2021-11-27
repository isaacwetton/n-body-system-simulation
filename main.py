# Import modules
from Particle import *
import numpy as np

# Define list of commands
COMMANDS = ["help", "exit", "add", "del", "plot"]
# Print welcome message
print("Welcome to this n-body gravity simulation by Isaac Wetton.\n\n"
      "The program initially has the Sun and Earth as the only objects.\n\n"
      "Type 'help' for a list of commands.\n")

# Wait for user input
command = input("")

# Check for valid command
while command not in COMMANDS:
    print("That is not a valid command. Type 'help' for a list of commands.")
    command = input("")

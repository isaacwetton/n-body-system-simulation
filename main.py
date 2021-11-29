# Import modules
from Particle import *
import numpy as np
import commandFuncs as cmd

# Define list of commands
COMMANDS = ["help", "add", "del", "plot"]

# Initialise system
sun = Particle(name="Sun")
earth = Particle(name="Earth")

# Print welcome message
print("Welcome to this n-body gravity simulation by Isaac Wetton.\n\n"
      "The program initially has the Sun and Earth as the only objects.\n\n"
      "Type 'help' for a list of commands.\n")

# Wait for user input
command = input("")

# Check for valid command
while command != "exit":
    while command not in COMMANDS:
        if command == "exit":
            break
        print("That is not a valid command. Type 'help' for a list of commands.")
        command = input("")
    if command == "exit":
        break
    cmd.run_cmd(command)
    command = input("")

exit()

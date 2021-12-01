def run_cmd(command):
    if command[:4] == 'help':
        print("The following is a list of valid commands with descriptions.\n\n"
              "add <particle>:\t\t\t\tAdds the specified particle to the simulation. Valid particles are: "
              "mercury, venus, earth, moon, mars, jupiter, saturn, uranus, neptune, pluto\n"
              "\t\t\t\t\t\t\tIf you specify the particle as 'custom', you can specify"
              "mass, position and velocity for a custom particle.\n"
              "del <particle>:\t\t\t\tDeletes an existing particle. If a particle is not specified, the list of current "
              "particles will be printed.\n"
              "plot <deltaT> <iterations>:\tGenerates a plot of the current system, generating new "
              "position/velocity/acceleration at intervals of <deltaT> seconds (float value).\n"
              "\t\t\t\t\t\t\tThe program runs for a total of <iterations> iterations (integer value).")
    elif command == 'add':
        print("")
    elif command == 'del':
        print("")
    elif command == 'plot':
        print("")

# Console error message if script is run directly
if __name__ == "__main__":
    print("This python script is not intended to be run independently.\n")
    input("Press the enter key to continue")
import os
import random
import time

# Define colors for the output
GREN = "\033[32m"
END = "\033[0m"

# List of F1 drivers for the current season
f1_drivers = [
    "Verstappen", "Perez", "Leclerc", "Sainz", "Hamilton", "Russell", "Norris", "Piastri",
    "Alonso", "Stroll", "Ocon", "Gasly", "Bottas", "Zhou", "Magnussen", "Hulkenberg",
    "Albon", "Sargeant", "Tsunoda", "Ricciardo"
]

# Function to display the current position of the buses
def display_buses(positions):
    output = []
    output.append(115 * "-")
    for index, position in enumerate(positions):
        output.append((position * " ") + "_______________  " + ((100 - position) * " ") + "|")
        output.append((position * " ") + "|__|__|__|__|__|___ " + ((97 - position) * " ") + "|")
        output.append((position * " ") + f"|    {f1_drivers[index]:<12} |)" + ((96 - position) * " ") + "|")
        output.append((position * " ") + "|~~~@~~~~~~~~~@~~~|)" + ((95 - position) * " ") + "|")
        output.append(115 * "_")
    return "\n".join(output)

# Initialize positions for all buses
positions = [0] * len(f1_drivers)

# Display the introduction
introduction = """
        <<<<<<<<<<< Carrera de Autobuses >>>>>>>>>>
            Participantes: " + ", ".join(f1_drivers) + "
"""
print(introduction)
time.sleep(3)

# Main loop to run the race
clear_command = "cls" if os.name == "nt" else "clear"
while all(position < 97 for position in positions):
    # Randomly decide which bus moves forward
    positions[random.randint(0, len(f1_drivers) - 1)] += 1
    
    # Clear the screen and display the updated positions
    os.system(clear_command)
    print(display_buses(positions))
    time.sleep(0.1)  # Increased sleep time to make the display more fluid

# Determine the winner
winner = f1_drivers[positions.index(max(positions))]

# Display the winner
print(f"{GREN}GANÓ LA CARRERA: {winner}{END}")

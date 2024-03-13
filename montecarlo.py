# This is the montecarlo problem!
import random

# Generate a random number between 0 and 2
winner_door = random.randint(0,2)

doors = [0,0,0]

# We make one winner door
doors[winner_door] = 1

# We choose one of the doors randomly
chosen_door = random.randint(0, 2)

# Host opens a door
for i in range(3):
    if i != chosen_door and doors[i] == 0:
        doors[i] = 'goat'
        break

# Now we have the option to switch our choice
# If we switch, we will choose the other unopened door
switch_door = 3 - chosen_door - doors.index('goat')

# Now we can check if we would win by sticking or switching
win_by_sticking = (doors[chosen_door] == 1)
win_by_switching = (doors[switch_door] == 1)

print(f"Win by sticking: {win_by_sticking}")
print(f"Win by switching: {win_by_switching}")
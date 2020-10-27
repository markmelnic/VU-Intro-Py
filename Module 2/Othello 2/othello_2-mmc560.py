""" Assignment: Othello 2
    Created on 27 oct. 2020
    @author: Mark Melnic """

SECOND = 1000  # milliseconds
MINUTE = 60000  # milliseconds
HOUR = 3600000  # milliseconds

black_player = int(input("Enter the time the black player thought: "))
white_player = int(input("Enter the time the white player thought: "))

human_player = max(black_player, white_player)

time_thought = ""
# calculate hours thought
hours_thought = human_player / HOUR
human_player = human_player % HOUR
if hours_thought >= 1:
    if hours_thought < 10:
        time_thought += "0" + str(int(hours_thought)) + ":"
    else:
        time_thought += str(int(hours_thought)) + ":"
else:
    time_thought += "00:"

# calculate minutes thought
minutes_thought = human_player / MINUTE
human_player = human_player % MINUTE
if minutes_thought >= 1:
    if minutes_thought < 10:
        time_thought += "0" + str(int(minutes_thought)) + ":"
    else:
        time_thought += str(int(minutes_thought)) + ":"
else:
    time_thought += "00:"

# calculate seconds thought
seconds_thought = human_player / SECOND
if seconds_thought >= 1:
    if seconds_thought < 10:
        time_thought += "0" + str(int(seconds_thought))
    else:
        time_thought += str(int(seconds_thought))
else:
    time_thought += "00"

print("The time the human player has spent thinking is:", time_thought)

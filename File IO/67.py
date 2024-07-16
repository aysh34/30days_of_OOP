# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score

def game():
    score = int(input("Enter your score: "))
    return score


user = game()
with open("Hi-score.txt") as f:
    highscore = f.read()  # Read the highscore as a string from the file

if highscore == "" or int(highscore) < user:
    with open("Hi-score.txt", "w") as f:
        f.write(str(user))  # Write the user score to the file

def game():
    score = int(input("Enter your score: "))
    return score


with open("Hi-score.txt") as f:
    highscore = int(f.read())

if game() > highscore:
    with open("Hi-score.txt", "w") as f:
        f.write(game())

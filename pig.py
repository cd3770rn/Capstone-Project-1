import random

# If the player rolls a 1, they score nothing and it becomes the next player's turn.
# If the player rolls any other number, it is added to their turn total and the player's turn continues.
# If a player chooses to "hold", their turn total is added to their score, and it becomes the next player's turn.
# The first player to score 100 or more points wins.

def roll(player):
    # Roll a random number and print it to console
    diceRoll = random.randint(1, 6)
    print(player + " rolled a " + str(diceRoll))
    return diceRoll

def cpuRoll():
    # Roll a random number and print it to console
    diceRoll = random.randint(1, 6)
    print("CPU rolled a " + str(diceRoll))
    return diceRoll

def promptHold():
    # Ask player if they want to hold
    while True:
        hold = input("Would you like to roll again? (Y/N) ")
        if hold not in ["Y", "y", "Yes", "yes", "N", "n", "No", "no"]:
            print("Please enter Y or N.")
            print("===============")

        else:
            return hold

def playerTurn(player, playerScore, pointsToWin):
    score = 0

    print(player + "'s turn begins. Total score: " + str(playerScore))
    playerRoll = roll(player)
    score += playerRoll

    while playerRoll != 1:
        # Ask the player if they want to roll again
        hold = promptHold()
        # If the player doesn't roll again, add the score they have accumulated to their score.
        if hold in ["N", "n", "no"]:
            playerScore += score
            print(player + " held. Total score: " + str(playerScore))
            testScore(player, playerScore, pointsToWin)
            print("===============")
            return playerScore

        elif hold in ["Y", "y", "yes"]:
            playerRoll = roll(player)
            score += playerRoll

    print(player + "'s turn ends. Lost score: " + str(score))
    print("===============")
    return playerScore

def cpuTurn(cpuScore, pointsToWin):
    score = 0

    print("CPU's turn begins. Total score: " + str(cpuScore))
    roll = cpuRoll()
    score += roll

    while roll != 1:
        # Generate a 0 or 1 representing whether or not to roll again
        hold = bool(random.getrandbits(1))
        # If the cpu holds, add the score it has accumulated to its score.
        if hold == 0:
            cpuScore += score
            print("CPU held. Total score: " + str(cpuScore))
            testScore("CPU", cpuScore, pointsToWin)
            print("===============")
            return cpuScore

        elif hold == 1:
            roll = cpuRoll()
            score += roll

    print("CPU's turn ends. Lost score: " + str(score))
    print("===============")
    return cpuScore

def testScore(player, playerScore, pointsToWin):
    if (playerScore >= pointsToWin):
        print(player + " wins!")

def getOpponentType():
    while True:
        opponentChoice = input("Play against CPU or human?\n")
        if opponentChoice not in ["CPU", "cpu", "Human", "human"]:
            print("Please enter CPU or human.")
            print("===============")

        else:
            return opponentChoice

def getPointsToWin():
    while True:
        try:
            pointsToWin = int(input("Play to how many points?\n"))

        except ValueError:
            print("Please enter a number.")
            print("===============")
            continue

        else:
            return pointsToWin

def play():
    playerScore = 0
    opponentScore = 0

    opponentChoice = getOpponentType()
    pointsToWin = getPointsToWin()
    print("===============")


    while True:
        playerScore = playerTurn("Player 1", playerScore, pointsToWin)

        if playerScore >= pointsToWin:
            break

        if opponentChoice in ["CPU", "cpu"]:
            opponentScore = cpuTurn(opponentScore, pointsToWin)

        elif opponentChoice in ["Human", "human"]:
            opponentScore = playerTurn("Player 2", opponentScore, pointsToWin)

        if opponentScore >= pointsToWin:
            break


play()
#Pokemon drinking game. Get glitched!
import random, time
import random

print('How many players are there?')
count = input()

for c in count.lower():
    if count != range(2, 100):
        print('Please enter the number of players.')
        count = input()
    else:
        continue


leadSquare = 0

# class for spiller object.
class Player():

    playerCount = 0
    square = 0

    def __init__(self, name, gender, color):
        self.name = name
        self.gender = gender
        self.color = color

        Player.playerCount += 1

    def moveSquare(self, amount):
        self.square += amount

    def rollDie(self):
        dice = random.randint(1, 6)
        self.moveSquare(dice)

        print('It is ' + self.name + '\'s turn.')
        print("Roll a die! Press enter to roll.")
        pressenter = input()
        time.sleep(0.5)
        print('You are now on square ' + str(self.square) + '.')

# class for spillebrætsfelt object.. Hvordan håndteres de særlige funktioner?
class boardSquare:
    index = 0
    def __init__(self, squareType):
        self.squareType = squareType

    def readText(cls, textIndex):
        print(str(mySquares[cls.textIndex]))


#Laver en liste med alle spillerne...
mySquares = []

with open('PDGfelter.txt', 'r') as f:
    mySquares = [line.strip() for line in f]

players = []

for i in range(0, int(count)):
    print('Hello player number ' + str(i + 1) + '!')
    time.sleep(0.5)
    print('What is your name?')
    name = input()
    print('Are you a boy or a girl?')
    gender = input()
    while gender.lower() not in {'boy', 'girl'}:
        print('Please write if you\'re a boy or a girl.')
        gender = input()
    print('What starter do you choose? red, green, blue?')
    color = input()
    while color.lower() not in {'red', 'green', 'blue'}:
        print('Please write the color of your starter Pokemon. Red, green or blue.')
        color = input()
    players.append(Player(name, gender, color))

for squares in mySquares:
    for player in players:
        player.rollDie()
        time.sleep(1)
        print(str(mySquares[player.square]))

time.sleep(3)

# *******Hangman Game******* #

#Importing the random module to later allow the random choosing of a word from the secretwords lists and the turtle module to draw the hangman game on the screen.#

import random
import turtle
window = turtle.Screen()
window.setup(width = 1.0, height = 1.0)
window.bgcolor("white")
window.title("Hangman")
NT = turtle.Turtle()
BSHT = turtle.Turtle()
NT.speed(10)
BSHT.speed(10)

#*************** SUB PROGRAMS ***************#

#Draws the noose for the hangman#

def drawNoose(turtle):
  turtle.hideturtle()
  turtle.penup()
  turtle.backward(300)
  turtle.pendown()
  turtle.forward(125)
  turtle.backward(125 / 2)
  turtle.left(90)
  turtle.forward(95)
  turtle.right(90)
  turtle.forward((125 / 2) + 55)
  turtle.right(90)
  turtle.forward(20)

#Draws the number of blanks/dashes based on the number of letters in the word that is chosen#

def drawBlankSpacesAndHiddenText(sw, turtle):
  turtle.hideturtle()
  if (len(sw) <= 6):
    for dashes in range(len(sw)):
      turtle.color("white")
      turtle.write(sw[dashes], font=("Verdana", 15, "normal"))
      turtle.color("black")
      turtle.pendown()
      turtle.forward(15)
      turtle.penup()
      turtle.forward(45)
  elif (len(sw) > 6 and len(sw) <= 12):
    for dashes in range(6):
      turtle.color("white")
      turtle.write(sw[dashes], font=("Verdana", 15, "normal"))
      turtle.color("black")
      turtle.pendown()
      turtle.forward(15)
      turtle.penup()
      turtle.forward(45)
    turtle.goto(0, -45)
    for dashes in range(6, len(sw)):
      turtle.color("white")
      turtle.write(sw[dashes], font=("Verdana", 15, "normal"))
      turtle.color("black")
      turtle.pendown()
      turtle.forward(15)
      turtle.penup()
      turtle.forward(45)
  elif (len(sw) > 12 and len(sw) <= 18):
    for dashes in range(6):
      turtle.color("white")
      turtle.write(sw[dashes], font=("Verdana", 15, "normal"))
      turtle.color("black")
      turtle.pendown()
      turtle.forward(15)
      turtle.penup()
      turtle.forward(45)
    turtle.goto(0, -45)
    for dashes in range(6, 12):
      turtle.color("white")
      turtle.write(sw[dashes], font=("Verdana", 15, "normal"))
      turtle.color("black")
      turtle.pendown()
      turtle.forward(15)
      turtle.penup()
      turtle.forward(45)
    turtle.goto(0, -90)
    for dashes in range(12, len(sw)):
      turtle.color("white")
      turtle.write(sw[dashes], font=("Verdana", 15, "normal"))
      turtle.color("black")
      turtle.pendown()
      turtle.forward(15)
      turtle.penup()
      turtle.forward(45)

#Draws each piece of the hangman if the user guesses incorrectly.#

def drawHangMan(g, hm, L, sw):
  hm.hideturtle()
  L.hideturtle()

#After the first wrong guess, the Hangman's head is drawn#

  if (len(g) == 1):
    hm.penup()
    hm.goto(-120, 45)
    hm.pendown()
    hm.circle(15)

#After the second wrong guess, the Hangman's body is drawn#

  if (len(g) == 2):
    hm.penup()
    hm.goto(-120, 45)
    hm.right(90)
    hm.pendown()
    hm.forward(60)
    hm.penup()

#After the third wrong guess, one of the Hangman's arms is drawn#

  if (len(g) == 3):
    hm.goto(-120, -15)
    hm.left(180)
    hm.forward(45)
    hm.left(135)
    hm.pendown()
    hm.forward(35)
    hm.penup()

#After the fourth wrong guess, one of the Hangman's arms is drawn#

  if (len(g) == 4):
    hm.goto(-120, 30)
    hm.left(90)
    hm.pendown()
    hm.forward(35)
    hm.penup()

#After the fifth wrong guess, one of the Hangman's legs is drawn#

  if (len(g) == 5):
    hm.goto(-120, -15)
    hm.pendown()
    hm.forward(45)
    hm.penup()

#After the sixth and last wrong guess, the Hangman's other leg is drawn, officially hanging him and ending the game#

  if (len(g) == 6):
    hm.goto(-120, -15)
    hm.right(90)
    hm.pendown()
    hm.forward(45)
    L.penup()
    L.goto(0, 60)
    L.write("Game Over! You LOSE", font=("Verdana", 20, "bold"))
    print("\nThe Secret Word was: " + sw)
    print("\nGame Over! You LOSE")

#Determines whether the user's guesses are correct or incorrect and fills in the blank spaces accordingly.#

def guess(sw):

#This spawns 3 new turtles. HM will be drawing the pieces of the hangman's body if the user guesses wrong, Lose will end the game if the user guesses incorrectly for the sixth time, and CRCT will be filling in the correct guesses in their designated spots of the secret word#

  HM = turtle.Turtle()
  Lose = turtle.Turtle()
  Lose.hideturtle()
  CRCT = turtle.Turtle()
  CRCT.hideturtle()
  HM.speed(2)
  Lose.speed(10)
  CRCT.speed(10)

#These three lists will hold the user's guesses#

  all_guesses = []
  correct_guesses = []
  incorrect_guesses = []

#The length of this list shows how many different letters are in the secret word and will be used later on to determine whether the user has won by comparing the length of this list to the length of the correct_guesses list to see if both length of both lists are equal#

  different_letters = []
  for letters in range(len(sw)):
    if (different_letters.count(sw[letters].lower()) == 0 and different_letters.count(sw[letters].upper()) == 0):
      different_letters.append(sw[letters])

#This while loop will run 5 times, allowing the user to only have 5 guesses to guess the secret word right letter-by-letter before losing#

  while (len(incorrect_guesses) < 6 and len(correct_guesses) < len(different_letters)):

#Asks the user to guess 1 letter, and if they ignore the input instructions, then they will continuously be given this prompt#

    print("\nSo far you have guessed: ", end="")
    print(all_guesses)
    guess = input("\nGuess ONE letter that you think is in the secret word/phrase: ").lower()
    while (len(guess) == 0 or len(guess) > 1 or guess.count(" ") != 0 or guess.isdigit() == True or guess.isalpha() == False):
      guess = input("\nGuess ONE letter that you think is in the secret word/phrase: ").lower()

    if (len(all_guesses) > 0):

#Checks to see if the user's guess already appears in the guesses list. If it does, then the user is asked why they would guess the same letter again. The guess still counts and the drawHangMan function is called, indicating a wasted guess on behalf of the user#

      while (all_guesses.count(guess) > 0):
        print("\nYou already guessed that letter.")
        guess = input("\nGuess ONE letter that you think is in the secret word/phrase: ").lower()

#If the above if-statement is false, then the below else-if statement checks to see if the user's guess appears 0 times in the array, indicating a new guess. The new guess is added to the guesses list#

      if (all_guesses.count(guess) == 0):
        all_guesses.append(guess)

#Checks to how many times the the user's guess appears in the secretword. If it appears 0 times, then the drawHangMan function is called, indicating an incorrect guess If it appears more than 0 times, then the spots where the guessed letter is will be revealed on screen#

        if (sw.count(guess) == 0 and sw.count(guess.upper()) == 0):
          incorrect_guesses.append(guess)
          drawHangMan(incorrect_guesses, HM, Lose, SecretWord)
        elif (sw.count(guess) != 0 or sw.count(guess.upper()) != 0):
          correct_guesses.append(guess)
          if (len(sw) <= 6):
            for dashes in range(len(sw)):
              if (sw[dashes] == guess or sw[dashes] == guess.upper()):
                CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
              CRCT.pendown()
              CRCT.forward(15)
              CRCT.penup()
              CRCT.forward(45)
            CRCT.goto(0, 0)
          elif (len(sw) > 6 and len(sw) <= 12):
            for dashes in range(6):
              if (sw[dashes] == guess or sw[dashes] == guess.upper()):
                CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
              CRCT.pendown()
              CRCT.forward(15)
              CRCT.penup()
              CRCT.forward(45)
            CRCT.goto(0, -45)
            for dashes in range(6, len(sw)):
              if (sw[dashes] == guess or sw[dashes] == guess.upper()):
                CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
              CRCT.pendown()
              CRCT.forward(15)
              CRCT.penup()
              CRCT.forward(45)
            CRCT.goto(0, 0)
          elif (len(sw) > 12 and len(sw) <= 18):
            for dashes in range(6):
              if (sw[dashes] == guess or sw[dashes] == guess.upper()):
                CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
              CRCT.pendown()
              CRCT.forward(15)
              CRCT.penup()
              CRCT.forward(45)
            CRCT.goto(0, -45)
            for dashes in range(6, 12):
              if (sw[dashes] == guess or sw[dashes] == guess.upper()):
                CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
              CRCT.pendown()
              CRCT.forward(15)
              CRCT.penup()
              CRCT.forward(45)
            CRCT.goto(0, -90)
            for dashes in range(12, len(sw)):
              if (sw[dashes] == guess or sw[dashes] == guess.upper()):
                CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
              CRCT.pendown()
              CRCT.forward(15)
              CRCT.penup()
              CRCT.forward(45)
            CRCT.goto(0, 0)

#Adds the user's first guess to the end of the guesses list#

    else:
      all_guesses.append(guess)

#Checks to how many times the the user's guess appears in the secretword. If it appears 0 times, then the drawHangMan function is called, indicating an incorrect guess. If it appears more than 0 times, then the spots where the guessed letter is will be revealed on screen#

      if (sw.count(guess) == 0 and sw.count(guess.upper()) == 0):
        incorrect_guesses.append(guess)
        drawHangMan(incorrect_guesses, HM, Lose, SecretWord)
      elif (sw.count(guess) != 0 or sw.count(guess.upper()) != 0):
        correct_guesses.append(guess)
        if (len(sw) <= 6):
          for dashes in range(len(sw)):
            if (sw[dashes] == guess or sw[dashes] == guess.upper()):
              CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
            CRCT.pendown()
            CRCT.forward(15)
            CRCT.penup()
            CRCT.forward(45)
          CRCT.goto(0, 0)
        elif (len(sw) > 6 and len(sw) <= 12):
          for dashes in range(6):
            if (sw[dashes] == guess or sw[dashes] == guess.upper()):
              CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
            CRCT.pendown()
            CRCT.forward(15)
            CRCT.penup()
            CRCT.forward(45)
          CRCT.goto(0, -45)
          for dashes in range(6, len(sw)):
            if (sw[dashes] == guess or sw[dashes] == guess.upper()):
              CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
            CRCT.pendown()
            CRCT.forward(15)
            CRCT.penup()
            CRCT.forward(45)
          CRCT.goto(0, 0)
        elif (len(sw) > 12 and len(sw) <= 18):
          for dashes in range(6):
            if (sw[dashes] == guess or sw[dashes] == guess.upper()):
              CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
            CRCT.pendown()
            CRCT.forward(15)
            CRCT.penup()
            CRCT.forward(45)
          CRCT.goto(0, -45)
          for dashes in range(6, 12):
            if (sw[dashes] == guess or sw[dashes] == guess.upper()):
              CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
            CRCT.pendown()
            CRCT.forward(15)
            CRCT.penup()
            CRCT.forward(45)
          CRCT.goto(0, -90)
          for dashes in range(12, len(sw)):
            if (sw[dashes] == guess or sw[dashes] == guess.upper()):
              CRCT.write(sw[dashes], font=("Verdana", 15, "normal"))
            CRCT.pendown()
            CRCT.forward(15)
            CRCT.penup()
            CRCT.forward(45)
          CRCT.goto(0, 0)

#This if-statement will be executed at the end of the game, where the user will be notified of whether they won or lost#

  if (len(correct_guesses) == len(different_letters)):
    Win = turtle.Turtle()
    Win.speed(10)
    Win.hideturtle()
    Win.penup()
    Win.goto(-30, 60)
    Win.write("Congratulations! You WIN", font=("Verdana", 20, "bold"))
    print("\nCongratulations! You WIN")

#*************** MAIN PROGRAM ***************#

#Welcome Message and then asking the user if they're familiar with the rules of the game#

print("Welcome to Hangman!\n")
rules = input("Would you like to be introduced to the rules? (yes or no) ").lower()
while (rules != "yes" and rules != "y" and rules != "no" and rules != "n"):
  rules = input("\nWould you like to be introduced to the rules? (type yes or no --> it's recommended that you type yes, so you know the user-input rules) ").lower()
if (rules == "yes" or rules == "y"):
    print("\n1. Choose between versing the CPU or versing a friend.\n\n2. If you choose to verse a friend, then the person who won't be guessing should input the secretword (don't use spaces, make sure that your word is less than or equal to 18 letters, and don't type in numbers or symbols) without the other person knowing what it is. If you choose to verse the CPU, then you will choose between playing on either easy or hard difficulty, where you will either be given easy or hard words to guess.\n\n3. You have 6 guesses before the Hangman is drawn on screen and you lose. If you guess all the letters in the blank spots correctly before the Hangman is drawn, then you win.\n\n4. Have fun!\n")

#The user chooses a gamemode#
gamemode = str(input("\nWould you like to verse a friend or the CPU? ")).lower()

while (gamemode != "friend" and gamemode != "cpu"):
  gamemode = input("\nWould you like to verse a friend or the CPU? ")

#If the user chooses to verse a friend#
if (gamemode == "friend"):
  print("\nRemember: DO NOT type in blanks, spaces, numbers, or symbols! Your word MUST be 18 letters or less in length!")
  SecretWord = str(input("\nEnter a secret word/phrase for your friend to guess: "))

#If the user ignores the input instructions for typing in their own secret word#

  while (len(SecretWord) == 0 or len(SecretWord) > 18 or SecretWord.count(" ") != 0 or SecretWord.isdigit() == True or SecretWord.isalpha() == False):
    print("\nRemember NOT to use spaces or blanks and that your word MUST be 18 letters or less in length! Also, DO NOT type in a number or symbol!")
    SecretWord = str(input("\nEnter a secret word for your friend to guess: "))
  drawNoose(NT)
  drawBlankSpacesAndHiddenText(SecretWord, BSHT)
  guess(SecretWord)

#If the user chooses to play the CPU, then they would then choose a difficulty to verse the CPU on#

elif (gamemode == "cpu"):
  difficulty = str(input("\nWould you like to play on easy or hard difficulty? ")).lower()
  while (difficulty != "easy" and difficulty != "hard"):
    difficulty = str(input("\nWould you like to play on easy or hard difficulty? ")).lower()

#If the user chooses to play on easy#

  if (difficulty == "easy"):
    EASYSecretWords = ["Pool", "Mama", "Egg", "Fire", "Arm", "Sun", "Dinner", "Free", "Horse", "Book", "Ice", "Sea", "Home", "Cross", "Funny", "House", "Bed", "Door", "Hair", "Good", "Rain", "Drink", "Eye", "Blood", "Dog"]
    SecretWord = random.choice(EASYSecretWords)
    drawNoose(NT)
    drawBlankSpacesAndHiddenText(SecretWord, BSHT)
    guess(SecretWord)

#If the User chooses to play on hard#

  elif (difficulty == "hard"):
    HARDSecretWords = ["Jazz", "Kiwifruit", "Horror", "Quiz", "Rhythm", "Cowboy", "Zombie", "Bookworm", "Nymph", "Jacuzzi", "Zodiac", "Whiskey", "Thumbscrew", "Pneumonia", "Grogginess", "Xylophone", "Testosterone", "Espionage", "Chrysanthemum", "Simplification", "Baccalaureate", "Eavesdroppers", "Jawbreakingly", "Vaccinization", "Claustrophobia"]
    SecretWord = random.choice(HARDSecretWords)
    drawNoose(NT)
    drawBlankSpacesAndHiddenText(SecretWord, BSHT)
    guess(SecretWord)
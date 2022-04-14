import random 

def numberGuessGame(num1, num2):
  answer = random.randint(1, 10)
 
  while True:
    try: 
      guess = int(input("Guess a number between 1 and 10.  "))
      if  0< guess <11:
        if guess == answer:
          print(f'Correct! The number is {answer}.')
          break 
        elif guess > answer:
          print("Too high. ", end = "")
        else:
          print("Too low. ", end = "")
      else:
        print("Please enter a number between 1 and 10.  ")
    except ValueError: 
      print ("Please only enter numbers.")

  again = input("Do you want to play again?  ")
  if again == "no":
    print("Goodbye.")
  else:
    numberGuessGame()
    

numberGuessGame()
  
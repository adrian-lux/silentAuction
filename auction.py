from replit import clear
from art import logo

#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welomce to the silent auction!\n")

biddersList = {}
while True:
  name = input("What is the name of the bidder? \n")
  amount = int(input("How much are you willing to bid?\n $"))
  biddersList[name] = amount
  answer = input("Is there anyone else who wants to bid? (yes,no)\n")
  if(answer == "no"):
    higgestBit = 0
    for bidder in biddersList:
      if(higgestBit < biddersList[bidder]):
        higgestBit = biddersList[bidder]
        winner = bidder
    clear()    
    print(f"The winner is {winner} with an amount of ${biddersList[winner]}")
    break   
  else:
    clear()
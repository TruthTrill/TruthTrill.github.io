#keepGoing.py
#demonstrates loop with multiple exits
#Charles Barnes


correct = "ricky"
tries = 0

keepGoing = True
while(keepGoing):

  tries = tries + 1
  print ("try #", tries)

  guess = input("What is the password ")
  if guess == correct:
    print("That's correct! Here's the treasure!")
    keepGoing = False
    
  elif tries >= 3:
    print("Too many wrong tries. Launching the missiles")
    keepGoing = False

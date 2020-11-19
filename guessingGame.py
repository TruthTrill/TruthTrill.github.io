from random import randint
secret = randint(1,10)
print("Yo wassup!")
guess = 0
while guess != secret:
  g = input("Guess da numba: ")
  guess = int(g)
  if guess == secret:
    print("You win! Aaayyeee~")
  else:
    if guess > secret:
      print("Too High mf")
    else:
      print ("Too low bih")
print("Game over!")
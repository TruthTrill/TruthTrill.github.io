def product(x, y):
  x * y;

#Just creating a function.
def printResult():
  #tell user "answer is " sum
  print ("Yo", name + "!");
  print ("The answer is", sum);
  print ("This is the product just in case you need it!", product);
  if (sum > 100):
    print ("Wow this is a large number!")
  elif (sum == 33):
    print ("That's My age!", sum)
  else:
    print ("Meh... Number is small...")



#Put your name in this box.
name = input("What is your name? ")
 
#Ask them to add numbers.
print ("Hi, {}".format(name),"how are you today? Ready to add some numbers right quick?");

#create an integer variable for x
x = 0
#create an integer variable for y
y = 0
#create an interger variable for sum 
sum = 0

#ask the user for "X: " and put answer in x
x = input("Fist Number: ")
#ask the user for "Y: " and put answer in y
y = input("Second Number: ")

#convert x to integer:
x = int(x)
#convert y to integer:
y = int(y)

#put x + y in sum
sum = x + y
product = x * y

#tell user "answer is " sum
printResult()
 

def multiplyNum(x, y):
 print (product);

niggas = sum
while niggas < 50:
		print("Ran up " + str(niggas) + " times.")
		niggas = niggas + 1
		if niggas == 50:
			break

def recursiveSum(niggas):
  if (niggas <= 50):
    return niggas
  else:
    return (niggas + recursiveSum(niggas - 1))

recursiveSum = niggas
print (recursiveSum)
import random
import os

def fu():
 a = random.randint(1,5)
 b = int(input("Enter a number from 1 to 5:"))
 
 print("You entered a number:", b)
 print("Number dropped:", a)
 
 if b == a :
  print("Bad luck!")
  os.system('shutdown -s')
  
 if b != a:
  print("Lucky!")
  fu()

fu()

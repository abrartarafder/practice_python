# problem 1
from datetime import date

todays_date = date.today()
name = input("Enter your name: ")
age = int(input("Enter your age: "))

remaining = 100 - age
year = todays_date.year + remaining
print(f'hey {name}, you will turn 100 in {year}!!')

# problem 2
n = int(input("Enter number: "))
if n % 2 == 0:
  print("Even")
else:
  print("Odd")
  
  
#   problem 3
def printNum(listie):
  for i in listie:
    if i < 5:
      print(i)
      
printNum([1,2,3,4])

# problem 4

n = int(input("Enter a number: "))
for i in range(1,n):
  if (n % i) == 0:
    print(i)
#     problem 5

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

newlist = []
newlist2 = []

for i in a:
  for k in b:
    if i == k:
      newlist.append(i)
      newlist2.append(k)
# set used to print 1
print(sorted(set(newlist)))
print(sorted(set(newlist2)))



# problem 6
n = input("Enter a string: ")
if n == n[::-1]:
  print("Palindrome")
else:
  print("NOT")
  
  
  
  
# problem 7
def listeven(listall):
  newlist = []
  for i in listall:
    if (i % 2) == 0:
      newlist.append(i)
  print(newlist)
      
listeven([12,10,91,1])



# problem 8
# ---- invalid notebook message ---

# problem 9

import random
n = random.randint(0,10)

for i in range(5):
  i = int(input("Enter a number to guess: "))
  if i < n:
    print("Too low")
  if i == n:
    print("Correct")
    break
  if i > n:
    print("Too high")

print(f"number was {n}")

# problem 10

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

newlist = []

for i in set(a):
  for k in set(b):
    if i == k:
        newlist.append(i)
      
print(newlist)

# problem 11

def is_prime(n):
    if n < 2:
        return False
    # range doesnt include itself
    for i in range(2,n):
        if (n % i) == 0:
            return False
    
    return True

n = int(input("Enter num: "))
if is_prime(n):
    print("PRIME")
else:
    print("NOT PRIME")
    
    

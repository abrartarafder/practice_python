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
    
    

from datetime import date

todays_date = date.today()
name = input("Enter your name: ")
age = int(input("Enter your age: "))

remaining = 100 - age
year = todays_date.year + remaining
print(f'hey {name}, you will turn 100 in {year}!!')

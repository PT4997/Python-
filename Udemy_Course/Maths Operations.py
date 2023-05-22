Double artrisk (**)  = "số mũ của 1 số"
#for example : 2**3 = "2 mũ 3"
# PAMDES
Parenthese : ()
Exponents: **
Multiplication : * , Division : /
Addition : + , Subtraction : -
# Count BMI
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight) / (float(height) * float(height)) #  or float(height) ** 2
print(int(BMI)) # 2 số nguyên trc dấu phẩy
print(BMI) # 1 dãy số
# round number
round(2.666667, 2) # làm tròn 2 số sau dấu phẩy
#f-String
score = 0
print(f"Your score is + {score}")
# Exercise Life in Weeks : Tính số ngày, tuần, tháng còn sống nếu sống đến 90 tuổi
age = input("What is your current age? ")
day =  (90 * 365) - (int(age) * 365)
week = (90 * 52) - (int(age) * 52)
month = (90 * 12) - (int(age) * 12)
print(f"You have {day} days, {week} weeks, and {month} months left.")
# Exercise pay the bill/person
print("Welcome to the tip calculator!")
bill = float(input("What was total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_people = int(input("How many people to split the bill? "))
money = (bill + (bill /100 * tip)) / number_people
total = round(money,2)
total = "{:.2f}".format(money)
print(f"Each person should pay ${total}")


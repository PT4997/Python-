# % là 1 số chia 1 số dư mấy
7 % 3 = 1
# odd là số lẻ
# even là số chẵn
# Check odd or even number
number = int(input("Type the number do you want to check? "))
if number % 2 == 0:
    print("This is the even number")
else:
    print("This is the odd number")
# BMI 2.0
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI_number = weight / (height * height)
BMI = round(BMI_number)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
# Count leap/not leap year : Năm nào có đuôi là 2 chữ số 0 thì phải chia hết cho 400 => năm nhuận , còn lại chia hết cho 4 => năm nhuận
year = int(input("Which year do you want to check? "))
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0 ):
    print("This is a leap year.")
else:
    print("This isn't a leap year.")
 a = a + 1 same a += 1
# Pizza Python Orders
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill += 15
elif size =="M":
    bill += 20
else:
    bill+= 25
if add_pepperoni == "Y"
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is : ${bill}.")
# Love Calculator
\n : xuống dòng
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = name1 + name2
lower_name = name.lower()
T = lower_name.count('t')
R = lower_name.count('r')
U = lower_name.count('u')
E = lower_name.count('e')
true = T + R + U + E
L = lower_name.count('l')
O = lower_name.count('o')
V = lower_name.count('v')
E = lower_name.count('e')
love = L + O + V + E
love_score = str(true) + str(love)
if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >= 40 and int(love_score) <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
# Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# Diagram Logical Operators : https://viewer.diagrams.net/index.html?highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'? ")
if a == "left":
    b = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait a boat. Type "swim" to swim across. ')
    if b == "wait":
        c = input("You arrive at the island unharmed. There is 3 housed=s with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if c == "yellow":
            print("You win")
        elif c == "blue":
            print("You eaten by beasts. Game over!")
        else:
            print("You are burned by fire. Game over!")
    else:
        print("You attacketed by trout. Game over!")
else:
    print("You fall into a hole. Game over!")

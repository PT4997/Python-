import random
random_integer = random.randint(1,10)
print(random_integer)
#random() là những số float từ 0 đến 1
random_float = random.random()* 5 # số float từ 0 đến 1 ko gồm 5
print(random_float)
# print "Heads" or "Tails"
random_int = random.randint(0,1)
if random_int == 0:
    print("Heads")
else:
    print("Tails")
#Banker Roulette
# Split string method
names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(", ")
import random
random_name = random.randint(0,(len(names)-1))
print(names[random_name]+" " + "is going to buy the meal today!")
#Treasure Map
row1 = ["⬜️","️⬜","️⬜"]
row2 = ["⬜","⬜","️⬜"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
a = int(position[0])
b = int(position[1])
map[b-1][a-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
#Rock Paper Scissors - Kéo Búa Bao
import random
list = ["Rock", "Paper", "Sicssors"]
choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Sicssors\n")
if int(choice) >= 3:
    print("You typed an invalid number. You lose!")
print(f"You choose {list[int(choice)]}.")
random = random.randint(0,2)
print(f"The computer chooses {list[random]}.")
if random == int(choice):
    print("You draw!")
elif random != 0:
    if int(choice) != 0:
        if int(choice) > random:
            print("You win!")
        elif int(choice) < random:
            print("You lose!")
    elif int(choice) == 0:
        if random == 1:
            print("You lose!")
        elif random == 2:
            print("You win")
elif random == 0:
    if int(choice) == 1:
        print("You win!")
    elif int(choice) == 2:
        print("You lose!")
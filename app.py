import random

count = 0
x = random.randint(1, 1000)
print(x)

value = input("Enter your guess from 1 to 1000:")
list = [500,200,100,100,50,20,10,10,5,0]
min_value = 1
max_value = 1000

for i in list:
    count += 1
    if int(value) == x:
        print("You got it! The hidden number is " + str(value))
        print("It took you" + " " + str(count) + " guesses!")
        break

    elif int(value) != x:
        print("Wrong! Guess count:" + " " + str(count))
        if count == 10:
            print("GAME OVER!")
            break
        if abs(x - min_value) <=  abs(max_value - x):
            max_value = max_value - i
            value = input("Enter your guess from" + " " + str(min_value) + " " + "to" + " "  + str(max_value) + ":")
        else:
            min_value = min_value + i
            value = input("Enter your guess from" + " " + str(min_value) + " " + "to" + " " + str(max_value) + ":")


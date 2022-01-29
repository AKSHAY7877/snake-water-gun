#       Snake Water Gun game by Akshay Sharma
import random
times = 10
list1 = ["snake" , "water", "gun"]
user_points = 0
comp_points = 0
i = 0
print("\t\t\t\t\tLet's start Snake Water Gun\n")
chances = 10
while i < times:
    print(f"\nChances left = {chances}\tPlayer Points = {user_points}\tComputer Points = {comp_points}")
    print("\nchoose '1' for snake, '2' for water, '3' for gun")
    user = input()
    if user == "1" or user == "2" or user == "3":
        pass
    else:
        print("Invalid input")
        continue
    comp = random.choice(list1)
    if user == "1" and comp == "snake":
        print("It's a TIE")
    elif user == "1" and comp == "water":
        user_points += 1
        print("Player Win \tcomputer choosen",comp,"\nSnake drinks the water")
    elif user == "1" and comp == "gun":
        comp_points += 1
        print("computer win \tcomputer choosen",comp,"\nGun kills the snake")
    elif user == "2" and comp == "snake":
        comp_points += 1
        print("computer Win \tcomputer choosen",comp,"\nSnake drinks the water")
    elif user == "2" and comp == "water":
        print("It's a TIE")
    elif user == "2" and comp == "gun":
        user_points += 1
        print("Player Win \tcomputer choosen",comp,"\nGun fails in Water")
    elif user == "3" and comp == "snake":
        user_points += 1
        print("Player Win \tcomputer choosen",comp,"\nGun kills the snake")
    elif user == "3" and comp == "water":
        comp_points += 1
        print("computer Win \tcomputer choosen",comp,"\nGun fails in Water")
    elif user == "3" and comp == "gun":
        print("It's a TIE")
    i += 1
    chances -= 1
else:
    if user_points > comp_points:
        print("\n\n\t\t\t\tPlayer Won\nPlayer points = ",user_points, "\tComputer points = ", comp_points)
    elif user_points == comp_points:
        print("\n\n\t\t\t\tIt's a tie between player and computer\nPoints = ",user_points)
    else:
        print("\n\n\t\t\t\tComputer Won\nComputer points = ", comp_points, "\tPlayer points = ", user_points)
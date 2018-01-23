import random

comp_choice = random.randint(1, 3)
print("Hello welcome to RPS game")
username = input("What is your name? ")
user_score = 0
comp_score = 0


def check_result_for_user(user):
    if user == 1:
        print("{} chose Rock 👊".format(username))
        return 1
    elif user == 2:
        print("{} chose Paper 👋".format(username))
        return 2
    elif user == 3:
        print("{} chose Scissor 🤘".format(username))
        return 3
    else:
        print("Invalid number please choose again")


def check_result_for_comp():
    if comp_choice == 1:
        print("{} chose Rock 👊".format("Computer"))
        return 1
    elif comp_choice == 2:
        print("{} chose Paper 👋".format("Computer"))
        return 2
    else:
        print("{} chose Scissor 🤘".format("Computer"))
        return 3


def print_less(user, username):
    if user == 1:
        print("{} chose Rock 👊".format(username))
        return 1
    elif user == 2:
        print("{} chose Paper 👋".format(username))
        return 2
    elif user == 3:
        print("{} chose Scissor 🤘".format(username))
        return 3
    else:
        print("Invalid number please choose again")


def game_result(num):
    global comp_score
    global user_score
    if compresult == num:
        print("{} won the game".format("Comp"))
        comp_score += 1
    else:
        print("{} won the game".format(username))
        user_score += 1


def printScore():
    print("Current Score: {} {}, Comp {}".format(username, user_score, comp_score))


while True:
    printScore()
    print(""" 
          Choose one of the options: 
          1 for Rock 👊
          2 for Paper 👋
          3 for Scissor 🤘
          😊
          """.replace("  ", ""))
    user_choice = int(input(": -> "))

    compresult = check_result_for_comp()
    userresult = check_result_for_user(user_choice)

    if compresult == userresult:
        print("Game Tied")
    elif userresult == 1:
        game_result(2)
    elif userresult == 2:
        game_result(3)
    elif userresult == 2:
        game_result(1)
    elif userresult == 3:
        game_result(1)
    printScore()
    again = input("Wanna try again?: ")

    if again == "no":
        break

from random import randrange
from math import ceil

def game(sum):
    val ="Y"
    while sum > 0 and val == "Y":

        game_amount = def_amount(sum)

        if(game_amount != 0):
            numberSelected = int(input("Select a number among 0 to 59\n")) #i will handle exception next time
            sum += play(numberSelected, game_amount)
            print("Actually you have {} ".format(sum) +"$")
            print("do you want to try again ?")
            val = (input("press 'Y' if you wish to continue the party\n")).capitalize()
        else :
            print("do you want to continue and change your amount ?")
            val = (input("press 'Y' if you wish so\n")).capitalize()

def play(number,amount):
    numb = randrange(50)
    if number == numb:
        print("you guess well, congratulation\n")
        return amount * 3
    elif number % 2 == numb % 2 :
        money_lost = ceil(amount/2)
        print("you missed the correct number anyway you guess the right color case, you lost {}!".format(money_lost))
        print("the right number was {} \n".format(numb))
        return - money_lost
    else:
        print("you missed the correct number and the right color case, you lost {}!".format(amount))
        print("the right number was {} \n".format(numb))
        return - amount

def def_amount(sum):
    amount = int(input("How much do you want to use for this round\n")) #i will handle exception next time
    if sum > amount: 
        print("your money for this round is {}".format(amount) + "$")
        return amount
    else:
        print("Sorry you don't have enough money\n")
        return 0

if __name__ == "__main__":
    sum = 1000
    print("\n you have 1000$ in your account\n")
    game(sum)
    print("Thank You for your participation\n\n")
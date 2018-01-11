import random

money = 15
bet = 1
lucky_seven = 7
rounds = 0
max_money_round = 0
highest_money = 15

while money > 0:
    print("This is your money right now: %s." % money)

    Dice1 = int(random.randint(1, 6))
    Dice2 = int(random.randint(1, 6))
    print(Dice1, Dice2)

    if Dice1 + Dice2 == lucky_seven:
        money += 4
        if money > highest_money:
            highest_money = money
            max_money_round = rounds
    elif Dice1 + Dice2 > lucky_seven:
        money -= 1
        if money > highest_money:
            highest_money = money
            max_money_round = rounds
    elif Dice1 + Dice2 < lucky_seven:
        money -= 1
        if money > highest_money:
            highest_money = money
            max_money_round = rounds
    print("You now have $" + str(money) + " left")
    rounds += 1

    if money == 0:
        print("This is how many rounds you have played: %s." % rounds)
        # print("This is the highest amount of money you should of had: %s." % Maxmoney)
        # print("and the round you should have had that money: %s." % maxmoneyround)
        print("This is the highest amount of money you had: $%s." % highest_money)
        print("and this is the round you had that money: round %s." % max_money_round)

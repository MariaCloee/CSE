import random

Money = 15
Bet = 1
lucky_seven = 7
rounds = 0
MaxMoney = 95
MaxMoneyRound = 20
while Money > 0:
    print("This is your money right now: %s." % Money)

    Dice1 = int(random.randint(1, 6))
    Dice2 = int(random.randint(1, 6))
    print(Dice1, Dice2)

    if Dice1 + Dice2 == lucky_seven:
        Money += 5
    elif Dice1 + Dice2 > lucky_seven:
        Money -= 1
    elif Dice1 + Dice2 < lucky_seven:
        Money -= 1
    print("You now have $" + str(Money) + " left")
    rounds += 1

    if Money == 0:
        print("This is how many rounds you have played: %s." % rounds)
        print("This is the highest amount of money you should of had: %s." % MaxMoney)
        print("and the round you should have had that money: %s." % MaxMoneyRound)

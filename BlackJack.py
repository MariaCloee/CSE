import random
import sys


def draw_card():
    return random.randint(1, 10)


print("Here are your cards:")
card1 = draw_card()
card2 = draw_card()
print(card1)
print(card2)


player_total = card1 + card2
print("Your total is: %d." % player_total)


print("Here are the dealer's cards:")
dealers_cards1 = draw_card()
dealers_cards2 = draw_card()
print(dealers_cards1)
print(dealers_cards2)
dealers_total = dealers_cards1 + dealers_cards2
print("The dealer's total is: %d." % dealers_total)
losing = "You Lost!"

answer = "yes"
while answer != "no":
    answer = input("It is your turn: Do you want another card?")
    if answer == "yes":
        hit_card = draw_card()
        player_total += hit_card
        print("You got a %d" % hit_card)
        print("Your total is %d" % player_total)
        if player_total == 21:
            print("You got a perfect 21!")
            sys.exit()
        if player_total > 21:
            print("You got over 21! You lost!")
            sys.exit()
if answer == "no":
    answer = ""
    while answer != "no" and dealers_total < 17:
        answer = input("Now it is the Dealer's turn. You must get over 17. Do you want another card?")
        print("YOU HAVE TO SAY YES BECAUSE YOU HAVE GREATER THAN 17!")
        answer = input("Now it is the Dealer's turn. You must get over 17. Do you want another card?")
    while answer == "yes":
        answer = input("Now it is the Dealer's turn. You must get over 17. Do you want another card?")
        hit_card = draw_card()
        dealers_total += hit_card
        print("Dealer got a %d" % hit_card)
        print("Dealer's total is %d" % dealers_total)
        if dealers_total == 21:
            print("You Lost!")
            sys.exit()
        if dealers_total > 21:
            print("You Win!")
            sys.exit()
    while answer == "no" and dealers_total >= 17:
        if player_total == 21:
            print("You got a perfect 21! You Win!")
            sys.exit()
        if player_total < 21:
            if player_total < dealers_total <= 21:
                print("You got %d, but Dealer got %d. You Lost!" % (player_total, dealers_total))
                sys.exit()
            if player_total > dealers_total <= 21:
                print("Dealer got %d, but you got %d. You Won!" % (dealers_total, player_total))
                sys.exit()
            if dealers_total == 21:
                print("Dealer got a perfect 21! You Lost!")
                sys.exit()
        if player_total > 21:
            print("You got over 21. You Lost!")
            sys.exit()

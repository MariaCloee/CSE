import random


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

answer = "yes"
while answer != "no":
    answer = input("It is your turn: Do you want another card?")
    if answer == "yes":
        hit_card = draw_card()
        player_total += hit_card
        print("You got a %d" % hit_card)
        print("Your total is %d" % player_total)
if answer == "no":
    answer = "yes"
    while answer != "no":
        answer = input("Now it is the Dealer's turn: Do you want another card?")
        if answer == "yes":
            hit_card = draw_card()
            dealers_total += hit_card
            print("You got a %d" % hit_card)
            print("Your total is %d" % dealers_total)
    if answer == "no":
        if player_total == 21:
            print("You Win!")
        if player_total < 21:
            if player_total < dealers_total <= 21:
                print("You Lost!")
            if player_total > dealers_total <= 21:
                print("You Win!")
            if dealers_total == 21:
                print("You lost!")
        if player_total > 21:
            print("You lost!")


if answer == "no":
    if player_total == 21:
        print("You Win!")
    if player_total < 21:
        if player_total < dealers_total < 21:
            print("You Lost!")
        if player_total > dealers_total < 21:
            print("You Win!")
        if dealers_total == 21:
            print("You lost!")
    if player_total > 21:
        print("You lost!")

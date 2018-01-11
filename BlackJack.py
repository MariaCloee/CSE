import random

print("Here are your cards:")
card1 = random.randint(1, 10)
card2 = random.randint(1, 10)
card3 = random.randint(1, 10)

print(card1)
print(card2)

answer = input("Do you want another card?")
if answer == "yes":
    print(card3)
    if card1 + card2 + card3 == 21:
        print("You Win!")
    if card1 + card2 + card3 < 21:
        print(input("Do you want another card?"))
    if card1 + card2 + card3 > 21:
        print("You lost!")


if answer == "no":
    if card1 + card2 == 21:
        print("You Win!")
    if card1 + card2 < 21:
        print(input("Do you want another card?"))
    if card1 + card2 > 21:
        print("You lost!")

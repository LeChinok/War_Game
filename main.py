#War game = Card, Deck, Player and Game logic
#To create a card property, we need to have a card shapes, rank, and value
import random
shapes = ("Hearts", "Circle", "Cross", "Spades")
ranks = ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten")
values = {"One":1, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10}

class Card:
    def __init__(self, shape, rank):
        self.shape = shape
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.shape

class Deck:
    def __init__(self):
        self.card_deck = []
        for shapez in shapes:
            for rankz in ranks:
                card_object = Card(shapez,rankz)
                self.card_deck.append(card_object)

    def shuffle(self):
        random.shuffle(self.card_deck)

    def serve(self):
        return self.card_deck.pop()

#Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.player_cards = []

#To add card to player hand
    def add_card(self, new_card):

        if type(new_card) == type([]):
            self.player_cards.extend(new_card)
        else:
            self.player_cards.append(new_card)
        pass

        # To serve or remove card
    def serve_card(self):
            return self.player_cards.pop(0)

    def __str__(self):
        return f"{self.name} has {len(self.player_cards)} Card(s)."

#Game set up
#Assign players
player_one = Player("One")
player_two = Player("Two")

#Create deck and shuffle deck
new_deck = Deck()
new_deck.shuffle()

#Give each player 20 cards each
import pdb

for x in range(20):
    player_one.add_card(new_deck.serve())
    player_two.add_card(new_deck.serve())

#Game logic
game_on = True
round_num = 0
while game_on:

    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.player_cards) == 0:
        print("Player one cards are finished, Player two won! Game has ended")
        game_on = False
        break

    if len(player_two.player_cards) == 0:
        print("Player two cards are finished, Player two won! Game has ended")
        game_on = False
        break

#New round, empty cards yet to be dropped on the table
    player_one_cards = []
    player_one_cards.append(player_one.serve_card())

    player_two_cards = []
    player_two_cards.append(player_two.serve_card())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_card(player_one_cards)
            player_one.add_card(player_two_cards)
            at_war = False
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_card(player_one_cards)
            player_two.add_card(player_two_cards)
            at_war = False
        else:
            print("WAR!")

            if len(player_one.player_cards) < 5:
                print("Player One Unable TO DECLARE WAR")
                print("Player two wins")
                game_on = False
                break
            elif len(player_two.player_cards) < 5:
                print("Player Two Unable TO DECLARE WAR")
                print("Player One wins")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.serve_card())
                    player_two_cards.append(player_two.serve_card())





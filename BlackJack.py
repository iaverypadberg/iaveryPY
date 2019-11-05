"""Class name is always capitalized"""
import random
"""Class Game implements the gameplay of BlackJack"""
class Game:

    def __init__(self,deck):
        self.deck = deck
        self.over21 = False
        self.max=21
        self.total = self.deck.getCardNumber(0)

    # Deals the first two cards to the player and informs them of their current total
    def deal(self):
        print"Your first card is the:",
        self.deck.printCard(0)
        self.deck.pop(0)
        self.total +=self.deck.getCardNumber(0)
        print"Your second card is the:",
        self.deck.printCard(0)
        print"Total is currently at:", self.total

    # Hit prompts the player to be hit or not. If they are hit and go over the max, they lose.
    def hit(self):
        hitOrNot = raw_input("Would you like to be hit?(y/n)")
        if hitOrNot == "y" or "Y":
            print"Here is your card:",self.deck.getCard(0)
        else:
            print"Computers turn"

"""Create a deck of cards using the MakeCard class. Added functionality so that
printing out the cards and shuffling the deck is possible"""
class Deck:

    def __init__(self):
        self.deck = []
        self.size = 52
        self.nonFaceCards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.faceCards = [11,11,11,11]

        #Add cards with number value 2-10
        for x in self.nonFaceCards:
            self.deck.append(MakeCard("red","hearts", x))
            self.deck.append(MakeCard("red","diamonds", x))
            self.deck.append(MakeCard("black","clubs", x))
            self.deck.append(MakeCard("black","spades", x))

        #Add Cards with number value 11
        for x in self.faceCards:
            self.deck.append(MakeCard("red","hearts", x))
            self.deck.append(MakeCard("red","diamonds", x))
            self.deck.append(MakeCard("black","clubs", x))
            self.deck.append(MakeCard("black","spades", x))


    #Prints the requested card out in an acceptable fashion
    def printCard(self,index):
        number, suit = deck.getCard(index)
        print number, "of", suit

    #Get an item from the index and return it
    def getCard(self,index):
        return MakeCard.getNumber(self.deck[index]),MakeCard.getSuit(self.deck[index])

    #Remove the card from the specified index
    def pop(self,index):
        self.deck.pop(index)

    #Shuffle method
    def shuffleDeck(self):
        random.shuffle(self.deck)

    #Get the value of the card
    def getCardNumber(self,index):
       return MakeCard.getNumber(self.deck[index])

"""MakeCard creates a card with a color, number, and suit. Added methods for retrieving the
color, suit and number of each card in the deck."""
class MakeCard:

    def __init__(self,color,suit,number):
        self.color=color
        self.suit=suit
        self.number=number

    # Get the number of the card because in black jack that is all that realy matters
    def getNumber(self):
        return self.number

    # Get color because why not?
    def getColor(self):
        return self.color

    # Get suit so printing out the cards looks good
    def getSuit(self):
        return(self.suit)


#Implementing the classes and their methods
deck = Deck()
#print(deck.getItem(1))
deck.shuffleDeck()
#print(deck.getItem(1))

game = Game(deck)
game.deal()
game.hit()

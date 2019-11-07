"""Class name is always capitalized"""
import random
"""Class Game implements the gameplay of BlackJack"""
class Game:

    def __init__(self,deck):

        # Universal variables
        self.deck = deck
        self.max = 21

        # Computer variables
        self.compOver21 = False
        self.compEndTurn = False
        self.compMax = 17
        self.compTotal = 0

        # Player variables
        self.over21 = False
        self.endTurn = False
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
    # They can choose to not be hit and the game will end after the computer gets its total score.
    def hit(self):
        hitOrNot = raw_input("Would you like to be hit?(y/n)")
        if hitOrNot == "y" or hitOrNot == "Y":
            print"Here is your card:",
            self.deck.printCard(0)
            self.total += self.deck.getCardNumber(0)
            print "Your total is at: ",self.total
            self.deck.pop(0)

            if self.total > self.max:
                self.over21 = True
                print "You are over 21"

        if hitOrNot == "n" or hitOrNot=="N":
            self.endTurn = True

    # Adds a card to the computers total
    # Removes from the same deck that the player is using
    # Computer loses if it is over 21
    def hitComputer(self):
        self.compTotal += self.deck.getCardNumber(0)
        self.deck.pop(0)

        if self.compTotal>= self.compMax:
            self.compEndTurn = True

        if self.compTotal> self.max:
            self.compOver21 = True
            self.compEndTurnm = True
            print "Computer is over 21"

    # A method to administer the gameplay. If the player is over the max of 21 or they would like to end their turn
    # it moves onto the computer.
    # If the computer is over or would like to end their turn, the games is over.
    def gamePlay(self):

        while self.endTurn == False and self.over21 == False:
            self.hit()
        while self.compEndTurn == False and self.compOver21 == False:
            self.hitComputer()

        self.endGame()

    # Prints out the final score of the player and the computer.
    # Declares the winner
    def endGame(self):
        print "The computers total scores is: ", self.compTotal

        # if statements deciding who wins
        if self.compOver21 == True and self.over21 == True:
            print "You and the Computer lost together."
        if self.compOver21 == True and self.over21 == False:
                print "You Win!"
        if self.over21 == True and self.compOver21 == False:
                print "Computer Wins!"
        if self.total == self.compTotal:
            print"This is a tie, so the computer wins!"
        if self.over21 == False and self.compOver21 == False:
            if self.total < self.compTotal:
                print "Computer Wins!"
            else:
                print"You Win!"


"""Create a deck of cards using the MakeCard class. Added functionality so that
printing out the cards and shuffling the deck is possible"""
class Deck:

    def __init__(self):
        self.deck = []
        self.size = 52
        self.nonFaceCards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.faceCards = [10,10,10,11]

        # Add cards with number value 2-10
        for x in self.nonFaceCards:
            self.deck.append(MakeCard("red","hearts", x))
            self.deck.append(MakeCard("red","diamonds", x))
            self.deck.append(MakeCard("black","clubs", x))
            self.deck.append(MakeCard("black","spades", x))

        # Add Cards with number value 11
        for x in self.faceCards:
            self.deck.append(MakeCard("red","hearts", x))
            self.deck.append(MakeCard("red","diamonds", x))
            self.deck.append(MakeCard("black","clubs", x))
            self.deck.append(MakeCard("black","spades", x))

    # Prints the requested card out in an acceptable fashion
    def printCard(self,index):
        number, suit = deck.getCard(index)
        print number, "of", suit

    # Get an item from the index and return it
    def getCard(self,index):
        return MakeCard.getNumber(self.deck[index]),MakeCard.getSuit(self.deck[index])

    # Remove the card from the specified index
    def pop(self,index):
        self.deck.pop(index)

    # Shuffle method
    def shuffleDeck(self):
        random.shuffle(self.deck)

    # Get the value of the card
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

# Implementing the classes and their methods
deck = Deck()
deck.shuffleDeck()
game = Game(deck)
game.deal()
game.gamePlay()

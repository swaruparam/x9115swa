"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""
import operator
from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            
    def check_count(self,number):
        ranks = [ ]
        c=0
        for card in self.cards:
            ranks.append(card.rank)
        for i in ranks:
            if ranks.count(i) == number:
                c+=1
        if c == number:
            return True
        return False        

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
        
    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""
        return self.check_count(2)

    def has_threeofakind(self):
        """Returns True if the hand has a three of a kind, False otherwise."""
        
        return self.check_count(3)
        
    def has_fourofakind(self):
        """Returns True if the hand has a four of a kind, False otherwise."""
        
        return self.check_count(4)
        
    def has_twopair(self):
        """Returns True if the hand has a twopair, False otherwise."""
        
        ranks = [ ]
        c=0
        for card in self.cards:
            ranks.append(card.rank)
        for i in ranks:
            if ranks.count(i) == 2:
                c+=1
        if c == 4:
            return True
        return False
        
        
    def has_fullhouse(self):
        """Returns True if the hand has a fullhouse, False otherwise."""
        
        ranks = [ ]
        c3=0
        c2=0
        for card in self.cards:
            ranks.append(card.rank)
        for i in ranks:
            if ranks.count(i) == 3:
                c3+=1
            if ranks.count(i) == 2:
                c2+=1
        if c3 == 3 and c2 == 2:
            return True
        return False
        
    def has_straight(self):
        ranks = [ ]
        c=0
        for card in self.cards:
            ranks.append(card.rank)
        ranks.sort()
        for i in range(len(ranks)-1):
            if ranks[i+1] == (ranks[i]+1):
                c+=1
            else:
                c=0
        if c > 4:
            return True
        return False
        
    def has_straightflush(self):
        if self.has_straight() and self.has_flush():
            return True
        return False
            
        
    def classify(self):
        label = ''
        if (self.has_straightflush() == True):
		    label='Straight Flush'
        elif (self.has_fourofakind() == True):
		    label='Four of a kind'
        elif (self.has_fullhouse() == True):
		    label='Full House'
    	elif (self.has_flush() == True):
    		label='Flush'
    	elif (self.has_straight() == True):
    		label='Straight'
    	elif (self.has_threeofakind() == True):
    		label='Three of a Kind'
    	elif (self.has_twopair() == True):
    		label='Two Pair'
    	elif (self.has_pair() == True):
    		label='One Pair'
    	else:
		    label='No Pair'
	return label
	
def deal(deck, num_cards=5, num_hands=10):
        hands = [ ]
        
        for i in range(num_hands):        
            hand = PokerHand()
            deck.move_cards(hand, num_cards)
            hands.append(hand)
        return hands
        
if __name__ == '__main__':
    # make a deck
    no_nothing = no_pair = no_twopair = no_threeofakind = no_straight = no_flush = no_fullhouse = no_fourofakind = no_straightflush = 0
    n = 1000
    num_cards = 7
    num_hands = 5
    for repeat in range(n):
        deck = Deck()
        deck.shuffle()

        hands = deal(deck,num_cards,num_hands)
        for hand in hands:
            label = hand.classify()
            if label == 'Straight Flush':
                no_straightflush+=1
            elif label =='Four of a kind':
                no_fourofakind+=1
            elif label == 'Full House':
                no_fullhouse+=1
            elif label == 'Flush':
                no_flush+=1
            elif label == 'Straight':
                no_straight+=1
            elif label == 'Three of a Kind':
                no_threeofakind+=1
            elif label == 'Two Pair':
                no_twopair+=1
            elif label == 'One Pair':
                no_pair+=1
            elif label == 'No Pair':
                no_nothing+=1
           # print label
        
    total = n*num_hands
    
    print "\nResults obtained with %d hands each with %d cards, repeated over %d iterations\n" % (num_hands,num_cards,n)
    print "Probability of getting one pair : ", float(no_pair)/total
    print "Probability of getting two pair : ", float(no_twopair)/total
    print "Probability of getting three of a kind : ", float(no_threeofakind)/total
    print "Probability of getting straight : ", float(no_straight)/total
    print "Probability of getting flush : ", float(no_flush)/total
    print "Probability of getting fullhouse : ", float(no_fullhouse)/total
    print "Probability of getting four of a kind : ", float(no_fourofakind)/total
    print "Probability of getting straight flush : ", float(no_straightflush)/total
    print "Probability of getting nothing of the above : ", float(no_nothing)/total
    
        

#Creator: Alan Wu
#Contact Info: alanwu379@gmail.com
#Senior studying Mathematics at CUNY Baruch

#The project starts by importing the random module. Every game of Higher Card  Wins will involve two players who tells the code to generat a random card (no jokers) for each of them and the card that has a higher value wins.
# A is considered 11 from BlackJack
#Freindly game, no betting (if you like betting, check out my coin flip simulator. It is solo player tho)
#The card suits doesnt play a role in this version of the game. BUT if you would like a copy of the code that does that, then reach out to me! I more than happy to code it and share it with you :) 
#What if they tied? well you will have to play it to find out :) 

#Game: Higher Card Wins
#Enjoy! :)

import random 

def deck_shuffle():
    deck = []                                                  #empty list AKA empty deck
    for card_count in range(4):                                #there are 4 suits of each vard, therefore I lopped it 4 times 
        
        for numbers in range(2,11):                            #lowest card stars with 2 and 11 is not inclusive
            x_card = str(numbers)                              #saved it as a string to be uniformal with the other elements in the list named 'deck'
            deck.insert(random.randrange(52),x_card)           #inserting each element randomly to shuffle the deck
        
        for JQKA in range(4):                                  #we cant just store the numbers from 0-3 to be J Q K A, so we will assign each face card and A to an integer in this for loop 
            if JQKA == 0:                                      
                J_card = 'J'
                deck.insert(random.randrange(52),J_card)
            elif JQKA == 1:
                Q_card = 'Q'
                deck.insert(random.randrange(52),Q_card)       #repeatedly inserting the elements/cards into the list/deck at random
            elif JQKA == 2:
                K_card = 'K'
                deck.insert(random.randrange(52),K_card)
            elif JQKA == 3:
                A_card = 'A'
                deck.insert(random.randrange(52),A_card)
    return deck                                                #return deck bacuase we want the outcome of this function to be a list, which we can use later as a shuffle deck in our card game


def card():
    deck = deck_shuffle()                                      #calling the function from above and store the outcome into 'deck'
    
#check the length of the deck by removing the # below
    #print(len(deck))
            
#check thethe deck by removing the # below
    #print(deck)    
    
    card_a = random.choice(deck)                               #let player a pick a card at random
    deck.remove(card_a)                                        #removing the card that was chosen by plater a, so player b wont pick the same exact card (making it realistic haha)
    card_b = random.choice(deck)                               #let player b pick a card at random from the deck that has 51 cards
    
    if card_a in ['J','Q','K']:                                #converting cards that are J Q K A to its value, which will be used later to find out which player has the larger card
        card_a_int = 10
    elif card_a == 'A':
        card_a_int = 11
    else:
        card_a_int = int(card_a)
        
    if card_b in ['J','Q','K']:                                #converting cards that are J Q K A to its value, which will be used later to find out which player has the larger card
        card_b_int = 10
    elif card_b == 'A':
        card_b_int = 11
    else:
        card_b_int = int(card_b)
    
    if card_b_int > card_a_int:                 
        print('Player A has a {}, player B has a {}. Therefore, player B wins!'.format(card_a,card_b))        #comparing card values
    elif card_b_int < card_a_int:
        print('Player A has a {}, player B has a {}. Therefore, player A wins!'.format(card_a,card_b))    
    else: 
        print('Player A has a {}, player B has a {}. Therefore, it is A tie!'.format(card_a,card_b))
        
        
card()    #calling the function card, which contains the function deck_shuffle :)

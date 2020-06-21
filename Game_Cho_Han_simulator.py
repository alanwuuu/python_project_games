#Creator: Alan Wu
#Contact Info: alanwu379@gmail.com
#Senior studying Mathematics at CUNY Baruch

#The project starts by importing the random module. Every game of Cho-Jan will involve generating two random number and adding them up to determined wether they are odd or even.

#Game: Cho-Han
#Enjoy! :)

import random

def Cho_Han(bet):
    first_dice = int(random.randrange(1,6))             #dice roll once
    second_dice = int(random.randrange(1,6))            #dice rool again
    dice_sum = first_dice + second_dice                 #add up the dices! Since python will do math for us, no calculator needed
    if dice_sum % 2 == 0:                               #using modulo 2 to see if sum is even or not
        dice = 'even'
    else:                                               #if you never seen modulo before, here is a quick example. 7 modulo 3 is 1 becuase 1 is the remainder after you divide 7 by 3. So 8%2 will be 0 becuase 8/2 will give you a whole number! Hope this helps :)
        dice = 'odd'
    if bet == dice:
        return "Congratulations! Your guess for {} is right, we have a {} and a {}, which adds up to {}.".format(dice,first_dice,second_dice,dice_sum)      #nice guess! I bet its not luck!
    else:
        return "um.. your luck ran out.. try again next time. I believe in you! ^_^"                #little unlucky, but its ok! try again :)
    
bet = str(input("Have you played Cho-Han before? Well, its simple, we roll 2 dices and you guess the sum of them is odd or even. Take a guess! Enter odd or even here: ")) #getting input from user while informing them what Cho-Han is all about

if bet != 'odd' and bet != 'even':   #elimating entries that are NOT odd or even, I could have writen more code to make Odd and Even acceptable too but I am too lazy
    print( 'I donnot think you enter either odd or even, maybe you will have to use lowercase O or E? PLease try again! ^_^')
else:
    print(Cho_Han(bet))   #once the bet is vaild, we shall run the Cho-Han simulator
#Creator: Alan Wu
#Contact Info: alanwu379@gmail.com
#Senior studying Mathematics at CUNY Baruch


#The project starts by importing the random module. Every game of chance will involve generating a random number.

#The project also has a variable named money that starts at 100. This represents your total amount of money. In every game of coin flip, you will be able to bet money. The value of money should change depending on whether you win or lose the game.

#Game: Coin Flip 
#Enjoy! :)

import random

#starting fund
total_money = float(100)


def coin_flip_start(play):      #function for user interaction
    if play == "No":            #this never realy happens becuase people love coin flipping...
        return 'Sad to see you go >_<'
    else:    
        while play == 'Yes':    #where all the fun starts
            bet_amount = float(input('How much would you like to bet? PLEASE enter the amount you would like to bet Here: '))         #where you can decide wether you want to be a risky player or a passive player
            bet_outcome = str(input('Would you like to bet on Heads or Tails? (Note: please type Heads or Tails with exact spelling and use upper case for the first letter) Enter Here: '))  #well, this is kinda pointless becuase its 50%/50%, unless there is a bug in my code?? O_O
            print(coin_flip(bet_amount,bet_outcome))  #tells us if we are winning or on our way to wininng 
            if total_money == 0:                                                                        #zero balance, cant play anymore
                print('Note: You cant play anymore due to no more funding... Come back later!')
                play = 'No'
            elif total_money < 0:                                                                       #so this person owes us money now.. what to do...
                print("So you owe use money now! pay back ASAP or we have to make you code for us!!")
                play = 'No'
                break                                                                                   #break out of the if loop and since play is equal to 'no', the while loop is broken as well, therefore we are done! Well not yet.. this person still owes us money haha
            else:
                play = str(input('Would you like to play coin flip again? PLease enter Yes or No: '))  #asking us if we want to play again, and our input will tigger the coin flipping simulator
        else:  
            if total_money > 0:
                print('Umm are you sure? Please try to enter Yes play again! (Upper case Y btw)')       #giving the user a second chance to play again, they dont want to lose thier progres right? haha
                play = str(input('Would you still like to play coin flip again? ^_^ PLease enter Yes or No: ')) #where they decide to play or not to play  (Shakespeare reference...)

            
                if play != 'Yes' and play != 'No':  #when users into somthing like '321^9%$8ry23f23g28$@$!7', we just have to ask them again if want to coin flip again lol
                    play = str(input('Sorry! I didnt understand that... So would you still like to play coin flip again? ^_^ PLease enter Yes or No: ')) #very friendly mmessage
                    return coin_flip_start(play)  #triggering the coin flipping machine if the user say YES! (Note: for inner if statement)
                else:
                    return coin_flip_start(play)  #triggering the coin flipping machine if the user say YES! (Note: for outer else statement )

                
def coin_flip(bet_amount,bet_outcome):       #function for user storing each coin flip and total amount of money the player has
    coin_temp = random.randrange(2)          #generating random outcome that is either 0 or 1, representing heads or tails
    global total_money                       #calling global variable, since we dont want to start with the initial fun every time we call the function (because that is cheating haha)
    
    #conditioning for the correct inputs for the amount the player is betting and wether they want to bet on tails or heads
    if bet_amount > total_money:             #No betting the money that you dont have, we dont do leverage here haha
        return ('Nice try... -_- but please enter an amount that is NOT above your current balance. Balance= {}!!').format(total_money)
    elif bet_amount <= 0:                    #Can you even bet negative money? wouldnt it just be the contrapositive? like you win money if you lose and vise versa? haha ANd betting 0 money is no fun :)
        return ('Nice try... -_- but please enter an amount that is NOT zero or negative!!')
    elif bet_outcome != 'Heads' and bet_outcome != 'Tails': #bets can only be put on heads or tails, nothing more! Unless... the coin stands... O_O
        return ('Nice try... -_- but please enter a bet that is either Heads or Tails!!')

    #flipping the coin
    if coin_temp == 0:
        outcome = 'Heads'   # 0 looks like a head, so I set it to represent head haha
    else:
        outcome = 'Tails'   # well, since 0 is head, 1 has to be tails 
    
    #calculating the total money based on the coin flip result
    if bet_outcome == outcome:      
        total_money +=  bet_amount   #this is what we want to see
        return "Congratulations! It is {}, you have won ${}! You now have ${}.".format(outcome,bet_amount,total_money)
    else:        
        total_money -=  bet_amount   #this is NOT what we want to see
        return "Unfortuntealy... It is {}, you have lost ${}. You now have ${}.".format(outcome,bet_amount,total_money)
    
    
play = str(input('Would you like to play coin flip? PLease enter Yes or No: ')) #the question that starts it all... ^_^
print(coin_flip_start(play))  #just calling the function 


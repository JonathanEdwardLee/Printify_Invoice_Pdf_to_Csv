#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from IPython.display import clear_output

def display_board (board):
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[ ]:


#test
test_board = ['#','O','X','O','X','O','X','X','X','X']
display_board(test_board)


# In[ ]:


def player_input():
    #output = (player1_marker,player2_marker)
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player1: Choose X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')    


# In[23]:


#test
player1_marker, player2_marker = player_input()


# In[26]:


def place_marker(board,marker,position):
    
    board[position] = marker


# In[28]:


#test
place_marker(test_board,'&',6)
display_board(test_board)


# In[29]:


def win_check(board,marker):
    return (
    #check rows
    (board[1]==board[2]==board[3]==marker) or
    (board[4]==board[5]==board[6]==marker) or
    (board[7]==board[8]==board[9]==marker) or
    #check column
    (board[1]==board[4]==board[7]==marker) or
    (board[2]==board[5]==board[8]==marker) or
    (board[3]==board[6]==board[9]==marker) or
    #check diagonal
    (board[1]==board[5]==board[9]==marker) or
    (board[7]==board[5]==board[3]==marker))


# In[31]:


#test
win_check(test_board,'X')


# In[32]:


import random #randomly choose who goes first

def choose_first():
    
    flip = random.randint(0,1)
    
    if flip==0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[36]:


def space_check(board,position): #check if position is available to play
    
    return board[position]==' '


# In[37]:


def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[38]:


def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
        return position


# In[39]:


#replay?
def replay():
    
    choice = input('Want to play again? Enter Yes or No ')
    return choice == 'Yes'


# In[40]:


print ("Let's play Tic Tac Toe!")
#while loop to keep running the game
while True:
#set up board,who's first, choose markers
    the_board = [" "]*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn + " will go first")
    
    play_game = input ('Ready to play? y or n ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
##game play
    while game_on:
        
        if turn == 'Player 1':
            #show board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place marker
            place_marker(the_board,player1_marker,position)
            #check for win
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print ("Player 1 has won!!!!!")
                game_on = False
            #check for tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ('You both lose!!!')
                    game_on = False
                else:
                    turn = 'Player 2'
        #Player 2 turn
        else:
            #show board
            display_board(the_board)
            #choose position
            position = player_choice(the_board)
            #place marker
            place_marker(the_board,player2_marker,position)
            #check for win
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print ("Player 2 has won!!!!!")
                game_on = False
            #check for tie
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ('You both lose!!!')
                    game_on = False
                else:
                    turn = 'Player 1'
                   
              
    if not replay():
        break
#break out the loop with replay()


# In[ ]:





#class for the Player 1 and 2
class Player():
        win_counter = 0
        token = "E"
        
        def __init__(self, name, player_number):
            self.name = name
            self.player_number = player_number
        
        #message for start of the game
        def __repr__(self):
            return "{name} is playing as Player {number} with the \"{token}\" token.".format(name=self.name, number=self.player_number, token=self.token)
        
            

        

class Four_In_A_Row():
        #dictionary for the single fields of the game
        # fields[column] = list[rows of that column]
        fields = {}
        for i in range (7):
            fields[i] = list(range(6))

        def __repr__(self):
            return "Welcome to Four In A Row! Let's have some fun in a game with many (4,531,985,219,092) possibilities. Before we can start you need to enter your names and choose a token. "

        #method to create a game field or clear the last for the next game
        def create_clear_game(self):
            for j in range(7):
                for i in range(6):
                    self.fields[j][i] = "-"
            self.print_field()
        
        def print_field(self):
            for i in range(6):
                row = ""
                for j in range(7):
                    row += ("{field}".format(field=self.fields[j][i]))
                    row += "|"
                row = row[:-1]
                print(row)
            print("1 2 3 4 5 6 7")
        
        def edit_field(self, column_number, player_token):
            for i in range(6):
                if self.fields[column_number - 1][-i - 1] == "-":
                    self.fields[column_number - 1][-i - 1] = player_token
                    break
            self.print_field()
        
        #method for the gameplayer
        def gameplay(self):
            #game preparation
            self.create_clear_game()
            print(player1)
            print(player2)
            #start of the game and player inputs
            move = 0
            random_number = 1
            while move < 42:
                move += 1
                if move % 2 == 1:
                    current_player_name = player1.name
                    current_player_token = player1.token
                else:
                    current_player_name = player2.name
                    current_player_token = player2.token
                column_number = int(input("{name} it`s your turn! In which column do you wanna place ur \"{token}\"? ".format(name=current_player_name, token=current_player_token)))
                #check if the column is filled already and infinite loop, if they dont pick an empty column
                while random_number < 10:
                    if self.fields[column_number - 1][0] != "-":
                        column_number = int(input("I'm sorry {name}, but that column is already completely filled. Take another one to place our \"{token}\". ".format(name=current_player_name, token=current_player_token)))
                    else:
                        break
                self.edit_field(column_number, current_player_token)
                #check is somebody won
                possible_win = self.check_win(current_player_name, current_player_token)
                if possible_win == True:
                    break    
            #end of the game and question for a new one
            decision = False
            helping_hand = 1
            if move >= 42:
                answer = input("It's a draw. No one of you won this time. Do you wanna play another game? Write \"Yes\" or \"No\": ")
                if answer == "Yes":
                    decision = True
                elif answer == "No":
                    decision = False
                else:
                    while helping_hand < 10:
                        new_answer = input("I'm sorry I dont understand. Write \"Yes\" or \"No\" please: ")
                        if new_answer == "Yes":
                            decision = True
                            break
                        elif new_answer == "No":
                            decision = False
                            break
            
            else:
                answer = input("Do you wanna play another one? Write \"Yes\" or \"No\": ")
                if answer == "Yes":
                    decision = True
                elif answer == "No":
                    decision = False
                else:
                    while helping_hand < 10:
                        new_answer = input("I'm sorry I dont understand. Write \"Yes\" or \"No\" please: ")
                        if new_answer == "Yes":
                            decision = True
                            break
                        elif new_answer == "No":
                            decision = False
                            break
            if decision == True:
                self.gameplay()


        #method to check for the win
        def check_win(self, player_name, token):
            win = False
            #checking 4 vertical
            for i in range(7):
                #have to be at least 4 same tokens
                if self.fields[i].count(token) >= 4:
                    #two in middle of the column need to be same token
                    if self.fields[i][2] == token and self.fields[i][3] == token:
                        #3 possibilities
                        if self.fields[i][1] == token:
                            if self.fields[i][0] == self.fields[i][1] or self.fields[i][4] == self.fields[i][1]:
                                win = True
                        if self.fields[i][4] == token and self.fields[i][4] == self.fields[i][5]:
                            win = True
            #checking 4 horizontal
            for j in range(6):
                #create list for rows
                for i in range(7):
                    list = []
                    list.append(self.fields[i][j])
                #have to be at least 4 tokens same kind
                if list.count(token) >= 4:
                    #middle of the row need to be the same
                    if list[3] == token:
                        #4 possibilities left
                        if list[2] == token:
                            if list[1] == token:
                                if list[1] == list[0] or list[1] == list[4]:
                                    win = True
                            if list[4] == token and list[5] == token:
                                win = True
                        if list[4] == token and list[5] == token and list [6] == token:
                            win = True
            #checking 4 diagonal
            if self.fields[3][0] == token:
                if self.fields[0][3] == token and self.fields[0][3] == self.fields[1][2] and self.fields[0][3] == self.fields[2][1]:
                    win = True
                if self.fields[4][1] == token and self.fields[4][1] == self.fields[5][2] and self.fields[4][1] == self.fields[6][3]:
                    win = True
            if self.fields[3][5] == token:
                if self.fields[0][2] == token and self.fields[0][2] == self.fields[1][3] and self.fields[0][2] == self.fields[2][4]:
                    win = True
                if self.fields[4][4] == token and self.fields[4][4] == self.fields[5][3] and self.fields[4][4] == self.fields[6][2]:
                    win = True 
            if self.fields[3][1] == token:
                if self.fields[4][2] == token and self.fields[5][3] == token:
                    if self.fields[2][0] == token or self.fields[6][4] == token:
                        win = True
                if self.fields[1][3] == token and self.fields[2][2] == token:
                    if self.fields[4][0] == token or self.fields[0][4] == token:
                        win = True
            if self.fields[3][4] == token:
                if self.fields[1][2] == token and self.fields[2][3] == token:
                    if self.fields[0][1] == token or self.fields[4][5] == token:
                        win = True
                if self.fields[4][3] == token and self.fields[5][2] == token:
                    if self.fields[2][5] == token or self.fields[6][1] == token:
                        win = True   
            if self.fields[3][3] == token:
                if self.fields[2][2] == token:
                    if self.fields[1][1] == token:
                        if self.fields[0][0] == token or self.fields[4][4] == token:
                            win = True
                    if self.fields[4][4] == token and self.fields[5][5] == token:
                        win = True
                if self.fields[4][2] == token:
                    if self.fields[5][1] == token:
                        if self.fields[6][0] == token or self.fields[2][4] == token:
                            win = True
                    if self.fields[2][4] == token and self.fields[1][5] == token:
                        win = True
            if self.fields[3][2] == token:
                if self.fields[4][3] == token:
                    if self.fields[5][4] == token:
                        if self.fields[6][5] == token or self.fields[2][1] == token:
                            win = True
                    if self.fields[2][1] == token and self.fields[1][0] == token:
                        win = True
                if self.fields[2][3] == token:
                    if self.fields[1][4] == token:
                        if self.fields[0][5] == token or self.fields[4][1] == token:
                            win = True
                    if self.fields[4][1] == token and self.fields[5][0] == token:
                        win = True
            if win == True:
                if token == player1.token:
                    player1.win_counter += 1
                    print("Congratulations {name}! You won the game. Your win counter has been increased by one. You now have {win_counter} wins.".format(name=player1.name, win_counter=player1.win_counter))
                if token == player2.token:
                    player2.win_counter += 1
                    print("Congratulations {name}! You won the game. Your win counter has been increased by one. You now have {win_counter} wins.".format(name=player2.name, win_counter=player2.win_counter))
                print("{player1} won {win_counter_player1} times and {player2} won {win_counter_player2} times by now.".format(player1=player1.name, player2=player2.name, win_counter_player1=player1.win_counter, win_counter_player2=player2.win_counter))
            return win
                            

                

             
                


#initialize the game
game = Four_In_A_Row()
print(game)

#player input name and token
player1 = Player(input("Hello there! What is your name Player 1?: "), 1)
player2 = Player(input("Greetings Player 2. What is your name?: "), 2)
token1 = input("{name}. Because you are Player 1, u can decide with which token u want to play. Wanna play as \"X\" or as \"O\"?: ".format(name=player1.name))
while token1 != "X" and token1 != "O":
    token1 = input("I'm sorry Player 1, but u can only play as \"X\" or as \"O\" so please write one of them.: ")
if token1 == "X":
    player2.token = "O"
else:
    player2.token = "X"
player1.token = token1

#game preparation
# game.create_clear_game()
# print(player1)
# print(player2)

#gameplay - player input to place their tokens
# move = 0
# random_number = 1
# while move < 42:
#     move += 1
#     if move % 2 == 1:
#         current_player_name = player1.name
#         current_player_token = player1.token
#     else:
#         current_player_name = player2.name
#         current_player_token = player2.token
#     column_number = int(input("{name} it`s your turn! In which column do you wanna place ur \"{token}\"? ".format(name=current_player_name, token=current_player_token)))
#     #check if the column is filled already and infinite loop, if they dont pick an empty column
#     while random_number < 10:
#         if game.fields[column_number - 1][0] != "-":
#             column_number = int(input("I'm sorry {name}, but that column is already completely filled. Take another one to place our \"{token}\". ".format(name=current_player_name, token=current_player_token)))
#         else:
#             break
#     game.edit_field(column_number, current_player_token)
#     possible_win = game.check_win(current_player_name, current_player_token)
#     if possible_win == True:
#         break
game.gameplay()

#end of the game - question, if players want to play another one
# decision = False
# helping_hand = 1
# if move >= 42:
#     answer = input("It's a draw. No one of you won this time. Do you wanna play another game? Write \"Yes\" or \"No\": ")
#     if answer == "Yes":
#         decision = True
#     elif answer == "No":
#         decision = False
#     else:
#         while helping_hand < 10:
#             new_answer = input("I'm sorry I dont understand. Write \"Yes\" or \"No\" please: ")
#             if new_answer == "Yes":
#                 decision = True
#                 break
#             elif new_answer == "No":
#                 decision = False
#                 break
            
# else:
#     answer = input("Do you wanna play another one? Write \"Yes\" or \"No\": ")
#     if answer == "Yes":
#         decision = True
#     elif answer == "No":
#         decision = False
#     else:
#         while helping_hand < 10:
#             new_answer = input("I'm sorry I dont understand. Write \"Yes\" or \"No\" please: ")
#             if new_answer == "Yes":
#                 decision = True
#                 break
#             elif new_answer == "No":
#                 decision = False
#                 break

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
        
            

        

#method to edit a field on the game
#method to check if somebody won the game
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
        
        def check_win(self, token):
            win = False
            #checking 4 vertical
            for i in range(7):
                #have to be at least 4 same tokens
                if self.fields[i].count(token) >= 4
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
game.create_clear_game()
print(player1)
print(player2)

#gameplay - player input to place their tokens
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
        if game.fields[column_number - 1][0] != "-":
            column_number = int(input("I'm sorry {name}, but that column is already completely filled. Take another one to place our \"{token}\". ".format(name=current_player_name, token=current_player_token)))
        else:
            break
    game.edit_field(column_number, current_player_token)
#game end - Someone won, loose or a draw - Question if players wanna play another game (tracking wins of one player)
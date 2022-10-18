#method to place token
#method to win, loose, or get a draw (track wins of a player)
class Player():
        win_counter = 0
        token = "E"

        def __init__(self, name, player_number):
            self.name = name
            self.player_number = player_number
        
        def __repr__(self):
            return "{name} is playing as Player {number} with the \"{token}\" token.".format(name=self.name, number=self.player_number, token=self.token)
        

#class for the game (fields of the game, columns and rows)
#dictionary for the columns related to the rows, so i dont need 7 or 6 lists
#method to create/clear game field (numerize the columns underneath or above)
#method to edit a field on the game
#method to check if somebody won the game
class Four_In_A_Row():
        fields = {}
        for i in range (7):
            fields[i] = range(6)

        def __repr__(self):
            return "Welcome to Four In A Row! Let's have some fun in a game with many (4,531,985,219,092) possibilities. Before we can start you need to enter your names and choose a token. "

        def create_game(self):
            


#create field
game = Four_In_A_Row()
print(game)

player1 = Player(input("Hello there! What is your name Player 1?: "), 1)
player2 = Player(input("Greetings Player 2. What is your name?: "), 2)
token1 = input("{name}. Because you are Player 1, u can decide with which token u want to play. Wanna play as \"X\" or as \"O\"?: ".format(name=player1.name))
while token1 != ("X" or "O"):
    token1 = input("I'm sorry Player 1, but u can only play as \"X\" or as \"O\" so please write one of them.: ")
if token1 == "X":
    player2.token = "O"
else:
    player2.token = "X"
player1.token = token1
print(player1)
print(player2)

#gameplay - input to place tokens, way of naming the different columns and showing these names, so players know where to place tokens

#game end - Someone won, loose or a draw - Question if players wanna play another game (tracking wins of one player)
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
        

#method to create/clear game field (numerize the columns underneath or above)
#method to edit a field on the game
#method to check if somebody won the game
class Four_In_A_Row():
        fields = {}
        for i in range (6):
            fields[i] = list(range(7))

        def __repr__(self):
            return "Welcome to Four In A Row! Let's have some fun in a game with many (4,531,985,219,092) possibilities. Before we can start you need to enter your names and choose a token. "

        def create_clear_game(self):
            for j in range(6):
                for i in range(7):
                    self.fields[j][i] = "-"
            for j in range(6):
                row = ""
                for i in range(7):
                    row += ("{field}".format(field=self.fields[j][i]))
                    row += "|"
                row = row[:-1]
                print(row)



#initialize the game
game = Four_In_A_Row()
print(game)
#player preparations
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

#gameplay - input to place tokens, way of naming the different columns and showing these names, so players know where to place tokens

#game end - Someone won, loose or a draw - Question if players wanna play another game (tracking wins of one player)
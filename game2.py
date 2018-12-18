
moves = ['rock', 'paper', 'scissors']

import random

#Create player class
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
        
        
#Create random player class
class RandomPlayer:
    def __init__(self):
        Player.__init__(self)
            
    def move(self, RandomPlayerMove):
        
        self.move = RandomPlayerMove
        #use imported random function
        RandomPlayerMove = random.randint(1,3) 
        
        #Computer choice is either rock, paper, or scissors 
        if RandomPlayerMove == ("Rock"): 
            print("The computer choses ROCK") 
        elif RandomPlayerMove == ("Paper"): 
            print("The computer choses PAPER") 
        else: 
            print("The computer choses SCISSORS") 
        
        #return value 
        return RandomPlayerMove 
   
      
        
#Create human player class        
class HumanPlayer:
    def __init__(self):
        Player.__init__(self)
            
    def move(self, HumanMove):
        HumanMove = input("'Rock', 'Paper', or 'Scissors' ")
        #Detect invalid entry
        while HumanMove != 1 and HumanMove != 2 and HumanMove != 3: 
            print ("Choose betwen 'Rock', 'Paper', or 'Scissors' to start the game.")
        return HumanMove
      
        
            
##class that remembers what move the opponent played last round
class ReflectPlayer:
    def __init__(self, ReflectPlayer):
        Player.__init__(self)
        self.ReflectPlayer = ReflectPlayer
    
    # def move 
    def move(self, move):
        self.move = move
        
    def getmove(self, move):
        return self.move
      
            
#define cycleplayer class that remembers what move it played last round,
# and cycles through the different moves. 
class CyclePlayer:
    def __init__(self, CyclePlayer):
        Player.__init__(self)
        self.CyclePlayer = CyclePlayer
        
        self.human_player_history = {}  # stores the frequency of human player moves
        for move in moves:
            self.human_player_history[move] = 0

    def move(self, max_move):
        max_move = max(self.human_player_history.items(), key=lambda elem: elem[1])[0]
        if max_move == 'rock':
            return 'paper'
        if max_move == 'scissors':
            return 'rock'
        if max_move == 'paper':
            return 'rock' 


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

#Create game class
class Game:
    def __init__(self, HumanPlayer, RandomPlayer):
        self.player1 = HumanPlayer
        self.player2 = RandomPlayer
        self.player1_score = 0
        self.player2_score = 0

    def play_round(self, HumanMove, RandomPlayerMove):
            
        move1 = self.player1.move(HumanMove)
        move2 = self.player2.move(RandomPlayerMove)
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.player1.learn(move1, move2)
        self.player2.learn(move2, move1)

        if (move1 == move2):
            print("it's a tie!")
            
        elif beats(move1, move2) is True:
                self.player1_score += 1
        elif beats(move2, move1) is True:
                self.player2_score += 1
                    
        print("It's Tie, Play again!")
        print(f"Scores, HumanPlayer: {self.player1.score} RandomPlayer: {self.player2.score}")
        print("Game over!")
    
    
    def play_game(self, HumanMove, RandomPlayerMove):    
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round(HumanMove, RandomPlayerMove)
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()

   
      
        

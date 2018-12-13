# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:48:39 2018
@author: Jennie
"""

moves = ['rock', 'paper', 'scissors']

import random

RandomPlayerMove = random.randint(1,3)
humanMove = int(input("rock(1), paper(2), or scissors(3): "))


#Create player class
class Player:
        def move(self):
            return 'rock'

        def learn(self, my_move, their_move):
            move1 = self.ComputerPlayer.move()
            move2 = self.ReflectPlayer.move()
            move3 = self.CyclePlayer.move()
            move4 = self.RandomPlayer.move()
            print(f"Player 1: {move1}  Player 2: {move2}")
            self.ComputerPlayer.learn(move1, move2, move3, move4)
            self.ReflectPlayer.learn(move2, move1, move3, move4)
           

#Create random player class
class RandomPlayer:
    def __init__(self):
            Player.__init__(self)
            
    def move():
        #use imported random function
        RandomPlayerMove = random.randint(1,3)
        #Computer choice is either rock, paper, or scissors 
    if RandomPlayerMove == 1: 
        print("The computer choses ROCK") 
    elif RandomPlayerMove == 2: 
        print("The computer choses PAPER") 
    else: 
        print("The computer choses SCISSORS") 
        
      
        
#Create human player class        
class HumanPlayer:
        def __init__(self):
            Player.__init__(self)
      
        #assign input to variable.
        def move():
            humanMove = int(input("rock(1), paper(2), or scissors(3): ")) 
            
        #Detect invalid entry
        while humanMove != 1 and humanMove != 2 and humanMove != 3: 
            
            print('The valid numbers are rock(type 1), paper(type 2),') 
            print('or scissors(type 3).') 
            humanMove = int(input('Enter a valid number please: ')) 

       #assign what the player chose based on entry 
        if humanMove == 1: 
           humanMove = 'ROCK' 
        elif humanMove == 2: 
           humanMove = 'PAPER' 
        else: 
          humanMove = 'SCISSORS' 
        
    
#Define reflect player class
##class that remembers what move the opponent played last round
class ReflectPlayer:
    def __init__(self):
         Player.__init__(self)
    
    #    def move (self): 
    def move(self):
        def __init__(self, move):
            self.move = move
            
        def getmove(self):
            return self.move
      
            
#define cycleplayer class that remembers what move it played last round,
# and cycles through the different moves. 
class CyclePlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.human_player_history = {}  # stores the frequency of human player moves
        for move in moves:
            self.human_player_history[move] = 0

    def move(self):
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
        def __init__(self, ComputerPlayer, ReflectPlayer):
            self.ComputerPlayer = ReflectPlayer
            self.ComputerPlayer = ReflectPlayer

        def play_round(self):
            move1 = self.ComputerPlayer.move()
            move2 = self.ReflectPlayer.move()
            print(f"Player 1: {move1}  Player 2: {move2}")
            self.ComputerPlayer.learn(move1, move2)
            self.ReflectPlayer.learn(move2, move1)
            if beats(move1, move2):
                print("player 1 wins this round")
                self.ComputerPlayer.score += 1
            elif beats(move2, move1):
                print("player 2 wins this round")
                self.ReflectPlayer.score += 1   
            else:
                print("A Tie!")
            print(f"Scores, Player 1: {self.p1.score} Player 2: {self.p2.score}")

        def play_game(self):
            print("Game start!")
            for round in range(3):
                print(f"Round {round}:")
                self.play_round()
            print("Game over!")

            if self.ComputerPlayer.score > self.ReflectPlayer.score:
                print ("Player 1 Wins the Game!")
            elif self.ReflectPlayer.score > self.ComputerPlayer.score:
                print ("Player 2 Wins the Game!")
            else:
                print("a TIE!? it must be settled with a FIGHT TO THE DEATH!")          


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
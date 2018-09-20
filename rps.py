#!/usr/bin/env python3
import random
from termcolor import colored

"""This program plays an expanded version of the game Rock, Paper, Scissors
between two Players, and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors', 'spock', 'lizard']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.their_move = their_move


class HumanPlayer(Player):
    def move(self):
        human_move = input("rock, paper, scissors, spock, lizard? ")
        while human_move not in moves:
            human_move = input("try again: rock, paper, scissors, \
spock, lizard? ")
        return human_move


class RandomPlayer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.their_move = None

    def learn(self, my_move, their_move):
        self.their_move = their_move

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        return self.their_move


class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.my_move = None

    def learn(self, my_move, their_move):
        self.my_move = my_move

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        elif self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'spock'
        elif self.my_move == 'spock':
            return 'lizard'
        elif self.my_move == 'lizard':
            return 'rock'


def beats(one, two):
    return ((one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock') or
            (one == 'rock' and two == 'lizard') or
            (one == 'lizard' and two == 'spock') or
            (one == 'spock' and two == 'scissors') or
            (one == 'scissors' and two == 'lizard') or
            (one == 'lizard' and two == 'paper') or
            (one == 'paper' and two == 'spock') or
            (one == 'spock' and two == 'rock') or
            (one == 'rock' and two == 'scissors'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def single_round(self):
        self.one_round = 1
        print("Sure, we will play 1 round.")

    def multiple_rounds(self):
        self.more_rounds = input("How many rounds do you want to play? ")
        while self.more_rounds == "1":
            self.more_rounds = input("It should be more than one round.\n\
How many rounds do you want to play? ")
        print(f"Okay, we will play {self.more_rounds} rounds.")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played: {move1}. \nComputer played: {move2}.")
        if beats(move1, move2) is True:
            print("You win this round!")
            self.score1 += 1
            print(f"Score: You: {self.score1}, Computer: {self.score2}\n")
        elif beats(move2, move1) is True:
            print("You lose this round!")
            self.score2 += 1
            print(f"Score: You: {self.score1}, Computer: {self.score2}\n")
        else:
            print("It's a tie this round!")
            print(f"Score: You: {self.score1}, Computer: {self.score2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        self.single = input("Do you want to play a single round? [Y/N]: ")
        while self.single not in ["Y", "y", "N", "n"]:
            self.single = input('Please enter either "Y" or "N": ')
        if self.single == "Y" or self.single == "y":
            self.single_round()
            self.total_rounds = self.one_round
        elif self.single == "N" or self.single == "n":
            self.multiple_rounds()
            self.total_rounds = self.more_rounds
        print("\nGame start!")
        for round in range(int(self.total_rounds)):
            print(f"Round {round + 1}:")
            self.play_round()
        print(f"Game over!\
              \nFinal score: You: {self.score1}, Computer: {self.score2}")
        if self.score1 > self.score2:
            print(colored("Yay! YOU WIN!\n", "blue"))
        elif self.score1 < self.score2:
            print(colored("Oh no! YOU LOSE!\n", "red"))
        else:
            print(colored("IT'S A TIE!\n", "green"))


if __name__ == '__main__':
    strategy = input("Which strategy would you like the computer to use?\n\
1. rock, 2. random, 3. imitate, 4. cycle.\n\
Enter a number 1 to 4: ")
    while strategy not in ["1", "2", "3", "4"]:
        strategy = input("Please enter a number between 1 to 4: ")
    if strategy == "1":
        print("The computer will always plays 'rock'.\n")
        game = Game(HumanPlayer(), Player())
        game.play_game()
    elif strategy == "2":
        print("The computer will choose its moves randomly.\n")
        game = Game(HumanPlayer(), RandomPlayer())
        game.play_game()
    elif strategy == "3":
        print("The computer will remember and imitate what you did in the \
previous round,\nexcept for the first round in which it will move randomly.\n")
        game = Game(HumanPlayer(), ReflectPlayer())
        game.play_game()
    elif strategy == "4":
        print("The computer will cycle through all the moves,\n\
except for the first round in which it will move randomly.\n")
        game = Game(HumanPlayer(), CyclePlayer())
        game.play_game()

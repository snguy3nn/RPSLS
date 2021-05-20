from human import Human
from ai import AI


class Game:
    def welcome_message(self):
        print('Welcome to Rock, Paper, Scissor, Lizard, Spock!!!')

    def __init__(self):
        self.player_one = Human()
        self.player_two = AI()

    def choose_second_player(self):
        prompt = input('Press 1 for Single Player or 2 for Multiplayer')
        if prompt == '1':
            self.player_two = AI()
        elif prompt == '2':
            self.player_one = Human()

    def round(self):
        human_choice = self.player_one.choose_gesture()
        ai_choice = self.player_two.choose_gesture()
        if human_choice == '1' and ai_choice == '3':
            print('Rock crushes Scissor!')
        if human_choice == '3' and ai_choice == '2':
            print('Scissor cuts Paper!')
        if human_choice == '2' and ai_choice == '1':
            print('Paper covers Rock')

    def run_game(self):
        self.welcome_message()
        self.choose_second_player()
        self.round()



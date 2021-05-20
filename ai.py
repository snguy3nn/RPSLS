import random
from player import Player


class AI(Player):
    def __init__(self):
        super().__init__()

    def chose_gesture(self):
        self.choose_gesture = random.choice(self.gestures)
        print(f'the computer chose {self.choose_gesture}')
from player import Player


class Human(Player):
    def __init__(self):
        self.name = input('Enter your name!')
        super().__init__()

    def chose_gesture(self):
        self.choose_gesture = input(self.gestures)






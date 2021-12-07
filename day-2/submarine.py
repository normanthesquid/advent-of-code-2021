class Submarine:
    def __init__(self):
        self.x_position = 0
        self.y_position = 0

    def forward(self, amount: int):
        self.x_position += amount

    def up(self, amount: int):
        self.y_position -= amount

    def down(self, amount: int):
        self.y_position += amount

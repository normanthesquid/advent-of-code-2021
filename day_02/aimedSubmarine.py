class Submarine:
    def __init__(self):
        self.aim = 0
        self.x_position = 0
        self.y_position = 0

    def forward(self, amount: int):
        self.x_position += amount
        self.y_position -= amount * self.aim

    def up(self, amount: int):
        self.aim += amount

    def down(self, amount: int):
        self.aim -= amount

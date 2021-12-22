from typing import List


from bingoCardNumber import bingo_card_number


class bingo_card:
    def __init__(self):
        self.rows: List[List[bingo_card_number]] = []
        self.winner: bool = False

    def number_called(self, number: int):
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                if self.rows[i][j].number == number:
                    self.rows[i][j].called = True
                    return

    def check_for_winner(self):
        potential_row_wins = [True, True, True, True, True]
        potential_column_wins = [True, True, True, True, True]

        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):
                if self.rows[i][j].called == False:
                    potential_row_wins[i] = False
                    potential_column_wins[j] = False

        if True in potential_row_wins:
            self.winner = True
        elif True in potential_column_wins:
            self.winner = True
        else:
            self.winner = False
        return self.winner

    def score(self):
        score = 0

        print(f"rows: {len(self.rows)}")
        for i in range(len(self.rows)):
            for j in range(len(self.rows[i])):

                print(
                    f"number: {self.rows[i][j].number} called:  {self.rows[i][j].called}"
                )
                if self.rows[i][j].called == False:
                    score += self.rows[i][j].number
                    print(f"score: {self.rows[i][j].number}")

        return score

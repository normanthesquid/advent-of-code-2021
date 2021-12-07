import os
from typing import List
from bingoCard import bingo_card
from bingoCardNumber import bingo_card_number


def play_bingo():

    calls, cards = read_input()
    winning_card = None

    for i in range(len(calls)):
        for j in range(len(cards)):
            cards[j].number_called(calls[i])
            if cards[j].check_for_winner():
                winning_card = cards[j]
                winning_call = calls[i]
                break
        if winning_card != None:
            break

    print(f"winning_card: {winning_card}")

    card_score = winning_card.score()
    print(f"winning_score: {card_score}")
    print(f"winning_call: {winning_call}")

    print(f"final_score: {card_score * winning_call}")


def read_input():
    cur_path = os.path.dirname(__file__)

    input_path = os.path.join(
        cur_path,
        "input\\input.txt",
    )

    with open(input_path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

    calls = [int(call) for call in lines[0].split(",")]

    cards: List[bingo_card] = []

    for i in range(len(lines) - 1):
        current_line = lines[i + 1]
        if current_line == "":
            current_card = bingo_card()
            cards.append(current_card)
        else:
            card_row = [
                bingo_card_number(int(card_number))
                for card_number in current_line.split()
            ]
            current_card.rows.append(card_row)

    return calls, cards


if __name__ == "__main__":
    play_bingo()

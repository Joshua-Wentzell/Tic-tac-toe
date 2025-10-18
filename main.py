from collections import Counter
from enum import Enum


class CellValue(Enum):
    EMPTY = " "
    PLAYER1 = "X"
    PLAYER2 = "O"


class GameState:
    def __init__(self):
        self.board: list = [[CellValue.EMPTY for _ in range(3)] for _ in range(3)]

    def display(self) -> str:
        display: str = ""
        for row in self.board:
            display += display.join(f"[{cell.value}]" for cell in row)
            display += "\n"
        return display

    def make_move(self, row: int, cell: int, value: CellValue):
        if 0 <= row < len(self.board):
            if 0 <= cell < len(self.board[row]):
                self.board[row][cell] = value
            else:
                raise ValueError("Invalid cell index")
        else:
            raise ValueError("Invalid row index")

    def is_winner(self, player: CellValue) -> bool:
        win_length: int = len(self.board)
        vertical_vals: list = []
        diagonal_count: int = 0
        diagonal_count_2: int = 0
        for i, row in enumerate(self.board):
            reversed_index = win_length - 1 - i
            if all(cell == player for cell in row):
                return True
            for index, cell in enumerate(row):
                if cell.value == player:
                    vertical_vals.append(index)
            if row[i] == player:
                diagonal_count += 1
            if row[reversed_index] == player:
                diagonal_count_2 += 1
        counts = Counter(vertical_vals)
        for _, count in counts.items():
            if count >= win_length:
                return True
        if diagonal_count >= win_length or diagonal_count_2 >= win_length:
            return True
        return False


class ComputerPlayer:
    def __init__(self, game_state):
        self.game_state = game_state

    def make_next_move(self):
        for key, value in self.game_state.board_data.items():
            if value == CellValue.EMPTY:
                self.game_state.make_move(key, CellValue.PLAYER2)
                break


class HumanPlayer:
    def __init__(self, game_state):
        self.game_state = game_state

    def make_next_move(self):
        cell = input("Please enter the cell you would like to play on: ")
        if cell in self.game_state.board_data.keys():
            self.game_state.make_move(cell, CellValue.PLAYER1)


new_game = GameState()
print("New game started")
print(new_game)
human_player = HumanPlayer(new_game)
computer_player = ComputerPlayer(new_game)
while new_game.check_winner() == "":
    human_player.make_next_move()
    print(new_game)
    print("Computer is moving")
    computer_player.make_next_move()
    print(new_game)
print(f"Game over, result: {new_game.check_winner()}")

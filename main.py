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
            for cell in row:
                display += f"[{cell.value}]"
            display += "\n"
        return display

    def get_board(self) -> list:
        return self.board

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
                if cell == player:
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
        board = self.game_state.get_board()
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if board[i][j] == CellValue.EMPTY:
                    self.game_state.make_move(i, j, CellValue.PLAYER2)
                    return


class HumanPlayer:
    def __init__(self, game_state):
        self.game_state = game_state

    def make_next_move(self):
        cell = input(
            "Please enter the cell you would like to play on in the col,row format: "
        )
        col, row = cell.split(",")
        row = int(row)
        col = int(col)
        self.game_state.make_move(col, row, CellValue.PLAYER1)


class Game:
    def __init__(self):
        self.game_state = GameState()

    def play(self):
        print("New game started")
        print(self.game_state.display())
        human_player = HumanPlayer(self.game_state)
        computer_player = ComputerPlayer(self.game_state)
        while True:
            human_player.make_next_move()
            print(self.game_state.display())
            human_winner = self.game_state.is_winner(CellValue.PLAYER1)
            if human_winner:
                break
            _ = input("Press enter to continue...")
            print("Computer is moving")
            computer_player.make_next_move()
            print(self.game_state.display())
            computer_winner = self.game_state.is_winner(CellValue.PLAYER2)
            if computer_winner:
                break
        print(f"Game over, winner: {"Player" if human_winner else "Computer"}")


def main():
    game = Game()
    game.play()
    while input("Would you like to play again? (y/n) ") == "y":
        game = Game()
        game.play()

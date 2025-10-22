from copy import deepcopy
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
        return deepcopy(self.board)

    def make_move(self, row: int, cell: int, value: CellValue):
        if value == CellValue.EMPTY:
            raise ValueError("Cannot assign an empty value")
        if 0 <= row < len(self.board):
            if 0 <= cell < len(self.board[row]):
                if self.board[row][cell] != CellValue.EMPTY:
                    raise ValueError(f"Cell {cell} already occupied")
                self.board[row][cell] = value
            else:
                raise ValueError("Invalid cell index")
        else:
            raise ValueError("Invalid row index")


class ComputerPlayer:
    def __init__(self, game_state):
        self.game_state = game_state

    def make_next_move(self):
        board = self.game_state.get_board()
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[i]):
                if board[i][j] == CellValue.EMPTY:
                    try:
                        self.game_state.make_move(i, j, CellValue.PLAYER2)
                    except Exception as e:
                        print(e)
                    return


class HumanPlayer:
    def __init__(self, game_state):
        self.game_state = game_state

    def make_next_move(self):
        cell = input(
            "Please enter the cell you would like to play on in the row,col format: "
        )
        try:
            row, col = cell.split(",")
            row = int(row) - 1
            col = int(col) - 1
            self.game_state.make_move(row, col, CellValue.PLAYER1)
        except Exception as e:
            print(e)


class Game:
    def __init__(self):
        self.game_state = GameState()

    def is_winner(self, player: CellValue) -> bool:
        board = self.game_state.get_board()
        win_length: int = len(board)
        diagonal_count: int = 0
        diagonal_count_2: int = 0
        for col in range(0, win_length):
            if all(board[row][col] == player for row in range(0, win_length)):
                return True
        for i, row in enumerate(board):
            reversed_index = win_length - 1 - i
            if all(cell == player for cell in row):
                return True
            if row[i] == player:
                diagonal_count += 1
            if row[reversed_index] == player:
                diagonal_count_2 += 1
        if diagonal_count >= win_length or diagonal_count_2 >= win_length:
            return True
        return False

    def play(self):
        print("New game started")
        print(self.game_state.display())
        human_player = HumanPlayer(self.game_state)
        computer_player = ComputerPlayer(self.game_state)
        while True:
            human_player.make_next_move()
            print(self.game_state.display())
            human_winner = self.is_winner(CellValue.PLAYER1)
            if human_winner:
                break
            _ = input("Press enter to continue...")
            print("Computer is moving")
            computer_player.make_next_move()
            print(self.game_state.display())
            computer_winner = self.is_winner(CellValue.PLAYER2)
            if computer_winner:
                break
        print(f"Game over, winner: {"Player" if human_winner else "Computer"}")


if __name__ == "__main__":
    game = Game()
    game.play()
    while input("Would you like to play again? (y/n) ") == "y":
        game = Game()
        game.play()

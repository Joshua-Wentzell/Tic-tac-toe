from enum import Enum


class CellValue(Enum):
    EMPTY = 1
    PLAYER1 = 2
    PLAYER2 = 3


class GameState:
    def __init__(self):
        self.board_data = {
            "A1": CellValue.EMPTY,
            "A2": CellValue.EMPTY,
            "A3": CellValue.EMPTY,
            "B1": CellValue.EMPTY,
            "B2": CellValue.EMPTY,
            "B3": CellValue.EMPTY,
            "C1": CellValue.EMPTY,
            "C2": CellValue.EMPTY,
            "C3": CellValue.EMPTY,
        }

    def __repr__(self):
        data_string = ""
        sorted_data = sorted(self.board_data.items(), key=lambda item: item[0])
        last_row_letter = ""
        for data_point in sorted_data:
            if last_row_letter == "":
                last_row_letter = data_point[0][0]
            elif last_row_letter != data_point[0][0]:
                data_string += "\n"
                last_row_letter = data_point[0][0]
            value = " "
            match data_point[1]:
                case CellValue.EMPTY:
                    value = " "
                case CellValue.PLAYER1:
                    value = "X"
                case CellValue.PLAYER2:
                    value = "O"
            data_string += f"[{value}]"
        return data_string

    def make_move(self, cell, value):
        if cell in self.board_data.keys():
            self.board_data[cell] = value


new_game = GameState()
print(new_game)
new_game.make_move("B2", CellValue.PLAYER1)
print(new_game)
new_game.make_move("C1", CellValue.PLAYER2)
print(new_game)

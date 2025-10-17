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

    def check_winner(self):
        WIN_COUNT = 3
        horiz_sorted_data = sorted(self.board_data.items(), key=lambda item: item[0])
        vert_sorted_data = sorted(self.board_data.items(), key=lambda item: item[0][1])
        last_row_letter = ""
        last_col_number = ""
        current_hor_count_p1 = 0
        current_hor_count_p2 = 0
        current_ver_count_p1 = 0
        current_ver_count_p2 = 0
        current_diag_count_p1 = 0
        current_diag_count_p2 = 0
        p1_wins = False
        p2_wins = False
        for data_point in horiz_sorted_data:
            if last_row_letter == "":
                last_row_letter = data_point[0][0]
            if last_row_letter != data_point[0][0]:
                current_hor_count_p1 = 0
                current_hor_count_p2 = 0
                last_row_letter = data_point[0][0]
            if data_point[1] == CellValue.PLAYER1:
                current_hor_count_p1 += 1
            if data_point[1] == CellValue.PLAYER2:
                current_hor_count_p2 += 1
            if current_hor_count_p1 >= WIN_COUNT:
                p1_wins = True
            if current_hor_count_p2 >= WIN_COUNT:
                p2_wins = True

        for data_point in vert_sorted_data:
            if last_col_number == "":
                last_col_number = data_point[0][1]
            if last_col_number != data_point[0][1]:
                current_ver_count_p1 = 0
                current_ver_count_p2 = 0
                last_col_number = data_point[0][1]
            if data_point[1] == CellValue.PLAYER1:
                current_ver_count_p1 += 1
            if data_point[1] == CellValue.PLAYER2:
                current_ver_count_p2 += 1
            if current_ver_count_p1 >= WIN_COUNT:
                p1_wins = True
            if current_ver_count_p2 >= WIN_COUNT:
                p2_wins = True

        vertical_offset = 0
        for i in range(1, WIN_COUNT + 1):
            if i > 1:
                vertical_offset += 1
            strt_lett = "A"
            strt_lett = chr(ord(strt_lett) + vertical_offset)
            index = str(strt_lett) + str(i)
            if self.board_data[index] == CellValue.PLAYER1:
                current_diag_count_p1 += 1
            if self.board_data[index] == CellValue.PLAYER2:
                current_diag_count_p2 += 1
            if current_diag_count_p1 >= WIN_COUNT:
                p1_wins = True
            if current_diag_count_p2 >= WIN_COUNT:
                p2_wins = True

        current_diag_count_p1 = 0
        current_diag_count_p2 = 0

        vertical_offset = 0
        for i in range(WIN_COUNT, 0, -1):
            if i < WIN_COUNT:
                vertical_offset += 1
            strt_lett = "A"
            strt_lett = chr(ord(strt_lett) + vertical_offset)
            index = str(strt_lett) + str(i)
            if self.board_data[index] == CellValue.PLAYER1:
                current_diag_count_p1 += 1
            if self.board_data[index] == CellValue.PLAYER2:
                current_diag_count_p2 += 1
            if current_diag_count_p1 >= WIN_COUNT:
                p1_wins = True
            if current_diag_count_p2 >= WIN_COUNT:
                p2_wins = True

        if p1_wins and p2_wins:
            return "Tie"
        elif p1_wins:
            return "Player 1"
        elif p2_wins:
            return "Player 2"
        if CellValue.EMPTY not in self.board_data.values():
            return "Tie"
        return ""


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

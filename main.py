class GameState:
    def __init__(self):
        self.board_data = {
            "A1": False,
            "A2": False,
            "A3": False,
            "B1": False,
            "B2": False,
            "B3": False,
            "C1": False,
            "C2": False,
            "C3": False
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
            if data_point[1] == True:
                value = "X"
            data_string += f"[{value}]"
        return data_string

new_game = GameState()
print(new_game)

import flet as ft


class DropDownControl(ft.Dropdown):
    def __init__(self):
        super().__init__()
        self.width = 280
        self.label = "Выберите кол-во игроков"
        self.options = [
            ft.dropdownm2.Option("5"),
            ft.dropdownm2.Option("6"),
            ft.dropdownm2.Option("7"),
            ft.dropdownm2.Option("8"),
            ft.dropdownm2.Option("9"),
            ft.dropdownm2.Option("10"),
        ]
        # self.on_change = self.on_change_handler

    def on_change_handler(self, e):
        pass



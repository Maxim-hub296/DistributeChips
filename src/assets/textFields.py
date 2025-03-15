import flet as ft

class ChipsTextfield(ft.TextField):
    def __init__(self, n_chips: int):
        super().__init__()
        self.width = 280
        self.input_filter = ft.InputFilter(allow=True, regex_string=r"^[0-9]*$", replacement_string="")
        self.price = n_chips
        self.label = f"Введите кол-во фишек номиналом {self.price}"



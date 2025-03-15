import flet as ft

from assets.dropdown import DropDownControl
from assets.textFields import ChipsTextfield


class CalculateButton(ft.FilledButton):
    def __init__(self, chips1: ChipsTextfield, chips5: ChipsTextfield, chips10: ChipsTextfield,
                 chips25: ChipsTextfield, chips50: ChipsTextfield, chips100: ChipsTextfield,
                 dropdown: DropDownControl):
        super().__init__()
        self.chips1 = chips1
        self.chips5 = chips5
        self.chips10 = chips10
        self.chips25 = chips25
        self.chips50 = chips50
        self.chips100 = chips100
        self.amount_of_players = dropdown

        self.dlg = ft.AlertDialog()

        self.width = 280
        self.text = "Рассчитать!"

        self.on_click = self.on_click_handler

    def on_click_handler(self, e):
        amount_of_chips1 = int(self.chips1.value) // int(self.amount_of_players.value)
        amount_of_chips5 = int(self.chips5.value) // int(self.amount_of_players.value)
        amount_of_chips10 = int(self.chips10.value) // int(self.amount_of_players.value)
        amount_of_chips25 = int(self.chips25.value) // int(self.amount_of_players.value)
        amount_of_chips50 = int(self.chips50.value) // int(self.amount_of_players.value)
        amount_of_chips100 = int(self.chips100.value) // int(self.amount_of_players.value)

        j = int(self.amount_of_players.value)
        remainders = {
            100: int(self.chips100.value) % j,
            50: int(self.chips50.value) % j,
            25: int(self.chips25.value) % j,
            10: int(self.chips10.value) % j,
            5: int(self.chips5.value) % j,
            1: int(self.chips1.value) % j
        }

        players = [
            {
                "chips1": amount_of_chips1,
                "chips5": amount_of_chips5,
                "chips10": amount_of_chips10,
                "chips25": amount_of_chips25,
                "chips50": amount_of_chips50,
                "chips100": amount_of_chips100,
                "total": (
                        amount_of_chips1 * 1 +
                        amount_of_chips5 * 5 +
                        amount_of_chips10 * 10 +
                        amount_of_chips25 * 25 +
                        amount_of_chips50 * 50 +
                        amount_of_chips100 * 100
                )
            }
            for _ in range(j)
        ]

        for denom in [100, 50, 25, 10, 5, 1]:
            for _ in range(remainders[denom]):
                min_total = min(p["total"] for p in players)
                recipient_idx = next(i for i, p in enumerate(players) if p["total"] == min_total)
                players[recipient_idx][f"chips{denom}"] += 1
                players[recipient_idx]["total"] += denom





        dialogs_texts = [f"Фишек номиналом 1: {players[0]["chips1"]}", f"Фишек номиналом 5: {players[0]['chips5']}",
                         f"Фишек номиналом 10: {players[0]['chips10']}", f"Фишек номиналом 25: {players[0]['chips25']}",
                         f"Фишек номиналом 50: {players[0]['chips50']}", f"Фишек номиналом 100: {players[0]['chips100']}"]

        self.dlg.content = ft.Column(controls=[ft.Text(value=dialogs_texts[0]),
                                               ft.Text(value=dialogs_texts[1]),
                                               ft.Text(value=dialogs_texts[2]),
                                               ft.Text(value=dialogs_texts[3]),
                                               ft.Text(value=dialogs_texts[4]),
                                               ft.Text(value=dialogs_texts[5])], height=250)





        self.dlg.actions = [ft.TextButton("Закрыть", on_click=lambda e: self.page.close(self.dlg))]
        self.dlg.shape = ft.RoundedRectangleBorder(radius=7)
        self.page.open(self.dlg)

        self.page.update()
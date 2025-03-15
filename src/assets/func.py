from assets.dropdown import DropDownControl
from assets.textFields import *
from assets.buttons import CalculateButton

def get_control() -> ft.Column:
    dropdown_control = DropDownControl()

    chip1_text_field = ChipsTextfield(1)
    chip5_text_field = ChipsTextfield(5)
    chip10_text_field = ChipsTextfield(10)
    chip25_text_field = ChipsTextfield(25)
    chip50_text_field = ChipsTextfield(50)
    chip100_text_field = ChipsTextfield(100)

    calculate_button = CalculateButton(chip1_text_field, chip5_text_field, chip10_text_field, chip25_text_field,
                                       chip50_text_field, chip100_text_field, dropdown_control)


    column = ft.Column(controls=[dropdown_control,
                                 chip1_text_field, chip5_text_field, chip10_text_field,
                                 chip25_text_field, chip50_text_field, chip100_text_field,
                                 calculate_button], alignment=ft.MainAxisAlignment.CENTER)
    return column



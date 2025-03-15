import flet as ft

from assets.func import get_control


def main(page: ft.Page):
    page.window.height = 627
    page.window.width = 505

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    controls = get_control()
    page.add(controls)

    page.update()


ft.app(main)

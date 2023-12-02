import flet as ft


def ask_for_name():
    name_input = ft.TextField(
        label="Your name?",
        width=500,
        height=200,
        multiline=False,
        border_radius=8
    )
    name_button = ft.ElevatedButton(
        text="Log in",
        color="#00008B",
        width=150,
        height=50,
        elevation=15,
        on_click=lambda e: login(name_input, name_container)
    )
    name_row = ft.Row([name_input, name_button], alignment=ft.MainAxisAlignment.CENTER)
    name_container = ft.Container(
        height=50,
        padding=ft.Padding(0, 0, 0, 0),
        content=name_row,
    )
    return name_input, name_container


user_input = ft.TextField(
    label="Enter user",
    width=500,
    height=200,
    multiline=True,
    max_lines=6,
    min_lines=6,
    border_radius=8
)

gpt_output = ft.TextField(
    label="Output GPT",
    color="#4682B4",
    multiline=True,
    max_lines=15,
    min_lines=15,
    border_radius=10,
    width=500,
    height=400
)


def create_user_input_row():
    card = ft.Card(
        elevation=10,
        color="#C6E2FF",
        width=700,
        height=200
    )
    return ft.Row([card], alignment=ft.MainAxisAlignment.CENTER)


def create_gpt_output_row():
    card = ft.Card(
        elevation=10,
        color="#9FB6CD",
        width=700,
        height=300
    )
    return ft.Row([card], alignment=ft.MainAxisAlignment.CENTER)


def login(name_input, name_container):
    if name_input.value:
        name_container.hidden = True
        user_input.hidden = False
        gpt_output.hidden = False
    else:
        name_input.error_message = "Please, enter your name"


name_input, name_container = ask_for_name()
name_container.hidden = False


def main(page: ft.Page):
    page.title = "FletGpt"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bg_color = "#00008B"
    page.window_maximized = True

    user_input_row = create_user_input_row()

    def click_button():
        gpt_output.value = f"Mock GPT response for: {user_input.value}"
        gpt_output.update()
        page.update()

    send_button = ft.ElevatedButton(
        text="Send",
        color="#00008B",
        width=170,
        height=60,
        elevation=15,
        on_click=click_button
    )
    button_row = ft.Row([send_button], alignment=ft.MainAxisAlignment.CENTER)
    button_container = ft.Container(
        height=100,
        padding=ft.Padding(0, 0, 0, 0),
        content=button_row,
    )

    gpt_output_row = create_gpt_output_row()

    column = ft.Column(
        [name_container, user_input_row, button_container, gpt_output_row],
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    page.add(column)


ft.app(target=main)

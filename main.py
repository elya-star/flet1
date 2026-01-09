import flet as ft
import datetime as dt

def main(page: ft.Page):
    text_hello = ft.Text(value="Hello World!", color=ft.Colors.GREEN_200)

    def on_button_click(_):
        page.title = "Моё первое приложение"
        page.theme_mode = ft.ThemeMode.LIGHT
        name = name_input.value.strip()
        print(name)
        if name:
            now = dt.datetime.now()
            time_str = now.strftime("%Y:%m:%d - %H:%M:%S")
            text_hello.color = None
            text_hello.value = f"{time_str} - Hello, {name}"
            name_input.value = ''
        else:
            text_hello.value = "Введите корректное имя" 
            text_hello.color = ft.Colors.RED_200
        page.update()


    eleveted_button = ft.ElevatedButton("SEND", icon=ft.Icons.SEND, on_click=on_button_click)
    name_input = ft.TextField(label='Введите имя', on_submit=on_button_click)

    page.add(text_hello, name_input, eleveted_button,)

ft.run(main, view=ft.AppView.WEB_BROWSER, port=8550)
    


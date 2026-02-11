import flet as ft

def app(page: ft.Page):
    page.title = "Изобранные"

    favorites = []
    last_name = ""

    plain_text = ft.Text(value="Hello ")
    favorites_text = ft.Text(value="Избранные:")

    def change(e):
        nonlocal last_name
        txt = user_input.value.strip()
        user_input.value = ""

        if txt:
            last_name = txt
            plain_text.value = f"Hello, {last_name}!"
            page.update()

    def add_to_favorites(e):
        txt = user_input.value.strip()

        if txt and txt not in favorites:
            favorites.append(txt)
            favorites_text.value = "Избранные:\n" + "\n".join(favorites)
            user_input.value = ""
            page.update()

    user_input = ft.TextField(label="Enter name", on_submit=change)
    btn = ft.TextButton("Отправить", on_click=change)
    fav_button = ft.TextButton("Добавить в избранные", on_click=add_to_favorites)

    page.add(plain_text, user_input, btn, fav_button, favorites_text)

ft.app(app)


#2 misson

import flet as ft

def app(page: ft.Page):
    plain_text = ft.Text(value="Hello world!")
    history = []

    def clear_history(e):
        history.clear()
        history_text.value = ""

    history_text = ft.Text()


    def change(e):
        txt = user_input.value.strip()
        user_input.value = ""
        history.append(txt)
        print(history)
        history_text.value = "История имён: \n" + ", \n".join(history)
        page.update()


    btn = ft.TextButton("Отправить", on_click=change)
    user_input = ft.TextField(label="Enter name", on_submit=change)

    page.add(plain_text, user_input, btn, history_text)


ft.app(app)

import flet as ft
import consulta_airtable as cat             # Consulta desde Airtable
import CONSULTA_CON_SQLITE as csql              # Nueva consulta desde SQLite

def main(page: ft.Page):

    def mostrar_interacciones(e: ft.ControlEvent):
        page.clean()
        cat.main(page)

    def mostrar_sqlite(e: ft.ControlEvent):
        page.clean()
        csql.main(page)

    page.title = "FARMI-UJAT"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT", size=40),
        center_title=True
    )

    # Botón para interacciones desde Airtable
    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication", size=40, color="black"),
                    ft.Text("Interacciones medicamentosas", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "orange")
        ),
        bgcolor="orange100",
        color="black",
        width=200,
        on_click=mostrar_interacciones
    )

    # Botón para consulta desde SQLite
    btn_sqlite = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("search", size=40, color="black"),
                    ft.Text("Consulta SQLite", text_align=ft.TextAlign.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=ft.BorderSide(1, "green")
        ),
        bgcolor="green100",
        color="black",
        width=200,
        on_click=mostrar_sqlite
    )

    # Mostrar los botones en una fila centrada
    page.add(ft.Divider(color="black"))
    page.add(ft.Row([btn_interacciones, btn_sqlite], alignment=ft.MainAxisAlignment.CENTER))
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)

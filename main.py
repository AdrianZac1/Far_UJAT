import flet as ft
import consulta_airtable as cat

def main(page: ft.Page):

    def mostrar_interacciones(e: ft.ControlEvent):
        page.clean()
        cat.main(page)
        

    page.title = "FARMI-UJAT"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT", size=40),
        center_title=True
    )
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
    page.add( ft.Divider(color="black") )
    page.add(btn_interacciones)
    page.update()


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
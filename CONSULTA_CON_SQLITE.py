import flet as ft
from MODELOSQLITE import Medicamento  # Cambiado para usar el modelo correcto

def obtener_medicamentos(nombre=""):
    """Consulta los medicamentos en la base de datos filtrando por nombre."""
    if nombre:
        query = Medicamento.select().where(Medicamento.nombre_farmaco.contains(nombre))
    else:
        query = Medicamento.select()
    return list(query)

def main(page: ft.Page):
    page.title = "Consulta de Medicamentos"
    page.bgcolor = ft.colors.WHITE

    def buscar_medicamento(e):
        query = e.control.value.lower()
        data_table.rows.clear()
        resultados = obtener_medicamentos(query)

        for med in resultados:
            data_table.rows.append(ft.DataRow(cells=[
                ft.DataCell(ft.Text(med.descripcion, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)),
                ft.DataCell(ft.Text(med.presentacion, color=ft.colors.BLACK)),
                ft.DataCell(ft.Text(med.clasificacion, italic=True, color=ft.colors.BLACK)),
                ft.DataCell(ft.Text(med.nivel_atencion, color=ft.colors.BLACK)),
                ft.DataCell(ft.Text(med.nombre_farmaco.nombre, color=ft.colors.PINK)),
            ]))
        page.update()

    search_box = ft.TextField(
        label="Ingrese el nombre del medicamento",
        color=ft.colors.BLACK,
        on_change=buscar_medicamento
    )

    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Descripción", weight=ft.FontWeight.BOLD, color=ft.colors.BLACK)),
            ft.DataColumn(ft.Text("Presentación", width=200, color=ft.colors.BLACK)),
            ft.DataColumn(ft.Text("Clasificación", italic=True, width=200, color=ft.colors.BLACK)),
            ft.DataColumn(ft.Text("Nivel de Atención", width=100, color=ft.colors.BLACK)),
            ft.DataColumn(ft.Text("Nombre Medicamento", width=100, color=ft.colors.PINK)),
        ],
        rows=[]
    )

    page.add(search_box, data_table)

ft.app(target=main)

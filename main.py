# ==============================================================================
# PROYECTO: TodoAppBasic1.2
# LENGUAJE: Python con Librería Flet (GUI Moderna)
# ==============================================================================
# Este programa traslada la misma lógica básica de listas (tareas = [])
# hacia una aplicación gráfica interactiva y visual usando Flet.
# ==============================================================================

import flet as ft

def main(page: ft.Page):
    # --------------------------------------------------------------------------
    # 1. CONFIGURACIÓN GENERAL DE LA VENTANA
    # --------------------------------------------------------------------------
    page.title = "TodoAppBasic1.2"
    page.window.width = 460
    page.window.height = 680
    page.window.resizable = False
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 24
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # --------------------------------------------------------------------------
    # 2. ESTADO DE LA APLICACIÓN (Igual que en la versión de consola)
    # --------------------------------------------------------------------------
    # Creamos una lista vacía para almacenar las tareas en memoria
    tareas = []

    # --------------------------------------------------------------------------
    # 3. CONTROLES VISUALES DE ENTRADA
    # --------------------------------------------------------------------------
    input_tarea = ft.TextField(
        hint_text="¿Qué tarea tienes pendiente?",
        expand=True,
        border_radius=10,
        autofocus=True,
    )

    mensaje_error = ft.Text(
        value="",
        color=ft.Colors.RED_500,
        size=12,
        weight=ft.FontWeight.W_500,
    )

    texto_contador = ft.Text(
        value="0 tareas pendientes",
        color=ft.Colors.GREY_700,
        size=13,
        weight=ft.FontWeight.BOLD,
    )

    # --------------------------------------------------------------------------
    # 4. CONTENEDOR DE LA LISTA Y ESTADO VACÍO
    # --------------------------------------------------------------------------
    lista_tareas = ft.ListView(
        expand=True,
        spacing=8,
    )

    estado_vacio = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(icon=ft.Icons.CHECK_CIRCLE_OUTLINE_ROUNDED, size=52, color=ft.Colors.BLUE_400),
                ft.Text("¡No tienes tareas pendientes!", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_800),
                ft.Text("Escribe una tarea arriba y presiona Agregar", size=13, color=ft.Colors.GREY_600),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=6,
        ),
        alignment=ft.Alignment.CENTER,
        padding=40,
        visible=True,
    )

    # --------------------------------------------------------------------------
    # 5. FUNCIÓN: actualizar_vista() (Equivalente a la OPCIÓN 1 de la consola)
    # --------------------------------------------------------------------------
    def actualizar_vista():
        # Limpiamos los controles visuales de la lista
        lista_tareas.controls.clear()

        # EQUIVALENTE A: if len(tareas) == 0:
        if len(tareas) == 0:
            estado_vacio.visible = True
            btn_limpiar.visible = False
            texto_contador.value = "0 tareas pendientes"
        else:
            estado_vacio.visible = False
            btn_limpiar.visible = True
            cantidad = len(tareas)
            texto_contador.value = "1 tarea pendiente" if cantidad == 1 else f"{cantidad} tareas pendientes"

            # EQUIVALENTE AL BUCLE: for tarea in tareas:
            for indice, tarea in enumerate(tareas):
                numero = indice + 1  # Numeración natural empezando en 1

                # Creamos una tarjeta gráfica para cada tarea
                tarjeta_tarea = ft.Container(
                    content=ft.Row(
                        controls=[
                            # Círculo con el número de tarea
                            ft.Container(
                                content=ft.Text(
                                    str(numero),
                                    color=ft.Colors.BLUE_700,
                                    weight=ft.FontWeight.BOLD,
                                    size=12,
                                ),
                                width=28,
                                height=28,
                                border_radius=14,
                                bgcolor=ft.Colors.BLUE_50,
                                border=ft.Border.all(1, ft.Colors.BLUE_200),
                                alignment=ft.Alignment.CENTER,
                            ),
                            # Texto de la tarea
                            ft.Text(
                                tarea,
                                size=14,
                                color=ft.Colors.BLUE_GREY_900,
                                expand=True,
                            ),
                            # Botón para eliminar (Equivalente a la opción 3)
                            ft.IconButton(
                                icon=ft.Icons.DELETE_OUTLINE_ROUNDED,
                                icon_color=ft.Colors.RED_400,
                                tooltip="Eliminar tarea",
                                on_click=lambda e, i=indice: eliminar_tarea(i),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    ),
                    padding=10,
                    border=ft.Border.all(1, ft.Colors.GREY_300),
                    border_radius=10,
                    bgcolor=ft.Colors.WHITE,
                )
                lista_tareas.controls.append(tarjeta_tarea)

        # Refrescamos la página visual de Flet
        page.update()

    # --------------------------------------------------------------------------
    # 6. FUNCIÓN: agregar_tarea(e) (Equivalente a la OPCIÓN 2 de la consola)
    # --------------------------------------------------------------------------
    def agregar_tarea(e):
        # Obtenemos el texto y removemos espacios en blanco (.strip())
        texto = input_tarea.value.strip()

        # Validamos que no esté vacío
        if texto == "":
            mensaje_error.value = "⚠️ Por favor, escribe una tarea antes de agregar."
            page.update()
            return

        # Limpiamos el mensaje de error si era válido
        mensaje_error.value = ""

        # EQUIVALENTE A: tareas.append(nueva_tarea)
        tareas.append(texto)

        # Limpiamos el campo de texto y devolvemos el foco
        input_tarea.value = ""
        input_tarea.focus()

        # Actualizamos la interfaz gráfica
        actualizar_vista()

    # --------------------------------------------------------------------------
    # 7. FUNCIÓN: eliminar_tarea(indice) (Equivalente a la OPCIÓN 3 de la consola)
    # --------------------------------------------------------------------------
    def eliminar_tarea(indice: int):
        # EQUIVALENTE A: if 0 <= indice < len(tareas): tareas.pop(indice)
        if 0 <= indice < len(tareas):
            tareas.pop(indice)
            actualizar_vista()

    # --------------------------------------------------------------------------
    # 8. FUNCIÓN: limpiar_todo(e)
    # --------------------------------------------------------------------------
    def limpiar_todo(e):
        tareas.clear()
        actualizar_vista()

    # Botón para agregar tarea
    btn_agregar = ft.IconButton(
        icon=ft.Icons.ADD_CIRCLE,
        icon_color=ft.Colors.BLUE_600,
        icon_size=38,
        tooltip="Agregar tarea",
        on_click=agregar_tarea,
    )

    # Permitir agregar tarea pulsando Enter en el teclado
    input_tarea.on_submit = agregar_tarea

    # Botón para limpiar todas las tareas
    btn_limpiar = ft.TextButton(
        "Limpiar todo",
        icon=ft.Icons.DELETE_SWEEP_ROUNDED,
        icon_color=ft.Colors.RED_400,
        on_click=limpiar_todo,
        visible=False,
    )

    # --------------------------------------------------------------------------
    # 9. CONSTRUCCIÓN DEL DISEÑO DE LA PÁGINA
    # --------------------------------------------------------------------------
    encabezado = ft.Column(
        controls=[
            ft.Text("📝 TodoAppBasic1.2", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_GREY_900),
            ft.Text("Lista de tareas visual desarrollada en Python", size=13, color=ft.Colors.GREY_600),
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=4,
    )

    fila_entrada = ft.Row(
        controls=[input_tarea, btn_agregar],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    barra_estado = ft.Row(
        controls=[texto_contador, btn_limpiar],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # Agrupamos los componentes dentro de un SafeArea para proteger la barra de estado y la cámara del celular
    contenido_principal = ft.Column(
        controls=[
            ft.Container(height=12),  # Espaciado superior para que no quede pegado arriba
            encabezado,
            ft.Divider(height=16, color=ft.Colors.TRANSPARENT),
            fila_entrada,
            mensaje_error,
            barra_estado,
            ft.Divider(height=10, color=ft.Colors.GREY_300),
            estado_vacio,
            lista_tareas,
        ],
        expand=True,
    )

    # Agregamos el contenido protegido a la página
    page.add(
        ft.SafeArea(
            content=contenido_principal,
            expand=True,
        )
    )

    # Dibujamos el estado inicial
    actualizar_vista()

# ------------------------------------------------------------------------------
# 10. EJECUCIÓN DE LA APLICACIÓN
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    ft.run(main)

# TodoAppBasic1.2

Una aplicación gráfica de escritorio y web moderna, reactiva y elegante para gestionar listas de tareas, desarrollada **100% en Python** utilizando la librería **Flet**. 

Este proyecto toma como base la lógica algorítmica fundamental de una lista de tareas por consola (`todo.py`) y la eleva a una experiencia visual interactiva completa sin abandonar el lenguaje Python.

---

##  ¿Para qué sirve TodoAppBasic1.2?

* **Gestión de tareas pendientes:** Permite anotar, organizar y dar seguimiento a tus deberes cotidianos en una interfaz limpia y atractiva.
* **Visualización ordenada:** Presenta las tareas enumeradas cronológicamente con insignias numéricas claras (1, 2, 3...).
* **Eliminación instantánea:** Permite descartar tareas completadas con un solo clic sobre el icono de papelera.
* **Control y estado vacío:** Muestra automáticamente un estado ilustrado cuando no hay tareas y actualiza un contador en tiempo real (ej. *"3 tareas pendientes"*).
* **Demostración pedagógica:** Enseña cómo los mismos conceptos de Python para principiantes (variables, listas, bucles, condiciones y funciones) se integran directamente con una interfaz gráfica basada en Flutter a través de Flet.

---

##  Tecnologías Utilizadas

| Tecnología | Versión | Rol en el Proyecto |
| :--- | :--- | :--- |
| **Python** | 3.13+ | Lenguaje de programación principal. Controla la lógica de datos, estructuras en memoria y el flujo de la aplicación. |
| **Flet** | 0.86+ | Librería gráfica para Python que permite construir interfaces modernas basadas en Flutter sin escribir código Dart, HTML o CSS. |

---

##  ¿Qué se hizo para crear el programa? (Paso a Paso)

Para construir **TodoAppBasic1.2**, se siguió un proceso de desarrollo estructurado en 6 fases:

### 1. Definición del Estado en Memoria
Al igual que en la versión básica de consola, se definió una lista estándar de Python:
```python
tareas = []
```
Esto asegura que la aplicación conserve una lógica simple y directa, donde cada tarea es una cadena de texto (`str`) almacenada en un arreglo dinámico.

### 2. Configuración de la Ventana
Se estableció una ventana compacta tipo aplicación móvil/escritorio (`460x680 px`), con tema visual claro (`ThemeMode.LIGHT`), padding equilibrado y alineación centrada para ofrecer una apariencia profesional.

### 3. Diseño de los Controles de Entrada
Se integró un campo de texto moderno (`ft.TextField`) con esquinas redondeadas y texto de sugerencia (*placeholder*), emparejado con un botón de adición (`ft.IconButton`). Se vinculó el evento `on_submit` del teclado para permitir añadir tareas presionando **Enter**.

### 4. Construcción del Área de Tareas y Estado Vacío
Se implementó un componente `ft.ListView` con desplazamiento automático y un contenedor de estado vacío (`estado_vacio`) que muestra un icono ilustrativo y un mensaje amigable cuando la lista no tiene elementos.

### 5. Traducción de la Lógica de Consola a Funciones Gráficas
Se crearon funciones específicas para cada acción del usuario que sustituyen el viejo menú de consola (`while True`):
* En vez de `print()` &rarr; se redibujan los controles en la página con `page.update()`.
* En vez de `input()` &rarr; se lee la propiedad `input_tarea.value`.
* En vez de `tareas.append()` manual &rarr; se ejecuta mediante el botón o la tecla Enter.
* En vez de pedir el número por teclado para borrar &rarr; cada tarea tiene su propio botón de papelera asociado a su índice.

### 6. Empaquetado y Ejecución
Se integró la llamada `ft.run(main)` para que la aplicación se lance automáticamente en una ventana nativa de escritorio o en el navegador.

---

## ⚙️ Explicación Detallada de las Funciones del Código

A continuación se detalla cada una de las funciones y procedimientos contenidos en [`main.py`](main.py):

---

### 1. `main(page: ft.Page)`
* **Propósito:** Es la función de entrada principal (*entry point*) de Flet. Recibe el objeto `page`, que representa el lienzo o ventana donde se construirá toda la aplicación.
* **Parámetros:**
  * `page` (`ft.Page`): El contenedor raíz que maneja el título, dimensiones, tema y los controles visuales.
* **Lo que hace internamente:**
  1. Configura propiedades de la ventana: título (`"TodoAppBasic1.2"`), ancho (460), alto (680) y márgenes.
  2. Inicializa la lista `tareas = []`.
  3. Instancia los controles visuales (campo de texto, botones, listas, textos).
  4. Define las funciones internas (`actualizar_vista`, `agregar_tarea`, `eliminar_tarea`, `limpiar_todo`).
  5. Agrega los elementos ordenadamente a la página mediante `page.add(...)`.
  6. Dispara la primera llamada a `actualizar_vista()` para mostrar la pantalla inicial.

---

### 2. `actualizar_vista()`
* **Propósito:** Sincroniza la lista de datos en memoria (`tareas`) con lo que el usuario ve en pantalla. Equivale a la **Opción 1 (Ver tareas)** de la versión de consola.
* **Parámetros:** Ninguno.
* **Lo que hace internamente:**
  1. Vía `lista_tareas.controls.clear()`, elimina los elementos visuales previos para no duplicar tareas.
  2. Comprueba si `len(tareas) == 0`:
     * Si está vacía: hace visible el contenedor de `estado_vacio`, oculta el botón de limpiar y pone el contador en *"0 tareas pendientes"*.
     * Si tiene tareas: oculta el `estado_vacio`, activa el botón de limpiar y actualiza el contador con la cantidad exacta.
  3. Recorre la lista con un bucle `for indice, tarea in enumerate(tareas):` y genera por cada una:
     * Una tarjeta `ft.Container` con fondo blanco y bordes redondeados.
     * Una insignia circular con el número natural de la tarea (`indice + 1`).
     * El texto de la tarea expandido.
     * Un botón `ft.IconButton` con icono de papelera configurado para llamar a `eliminar_tarea(indice)`.
  4. Llama a `page.update()` para refrescar la interfaz gráfica de forma inmediata.

---

### 3. `agregar_tarea(e)`
* **Propósito:** Añade una nueva tarea a la lista cuando el usuario presiona el botón o la tecla Enter. Equivale a la **Opción 2 (Agregar tarea)** de la versión de consola.
* **Parámetros:**
  * `e`: El evento generado por Flet al hacer clic o enviar el formulario.
* **Lo que hace internamente:**
  1. Extrae el texto del campo de entrada y elimina espacios accidentales: `texto = input_tarea.value.strip()`.
  2. Valida si el texto está vacío (`texto == ""`):
     * Si está vacío: muestra un mensaje en color rojo (`mensaje_error.value`) y detiene la función.
  3. Si es válido:
     * Limpia el mensaje de error.
     * Inserta la tarea en la lista con `tareas.append(texto)`.
     * Limpia el campo de texto (`input_tarea.value = ""`) y devuelve el cursor al campo con `input_tarea.focus()`.
     * Invoca a `actualizar_vista()` para que la tarea aparezca en pantalla.

---

### 4. `eliminar_tarea(indice: int)`
* **Propósito:** Elimina la tarea específica seleccionada por el usuario. Equivale a la **Opción 3 (Eliminar tarea)** de la versión de consola.
* **Parámetros:**
  * `indice` (`int`): La posición numérica exacta del elemento en la lista `tareas`.
* **Lo que hace internamente:**
  1. Verifica que el índice se encuentre dentro del rango válido: `0 <= indice < len(tareas)`.
  2. Extrae y retira la tarea de la lista mediante `tareas.pop(indice)`.
  3. Ejecuta `actualizar_vista()` para redibujar la lista y renumerar automáticamente las tareas restantes.

---

### 5. `limpiar_todo(e)`
* **Propósito:** Función complementaria para vaciar la lista completa de tareas con un solo toque.
* **Parámetros:**
  * `e`: Evento de clic del botón.
* **Lo que hace internamente:**
  1. Ejecuta `tareas.clear()`, dejando la lista en cero elementos.
  2. Llama a `actualizar_vista()`, mostrando de nuevo el estado vacío de bienvenida.

---

##  Comparación: De la Consola a Flet

| Concepto en Python | Versión de Consola (`todo.py`) | Versión Gráfica Flet (`main.py`) |
| :--- | :--- | :--- |
| **Almacenamiento** | `tareas = []` | `tareas = []` *(Exactamente igual)* |
| **Añadir tarea** | `tareas.append(texto)` | `tareas.append(texto)` *(Exactamente igual)* |
| **Eliminar tarea** | `tareas.pop(indice)` | `tareas.pop(indice)` *(Exactamente igual)* |
| **Contar tareas** | `len(tareas)` | `len(tareas)` *(Exactamente igual)* |
| **Validar texto** | `texto.strip() == ""` | `texto.strip() == ""` *(Exactamente igual)* |
| **Entrada de usuario** | `input("Escribe una tarea: ")` | `input_tarea.value` en un `ft.TextField` |
| **Salida al usuario** | `print("1. Comprar pan")` | Componentes `ft.Row` y `ft.Container` en un `ft.ListView` |
| **Bucle del programa** | `while True:` infinito en terminal | Ciclo de eventos reactivo manejado por Flet |

---

## ¿Cómo Ejecutar la Aplicación?

1. Abre tu terminal (**PowerShell** o **Símbolo del sistema**).
2. Navega hasta la carpeta del proyecto:
   ## Por ejemplo:
   ```bash
   cd "C:\Users\Proyecto\TodoAppBasic1.2"
   ```
3. Ejecuta el archivo principal con Python:
   ```bash
   python main.py
   ```
4. Se abrirá inmediatamente la ventana visual de **TodoAppBasic1.2** lista para interactuar.

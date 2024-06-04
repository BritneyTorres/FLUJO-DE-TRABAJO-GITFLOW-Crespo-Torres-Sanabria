class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)

    def ver_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            tarea = self.tareas[indice]
            print(f"Título: {tarea.titulo}")
            print(f"Descripción: {tarea.descripcion}")
        else:
            print("Índice de tarea fuera de rango")

    def marcar_tarea_como_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completada = True
            print("Tarea marcada como completada.")
        else:
            print("Índice de tarea fuera de rango")

    def eliminar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            del self.tareas[indice]
            print("Tarea eliminada exitosamente.")
        else:
            print("Índice de tarea fuera de rango")
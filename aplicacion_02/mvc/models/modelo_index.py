import web

class ModeloIndex:
    def __init__(self):
        self.nombre = "Juan"
        self.email = "deja@email.com"

    def consultaProductos(self):
        datos = [
            "Laptop",
            "Mouse",
            "Juguete"
        ]
        return datos
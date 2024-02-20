import web

class Contactos:
    def __init__(self):
        self.nombre = None
        self.email = None

    def consultarContactos(self):
        datos = [
                    {"nombre": "Juana", "email": "juan@gmail.com"},
                    {"nombre": "Mercedes", "email": "moxxita@example.com"}
                ]

        return datos
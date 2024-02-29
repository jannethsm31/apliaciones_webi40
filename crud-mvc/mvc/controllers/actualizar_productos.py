import web
from mvc.models.modelo_productos import ModeloProductos

v_producto = ModeloProductos()
render = web.template.render('mvc/views/')

class ActualizarProductos:

    def GET(self, idProducto):
        try:
            lista = []
            producto = v_producto.DetallesProductos(idProducto)
            print('Actualizar', producto)
            lista.append(producto)
            return render.actualizar_productos(lista)
        except Exception as error:
            print(f'Ocurrió un error {error} Controlador AG')
            return "Ocurrió un error"

    def POST(self, idProducto):
        try:
            variable = web.input()
            print("variable", variable)
            if variable and idProducto == variable.producto:
                producto = {
                    "id_productos": int(idProducto),
                    "nombre": variable.nombre,
                    "descripcion": variable.descripcion,
                    "precio": int(variable.precio) if variable.precio.isdigit() else 0,
                    "existencias": int(variable.existencias) if variable.existencias.isdigit() else 0
                }
                resultado = v_producto.ActualizarProducto(producto)
                if resultado:
                    web.seeother("/")
                else:
                    return render.actualizar_productos(producto)
        except Exception as error:
            print(f'Ocurrió un error {error} Controlador AP')
            return "Ocurrió un error"
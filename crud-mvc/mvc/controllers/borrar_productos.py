import web
from mvc.models.modelo_productos import ModeloProductos

v_producto = ModeloProductos()
render = web.template.render('mvc/views')

class BorrarProductos:
    def GET(self, idProducto):
        try:
            lista = []
            producto = v_producto.DetallesProductos(idProducto)
            if producto:
                lista.append(producto)
                return render.borrar_productos(lista)
            else:
                return "Producto no encontrado"
        except Exception as error:
            print(f'Ocurrio un error: {error} Controlador BB')
            return "Ocurrio un error"

    def POST(self, idProducto):
        try:
            form = web.input()
            if idProducto == form.producto:
                result = v_producto.BorrarProductos(idProducto)
                if result:
                    web.seeother("/")
                else:
                    return render.borrar_productos(form.produccto)
            else:
                return "ID de producto no coincide"
        except Exception as error:
            print(f"Ocurrio un error: {error} Controlador BP")
            return "Ocurrio un error"
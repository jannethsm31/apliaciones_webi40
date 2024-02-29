import web
from mvc.models.modelo_productos import ModeloProductos

v_producto = ModeloProductos()
render = web.template.render('mvc/views/')

class ListaProductos:
    def GET(self):
        try:
            productos = v_producto.ObtenerTodosProductos()
            print(productos)
            return render.lista_productos(productos)
        except Exception as error:
            print(f"Ocurrio un error {error} Controlador LL")
            return "Ocurrio un error"
    def POST(self):
        try:
            entrada = web.input()
            producto = entrada.buscar
            respuesta = v_producto.BuscarProductos(producto)
            print('resuesta', respuesta)
            return render.lista_productos(respuesta)
        except Exception as error:
            return "Ocurrió un error"
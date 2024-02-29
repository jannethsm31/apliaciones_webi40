import web
from mvc.models.modelo_productos import ModeloProductos

v_productos = ModeloProductos()
render =  web.template.render('mvc/views/')

class DetalleProductos:
    def GET(self, idProductos):
        try:
            lista = []
            print(idProductos)
            producto = v_productos.DetallesProductos(idProductos)
            if producto:
                lista.append(producto)
                return render.detalle_productos(lista)
            else: 
                return "Producto no encontrado"
        except Exception as error:
            print(f"Ocurrio un errorr {error} Controlador DD")
            return "Ocurrio un error"
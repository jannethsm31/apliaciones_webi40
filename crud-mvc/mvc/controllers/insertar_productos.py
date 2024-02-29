import web
from mvc.models.modelo_productos import ModeloProductos

v_producto = ModeloProductos()
render = web.template.render('mvc/views/')

class InsertarProductos:
    def GET(self):
        try:
            return render.insertar_productos()
        except Exception as error:
            print(f'Ocurrio un error: {error} Controlador II')
            return "Ocurrio un error"

    def POST(self):
        try:
            p_insertado = web.input()
            print('hola', p_insertado)
            if p_insertado:
                producto = {
                    "nombre": p_insertado.nombre,
                    "descripcion": p_insertado.descripcion,
                    "precio": p_insertado.precio,
                    "existencias": p_insertado.existencia
                }
                resultado = v_producto.insertarProducto(producto)
                if resultado:
                    web.seeother("/")
                else: 
                    return render.insertar_productos()
        except Exception as error:
            print(f"Ocurrio un error: {error} Controlador IP")
            return "Ocurrio un error"
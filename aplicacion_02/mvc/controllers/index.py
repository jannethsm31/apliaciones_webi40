import web
from mvc.models.modelo_index import ModeloIndex # Importamos el modelo desde la ruta

render = web.template.render('mvc/views/', base='layout')

m_index = ModeloIndex() #m_index tiene acceso a todas la variables que se generan

class Index:
    def GET(self):
        try:
            productos = m_index.consultaProductos()
            return render.index(productos)
        except Exception as e:
            print(f"Error 101 - index {e.args}")
            return "Ups algo salio mal"
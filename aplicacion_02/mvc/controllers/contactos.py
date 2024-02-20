import web
from mvc.models.modelo_contactos import Contactos # Importamos el modelo desde la ruta

render = web.template.render('mvc/views/', base='layout_contactos')

m_contactos = Contactos() #m_contactos tiene acceso a todas la variables que se generan

class ContactosIndex:
    def GET(self):
        try:
            v_contactos = m_contactos.consultarContactos()
            return render.contactos(v_contactos)

        except Exception as e:
            print(f"Error 101 - index {e}")
            return "Ups algo salio mal"
import web #Libreria web.py URL= http://localhost:8080

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.contactos.ContactosIndex',
    '/index', 'mvc.controllers.index.Index',
    #'/productos', 'mvc.controllers.productos.Productos'
    # Indica la ruta. de carpetas, ruta del archivo y de la clase
)
app = web.application(urls, globals())



if __name__ == "__main__":
    #web.config.debug = False  #nos permite que los fallos no los vea el usuario o visitante
    app.run()
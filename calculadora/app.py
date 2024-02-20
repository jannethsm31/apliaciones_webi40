import web

urls = (
    "/", "mvc.controllers.calculadora.Calculadora"
)

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
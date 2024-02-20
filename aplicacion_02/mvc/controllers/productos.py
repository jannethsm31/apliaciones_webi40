import web

render = web.template.render('mvc/views/')


class Productos:
    def GET(self):
        return render.productos()
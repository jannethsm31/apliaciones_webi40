import web
from mvc.models.calculadora_modelo import CalculadoraModelo

render = web.template.render("mvc/views/")

class Calculadora:
    def GET(self):
        return render.calculadora(num1='', num2='', sum='')

    def POST(self):
        form = web.input()
        num1 = form.num1
        num2 = form.num2
        modelo = CalculadoraModelo()
        resultado = modelo.sumar(num1, num2)
        return render.calculadora(num1, num2, resultado)

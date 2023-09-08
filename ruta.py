from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola Mundo!'

@app.route('/dojo')
def dojo():
    return '¡Dojo!'

@app.route('/say/<string:name>')
def say_hello(name):
    return f'¡Hola, {name}!'

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    return word * num

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración

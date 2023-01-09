
""" Aplicacion persistencia """
#importamos de flask, Flask, request y redirect
from flask import Flask, request, redirect, Response

#importamos la funcion guardar_pedido del archivo persistencia.py
from persistencia import guardar_pedido

#se crea la aplicacion indicando el nombre actual como punto para establecer las rutas
app = Flask(__name__)

#se configura la ruta /pizza que aceptara el metodo POST
@app.route("/pizza", methods=['POST'])

#se implementa el metodo pizza que recibiria de la petición el nombre y el apellido
def pizza():
    """ Aplicacion persistencia función que guarda los datos del pedido """
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    #lo imprime en consola
    print ('Nombre: '+nombre)
    print ('Apellido: '+apellido)
    #lo guarda en un fichero pedidos.txt de guardar pedido
    guardar_pedido(nombre, apellido)
    return redirect("http://localhost/actividad_20221211/apache/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])

def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    # Aquí va el código Python. Debe capturar el parámetro "size" de la request. Debe
    #retornar siempre "Disponible", excepto para el tamaño "S" que debe retornar "No
    #disponible" y se debe asignar en mensaje, así mensaje = "Lo que corresponda"
    size = request.form.get("size")
    mensaje = "Disponible"
    if size == "S":
        mensaje = "No disponible"

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})

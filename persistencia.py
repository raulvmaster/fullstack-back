"""
    se define la funcion guardar_pedido, que recibe como parametros
    nombre, apellido
"""
def guardar_pedido(nombre, apellidos):
    """
    abre un fichero en modo añadir y guarda los parametros, nombre y apellidos
    """
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write("-"+nombre + " " + apellidos + "\n")
        file.close()
        
class Producto():
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    def verificar_disponibilidad(self, cantidad):
        return self.stock >= cantidad

    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Venta realizada: {cantidad} unidades de {self.nombre}")
        else:
            print("Stock insuficiente")

    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Stock actualizado: {self.stock} unidades de {self.nombre}")


producto = Producto("Laptop", 1200, 10)

acciones = [
    ("Verificar 5 unidades", producto.verificar_disponibilidad(5)),
    ("Vender 3 unidades", producto.vender(3)),
    ("Verificar 8 unidades", producto.verificar_disponibilidad(8)),
    ("Intentar vender 8 unidades", producto.vender(8)),
    ("Reabastecer con 10 unidades", producto.reabastecer(10)),
    ("Verificar 8 unidades", producto.verificar_disponibilidad(8)),
    ("Vender 8 unidades", producto.vender(8))
]

for accion, resultado in acciones:
    print(f"{accion}: {resultado}" if isinstance(resultado, bool) else f"{accion}")

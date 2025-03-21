class Rectangulo:
    def __init__(self, largo: float, ancho: float):
        if largo <= 0 or ancho <= 0:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
        self.__largo = largo
        self.__ancho = ancho

    def cambiar_dimensiones(self, nuevo_largo: float, nuevo_ancho: float):
        if nuevo_largo <= 0 or nuevo_ancho <= 0:
            raise ValueError("El largo y el ancho deben ser mayores que cero.")
        self.__largo = nuevo_largo
        self.__ancho = nuevo_ancho

    def calcular_area(self) -> float:
        return self.__largo * self.__ancho

    def calcular_perimetro(self) -> float:
        return 2 * (self.__largo + self.__ancho)

    def obtener_dimensiones(self) -> tuple:
        return self.__largo, self.__ancho

# Ejemplo de uso
rectangulo = Rectangulo(10, 5)
print(f"Dimensiones: {rectangulo.obtener_dimensiones()}")
print(f"Área: {rectangulo.calcular_area()}")
print(f"Perímetro: {rectangulo.calcular_perimetro()}")

rectangulo.cambiar_dimensiones(15, 7)
print(f"Nuevas dimensiones: {rectangulo.obtener_dimensiones()}")
print(f"Nueva área: {rectangulo.calcular_area()}")
print(f"Nuevo perímetro: {rectangulo.calcular_perimetro()}")

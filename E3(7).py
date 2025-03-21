class Estudiante:
    def __init__(self, nombre: str, edad: int):
        if edad <= 0:
            raise ValueError("La edad debe ser un número positivo.")
        self.__nombre = nombre
        self.__edad = edad
        self.__notas = []

    def agregar_nota(self, nota: float):
        if not (0 <= nota <= 100):
            raise ValueError("La nota debe estar en el rango de 0 a 100.")
        self.__notas.append(nota)

    def calcular_promedio(self) -> float:
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

    def obtener_nombre(self) -> str:
        return self.__nombre

    def obtener_edad(self) -> int:
        return self.__edad

# Ejemplo de uso
estudiante = Estudiante("Cristian Conde", 17)
print(f"Nombre: {estudiante.obtener_nombre()}, Edad: {estudiante.obtener_edad()}")

estudiante.agregar_nota(85)
estudiante.agregar_nota(90)
estudiante.agregar_nota(78)

print(f"Promedio de notas: {estudiante.calcular_promedio()}")

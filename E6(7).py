class Empleado:
    contador_empleados = 0

    def __init__(self, nombre: str, salario: float):
        self.nombre = nombre
        self.salario = salario
        Empleado.contador_empleados += 1

    @classmethod
    def cantidad_empleados(cls) -> int:
        return cls.contador_empleados

# Ejemplo de uso
empleado1 = Empleado("Cristian Conde", 3000)
empleado2 = Empleado("Antonio Ortega", 3500)

print(f"Total de empleados: {Empleado.cantidad_empleados()}")

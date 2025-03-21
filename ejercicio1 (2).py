class Estudiante():
    def __init__(self, nombre, apellido, calificacion):
        self.nombre = nombre
        self.apellido = apellido
        self.calificacion = float(calificacion)


estudiante1 = Estudiante("Cristian", "Conde", "4.6")
estudiante2 = Estudiante("Antonio", "Ortega", "3.7")
estudiante3 = Estudiante("Juan", "Perez", "2.5")

estudiantes = [estudiante1, estudiante2, estudiante3]

for estudiante in estudiantes:
    print(f"Nombre: {estudiante.nombre}")
    print(f"Apellido: {estudiante.apellido}")
    print(f"Calificación: {estudiante.calificacion}")

    if estudiante.calificacion >= 3.0:
        print("Aprobado")
    else:
        print("Reprobado")
    print("------------")

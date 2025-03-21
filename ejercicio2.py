class Libro():
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de Páginas: {self.num_paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        self.num_paginas = nuevas_paginas
        print(f"El número de páginas ha sido actualizado a: {self.num_paginas}")


libro1 = Libro("El Quijote", "Miguel de Cervantes", 1000)
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 500)

libro1.mostrar_informacion()
libro1.actualizar_paginas(1050)
libro1.mostrar_informacion()

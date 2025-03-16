class Libro:
    def __init__(self, titulo, autor, paginas):
        
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_info(self):
        
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.paginas}")

    def actualizar_paginas(self, nuevas_paginas):
        
        if nuevas_paginas > 0:
            self.paginas = nuevas_paginas
            print("Número de páginas actualizado correctamente.")
        else:
            print("El número de páginas debe ser mayor a 0.")

# Ejemplo de uso
libro1 = Libro("Narnia", "C.S Lewis", 816)
libro1.mostrar_info()

# Actualizar número de páginas
libro1.actualizar_paginas(800)
libro1.mostrar_info()

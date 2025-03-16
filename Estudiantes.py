class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def mostrar_info(self):
        
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Calificación: {self.calificacion}")

    def verificar_aprobacion(self):
        """
        El estudiante aprobó o reprobó.
        Se considera aprobado si la calificación es 3.0 o superior.
        """
        if self.calificacion >= 3.0:
            return f"{self.nombre} ha aprobado. ✅"
        else:
            return f"{self.nombre} ha reprobado. ❌"

# Ejemplo de uso
estudiante1 = Estudiante("Karol Marquez", 20, 4.5)
estudiante1.mostrar_info()
print(estudiante1.verificar_aprobacion())

estudiante2 = Estudiante("Breyner Quintero", 21, 2.8)
estudiante2.mostrar_info()
print(estudiante2.verificar_aprobacion())

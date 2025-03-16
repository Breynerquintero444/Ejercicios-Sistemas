class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
       
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
            print(f"El vehículo ha acelerado. Velocidad actual: {self.velocidad_actual} km/h")
        else:
            self.velocidad_actual = self.velocidad_maxima
            print(f"¡Cuidado! Se ha alcanzado la velocidad máxima de {self.velocidad_maxima} km/h")

    def frenar(self, decremento):
       
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
            print(f"El vehículo ha frenado. Velocidad actual: {self.velocidad_actual} km/h")
        else:
            self.velocidad_actual = 0
            print("El vehículo se ha detenido.")

    def verificar_limite(self, velocidad_limite):
       
        if self.velocidad_actual > velocidad_limite:
            print(f"¡Alerta! Excediendo el límite de velocidad de {velocidad_limite} km/h")
        else:
            print(f"Velocidad dentro del límite de {velocidad_limite} km/h")

# Crear un objeto Vehiculo
vehiculo = Vehiculo("Toyota", "Corolla", 180)

# Menú interactivo
while True:
    print("\n--- Menú de Control de Vehículo ---")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Verificar límite de velocidad")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        incremento = int(input("Ingrese la cantidad a acelerar (km/h): "))
        vehiculo.acelerar(incremento)
    elif opcion == "2":
        decremento = int(input("Ingrese la cantidad a frenar (km/h): "))
        vehiculo.frenar(decremento)
    elif opcion == "3":
        velocidad_limite = int(input("Ingrese el límite de velocidad (km/h): "))
        vehiculo.verificar_limite(velocidad_limite)
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")

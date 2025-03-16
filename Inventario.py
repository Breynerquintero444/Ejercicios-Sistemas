class Producto:
    def __init__(self, nombre, precio, stock):
        
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        
        return self.stock >= cantidad

    def vender(self, cantidad):
        
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Venta exitosa: {cantidad} unidades de {self.nombre} vendidas.")
        else:
            print(f"Error: No hay suficiente stock para vender {cantidad} unidades.")

    def reabastecer(self, cantidad):
        
        self.stock += cantidad
        print(f"Reabastecimiento exitoso: Se agregaron {cantidad} unidades de {self.nombre}.")

# Crear objeto Producto con valores iniciales
producto1 = Producto("Laptop", 1200, 10)

# Realizar operaciones según el enunciado
print(producto1.verificar_disponibilidad(5))  # Verificar si hay 5 unidades disponibles
producto1.vender(3)  # Vender 3 unidades
print(producto1.verificar_disponibilidad(8))  # Verificar si hay 8 unidades disponibles
producto1.vender(8)  # Intentar vender 8 unidades (debería fallar)
producto1.reabastecer(10)  # Reabastecer con 10 unidades
print(producto1.verificar_disponibilidad(8))  # Verificar nuevamente si hay 8 unidades disponibles
producto1.vender(8)  # Vender 8 unidades

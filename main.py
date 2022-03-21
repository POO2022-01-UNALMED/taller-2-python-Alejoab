class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color



class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, newRegistro):
        self.registro = newRegistro

    def asignarTipo(self, newTipo):
        if newTipo in ["electrico", "gasolina"]:
            self.tipo = newTipo




class Auto:
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        
    def cantidadAsientos(self):
        a = filter(lambda x: isinstance(x, Asiento), self.asientos)
        return len(list(a))

    def verificarIntegridad(self):
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        
        else:
            for i in self.asientos:
                if isinstance(i, Asiento) and i.registro != self.registro:
                    return "Las piezas no son originales"

        return "Auto original"

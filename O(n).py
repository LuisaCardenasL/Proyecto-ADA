class Parte:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion


class Escena:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partes = []

    def agregar_parte(self, parte):
        self.partes.append(parte)

    def obtener_duracion_total(self):
        duracion_total = 0
        for parte in self.partes:
            duracion_total += parte.duracion
        return duracion_total


class Espectaculo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.escenas = []

    def agregar_escena(self, escena):
        self.escenas.append(escena)

    def obtener_duracion_total(self):
        duracion_total = 0
        for escena in self.escenas:
            duracion_total += escena.obtener_duracion_total()
        return duracion_total


# Ejemplo de uso
espectaculo = Espectaculo("Espectáculo de Circo")

# Crear escena 1
escena1 = Escena("Escena 1")

parte1 = Parte("Parte 1", 10)
parte2 = Parte("Parte 2", 15)

escena1.agregar_parte(parte1)
escena1.agregar_parte(parte2)

# Crear escena 2
escena2 = Escena("Escena 2")

parte3 = Parte("Parte 3", 12)
parte4 = Parte("Parte 4", 8)

escena2.agregar_parte(parte3)
escena2.agregar_parte(parte4)

# Agregar escenas al espectáculo
espectaculo.agregar_escena(escena1)
espectaculo.agregar_escena(escena2)

# Obtener duración total del espectáculo
duracion_total = espectaculo.obtener_duracion_total()
print("Duración total del espectáculo:", duracion_total)

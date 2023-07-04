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

    def obtener_grandeza_total(self):
        grandeza_total = 0
        for parte in self.partes:
            grandeza_total += len(parte.nombre.split(", "))
        return grandeza_total


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

    def obtener_animal_mas_participante(self):
        participantes = {}
        for escena in self.escenas:
            for parte in escena.partes:
                for animal in parte.nombre.split(", "):
                    if animal in participantes:
                        participantes[animal] += 1
                    else:
                        participantes[animal] = 1
        animal_mas_participante = max(participantes, key=participantes.get)
        return animal_mas_participante, participantes[animal_mas_participante]

    def obtener_animales_menos_participantes(self):
        participantes = {}
        for escena in self.escenas:
            for parte in escena.partes:
                for animal in parte.nombre.split(", "):
                    if animal in participantes:
                        participantes[animal] += 1
                    else:
                        participantes[animal] = 1
        min_participaciones = min(participantes.values())
        animales_menos_participantes = [animal for animal, participaciones in participantes.items() if participaciones == min_participaciones]
        return animales_menos_participantes, min_participaciones

    def obtener_escena_menor_grandeza_total(self):
        escena_menor_grandeza_total = min(self.escenas, key=lambda x: x.obtener_grandeza_total())
        return escena_menor_grandeza_total.nombre

    def obtener_escena_mayor_grandeza_total(self):
        escena_mayor_grandeza_total = max(self.escenas, key=lambda x: x.obtener_grandeza_total())
        return escena_mayor_grandeza_total.nombre

    def obtener_promedio_grandeza_total(self):
        total_grandeza = 0
        total_escenas = len(self.escenas)
        for escena in self.escenas:
            total_grandeza += escena.obtener_grandeza_total()
        promedio_grandeza = total_grandeza / total_escenas
        return round(promedio_grandeza, 2)


# Ejemplo de uso
espectaculo = Espectaculo("Espectáculo de Circo")

# Crear escena 1
escena1 = Escena("Escena 1")

parte1 = Parte("Capibara, Loro, Caimán", 10)
parte2 = Parte("Capibara, Caimán, Boa", 15)

escena1.agregar_parte(parte1)
escena1.agregar_parte(parte2)

# Crear escena 2
escena2 = Escena("Escena 2")

parte3 = Parte("Capibara, Loro, Cocodrilo", 12)
parte4 = Parte("Loro, Cocodrilo, Pantera negra", 8)

escena2.agregar_parte(parte3)
escena2.agregar_parte(parte4)

# Crear escena 3
escena3 = Escena("Escena 3")

parte5 = Parte("Capibara, Loro, Tigre", 10)
parte6 = Parte("Loro, Caimán, León", 15)

escena3.agregar_parte(parte5)
escena3.agregar_parte(parte6)

# Crear escena 4
escena4 = Escena("Escena 4")

parte7 = Parte("Boa, Cocodrilo, León", 10)
parte8 = Parte("Cebra, Pantera negra, Tigre", 15)

escena4.agregar_parte(parte7)
escena4.agregar_parte(parte8)

# Crear escena 5
escena5 = Escena("Escena 5")

parte9 = Parte("Cebra, Pantera negra, León", 12)

escena5.agregar_parte(parte9)

# Agregar escenas al espectáculo
espectaculo.agregar_escena(escena1)
espectaculo.agregar_escena(escena2)
espectaculo.agregar_escena(escena3)
espectaculo.agregar_escena(escena4)
espectaculo.agregar_escena(escena5)

# Obtener duración total del espectáculo
duracion_total = espectaculo.obtener_duracion_total()
print("Duración total del espectáculo:", duracion_total)

# Obtener participación de animales
animal_mas_participante, cantidad_participaciones = espectaculo.obtener_animal_mas_participante()
print("El animal que participó en más escenas dentro del espectáculo fue el", animal_mas_participante, "que participó en", cantidad_participaciones, "escenas.")

animales_menos_participantes, min_participaciones = espectaculo.obtener_animales_menos_participantes()
print("Los animales que menos participaron en escenas dentro del espectáculo fueron", ", ".join(animales_menos_participantes), "quienes participaron cada uno en", min_participaciones, "escenas.")

# Obtener escenas con mayor y menor grandeza total
escena_menor_grandeza_total = espectaculo.obtener_escena_menor_grandeza_total()
print("La escena de menor grandeza total fue la escena", escena_menor_grandeza_total)

escena_mayor_grandeza_total = espectaculo.obtener_escena_mayor_grandeza_total()
print("La escena de mayor grandeza total fue la escena", escena_mayor_grandeza_total)

# Obtener promedio de grandeza total
promedio_grandeza = espectaculo.obtener_promedio_grandeza_total()
print("El promedio de grandeza de todo el espectáculo fue de", promedio_grandeza)
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

    def obtener_grandeza_total(self):
        grandeza_total = 0
        for parte in self.partes:
            grandeza_total += len(parte.nombre.split(", "))
        return grandeza_total


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

    def obtener_animal_mas_participante(self):
        participantes = {}
        for escena in self.escenas:
            for parte in escena.partes:
                for animal in parte.nombre.split(", "):
                    if animal in participantes:
                        participantes[animal] += 1
                    else:
                        participantes[animal] = 1
        animal_mas_participante = max(participantes, key=participantes.get)
        return animal_mas_participante, participantes[animal_mas_participante]

    def obtener_animales_menos_participantes(self):
        participantes = {}
        for escena in self.escenas:
            for parte in escena.partes:
                for animal in parte.nombre.split(", "):
                    if animal in participantes:
                        participantes[animal] += 1
                    else:
                        participantes[animal] = 1
        min_participaciones = min(participantes.values())
        animales_menos_participantes = [animal for animal, participaciones in participantes.items() if participaciones == min_participaciones]
        return animales_menos_participantes, min_participaciones

    def obtener_escena_menor_grandeza_total(self):
        escena_menor_grandeza_total = min(self.escenas, key=lambda x: x.obtener_grandeza_total())
        return escena_menor_grandeza_total.nombre

    def obtener_escena_mayor_grandeza_total(self):
        escena_mayor_grandeza_total = max(self.escenas, key=lambda x: x.obtener_grandeza_total())
        return escena_mayor_grandeza_total.nombre

    def obtener_promedio_grandeza_total(self):
        total_grandeza = 0
        total_escenas = len(self.escenas)
        for escena in self.escenas:
            total_grandeza += escena.obtener_grandeza_total()
        promedio_grandeza = total_grandeza / total_escenas
        return round(promedio_grandeza, 2)


# Ejemplo de uso
espectaculo = Espectaculo("Espectáculo de Circo")

# Crear escena 1
escena1 = Escena("Escena 1")

parte1 = Parte("Capibara, Loro, Caimán", 10)
parte2 = Parte("Capibara, Caimán, Boa", 15)

escena1.agregar_parte(parte1)
escena1.agregar_parte(parte2)

# Crear escena 2
escena2 = Escena("Escena 2")

parte3 = Parte("Capibara, Loro, Cocodrilo", 12)
parte4 = Parte("Loro, Cocodrilo, Pantera negra", 8)

escena2.agregar_parte(parte3)
escena2.agregar_parte(parte4)

# Crear escena 3
escena3 = Escena("Escena 3")

parte5 = Parte("Capibara, Loro, Tigre", 10)
parte6 = Parte("Loro, Caimán, León", 15)

escena3.agregar_parte(parte5)
escena3.agregar_parte(parte6)

# Crear escena 4
escena4 = Escena("Escena 4")

parte7 = Parte("Boa, Cocodrilo, León", 10)
parte8 = Parte("Cebra, Pantera negra, Tigre", 15)

escena4.agregar_parte(parte7)
escena4.agregar_parte(parte8)

# Crear escena 5
escena5 = Escena("Escena 5")

parte9 = Parte("Cebra, Pantera negra, León", 12)

escena5.agregar_parte(parte9)

# Agregar escenas al espectáculo
espectaculo.agregar_escena(escena1)
espectaculo.agregar_escena(escena2)
espectaculo.agregar_escena(escena3)
espectaculo.agregar_escena(escena4)
espectaculo.agregar_escena(escena5)

# Obtener duración total del espectáculo
duracion_total = espectaculo.obtener_duracion_total()
print("Duración total del espectáculo:", duracion_total)

# Obtener participación de animales
animal_mas_participante, cantidad_participaciones = espectaculo.obtener_animal_mas_participante()
print("El animal que participó en más escenas dentro del espectáculo fue el", animal_mas_participante, "que participó en", cantidad_participaciones, "escenas.")

animales_menos_participantes, min_participaciones = espectaculo.obtener_animales_menos_participantes()
print("Los animales que menos participaron en escenas dentro del espectáculo fueron", ", ".join(animales_menos_participantes), "quienes participaron cada uno en", min_participaciones, "escenas.")

# Obtener escenas con mayor y menor grandeza total
escena_menor_grandeza_total = espectaculo.obtener_escena_menor_grandeza_total()
print("La escena de menor grandeza total fue la escena", escena_menor_grandeza_total)

escena_mayor_grandeza_total = espectaculo.obtener_escena_mayor_grandeza_total()
print("La escena de mayor grandeza total fue la escena", escena_mayor_grandeza_total)

# Obtener promedio de grandeza total
promedio_grandeza = espectaculo.obtener_promedio_grandeza_total()
print("El promedio de grandeza de todo el espectáculo fue de", promedio_grandeza)
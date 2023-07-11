class Animal:
    def __init__(self, nombre, grandeza):
        self.nombre = nombre
        self.grandeza = grandeza

    def __str__(self):
        return f"{self.nombre} ({self.grandeza})"


class Escena:
    def __init__(self, animales):
        self.animales = animales
        self.grandeza_total = sum(animal.grandeza for animal in animales)
        self.max_grandeza_individual = max(animal.grandeza for animal in animales)

    def __str__(self):
        return ", ".join(str(animal) for animal in self.animales)


class Espectaculo:
    def __init__(self, n, m, k, animales, partes):
        self.n = n
        self.m = m
        self.k = k
        self.animales = animales
        self.partes = partes


    '''
        Se utilizó el método de ordenamiento quicksort ya que tiene
        un orden de crecimiento promedio de O(n log(n))
    '''
    def ordenar_escenas_quicksort(self, escenas):
        if len(escenas) <= 1:
            return escenas

        pivote = escenas[len(escenas) // 2]
        menores, iguales, mayores = [], [], []

        for escena in escenas:
            if escena.grandeza_total < pivote.grandeza_total:
                menores.append(escena)
            elif escena.grandeza_total == pivote.grandeza_total:
                if escena.max_grandeza_individual < pivote.max_grandeza_individual:
                    menores.append(escena)
                elif escena.max_grandeza_individual == pivote.max_grandeza_individual:
                    iguales.append(escena)
                else:
                    mayores.append(escena)
            else:
                mayores.append(escena)

        return (
            self.ordenar_escenas_quicksort(menores)
            + iguales
            + self.ordenar_escenas_quicksort(mayores)
        )

    def mostrar_escenas(self, escenas):
        for escena in escenas:
            print(escena)

    def ejecutar_espectaculo(self):
        todas_las_escenas = [Escena(partida) for partida in self.partes]
        apertura = todas_las_escenas[: self.m * self.k]
        partes_siguientes = todas_las_escenas[self.m * self.k :]

        escenas_ordenadas_apertura = self.ordenar_escenas_quicksort(apertura)
        escenas_ordenadas_partes = self.ordenar_escenas_quicksort(partes_siguientes)

        print("Apertura:")
        self.mostrar_escenas(escenas_ordenadas_apertura)

        for i, parte in enumerate(escenas_ordenadas_partes, 1):
            print(f"Parte {i}:")
            self.mostrar_escenas([parte])

        todas_las_escenas_ordenadas = (
            escenas_ordenadas_apertura + escenas_ordenadas_partes
        )
        animales_escenas = [
            animal
            for escena in todas_las_escenas_ordenadas
            for animal in escena.animales
        ]

        animales_participantes = set(animales_escenas)
        animales_contador = {
            animal: animales_escenas.count(animal) for animal in animales_participantes
        }

        animal_mas_participante = max(animales_contador, key=animales_contador.get)
        max_participacion = animales_contador[animal_mas_participante]

        animales_menos_participantes = [
            animal
            for animal, count in animales_contador.items()
            if count == min(animales_contador.values())
        ]
        min_participacion = animales_contador[animales_menos_participantes[0]]

        escena_menor_grandeza_total = min(
            todas_las_escenas_ordenadas, key=lambda escena: escena.grandeza_total
        )
        escena_mayor_grandeza_total = max(
            todas_las_escenas_ordenadas, key=lambda escena: escena.grandeza_total
        )

        promedio_grandezas = sum(animal.grandeza for animal in animales_escenas) / len(
            animales_escenas
        )

        print("\nResultados:")
        print(
            f"El animal que participó en más escenas: {animal_mas_participante.nombre} ({max_participacion} escenas)"
        )
        print(
            f"El animal que participó en menos escenas: {', '.join(str(animal) for animal in animales_menos_participantes)} ({min_participacion} escenas)"
        )
        print(f"Escena de menor grandeza total: {escena_menor_grandeza_total}")
        print(f"Escena de mayor grandeza total: {escena_mayor_grandeza_total}")
        print(f"Promedio de grandeza de todo el espectáculo: {promedio_grandezas:.2f}")


"""
    Ejemplo de uso 
"""

# Creacion del espectaculo
n = 9
m = 4
k = 3

animales = [
    Animal("Capibara", 1),
    Animal("Loro", 2),
    Animal("Caimán", 3),
    Animal("Boa", 4),
    Animal("Cocodrilo", 5),
    Animal("Cebra", 6),
    Animal("Pantera negra", 7),
    Animal("Tigre", 8),
    Animal("León", 9),
]

partes = [
    [Animal("Caimán", 3), Animal("Capibara", 1), Animal("Loro", 2)],
    [Animal("Boa", 4), Animal("Caimán", 3), Animal("Capibara", 1)],
    [Animal("Cocodrilo", 5), Animal("Capibara", 1), Animal("Loro", 2)],
    [Animal("Pantera negra", 7), Animal("Cocodrilo", 5), Animal("Loro", 2)],
    [Animal("Tigre", 8), Animal("Loro", 2), Animal("Capibara", 1)],
    [Animal("León", 9), Animal("Caimán", 3), Animal("Loro", 2)],
    [Animal("León", 9), Animal("Cocodrilo", 5), Animal("Boa", 4)],
    [Animal("León", 9), Animal("Pantera negra", 7), Animal("Cebra", 6)],
    [Animal("Tigre", 8), Animal("Cebra", 6), Animal("Pantera negra", 7)],
]


espectaculo = Espectaculo(n, m, k, animales, partes)

# Ejecución del espectaculo
espectaculo.ejecutar_espectaculo()
from itertools import combinations


def generar_escenas_apertura(animales):
    escenas = []
    for comb in combinations(animales, 3):
        escenas.append(list(comb))
    return escenas


def calcular_grandeza_total(escena):
    return sum(grandeza for _, grandeza in escena)


def ordenar_escenas_apertura(escenas):
    return sorted(escenas, key=lambda escena: (calcular_grandeza_total(escena), max(grandeza for _, grandeza in escena)))


def dividir_partes(escenas, m, k):
    partes = []
    for i in range(0, len(escenas), k):
        parte = escenas[i:i+k]
        partes.append(parte)
    return partes


def ordenar_escenas_partes(partes):
    for parte in partes:
        parte.sort(key=lambda escena: calcular_grandeza_total(escena))


def encontrar_animal_participacion(partes):
    animal_participacion = {}
    for parte in partes:
        for escena in parte:
            for animal in escena:
                if animal in animal_participacion:
                    animal_participacion[animal] += 1
                else:
                    animal_participacion[animal] = 1
    max_participacion = max(animal_participacion.values())
    animales_max_participacion = [animal for animal, participacion in animal_participacion.items(
    ) if participacion == max_participacion]
    min_participacion = min(animal_participacion.values())
    animales_min_participacion = [animal for animal, participacion in animal_participacion.items(
    ) if participacion == min_participacion]
    return animales_max_participacion, max_participacion, animales_min_participacion, min_participacion


def encontrar_extremos_grandeza(escenas):
    escena_min_grandeza = min(
        escenas, key=lambda escena: calcular_grandeza_total(escena))
    escena_max_grandeza = max(
        escenas, key=lambda escena: calcular_grandeza_total(escena))
    return escena_min_grandeza, escena_max_grandeza


def calcular_promedio_grandeza(escenas):
    total_grandeza = sum(calcular_grandeza_total(escena) for escena in escenas)
    return total_grandeza / len(escenas)

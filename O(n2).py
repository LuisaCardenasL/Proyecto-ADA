def organizar_espectaculo(escenas):
    # Ordenar las escenas de cada parte
    for parte in escenas:
        bubble_sort(parte, key=lambda escena: escena_grandeza_total(escena))

    # Ordenar las partes en el espectáculo principal
    bubble_sort(escenas, key=lambda parte: parte_grandeza_total(parte))

    # Obtener información adicional
    animal_mas_participacion, animal_menos_participacion = obtener_animal_participacion(
        escenas)
    escena_menor_grandeza, escena_mayor_grandeza = obtener_escenas_grandeza(
        escenas)
    promedio_grandeza = calcular_promedio_grandeza(escenas)

    # Retornar el resultado
    return {
        'escenas_ordenadas': escenas,
        'animal_mas_participacion': animal_mas_participacion,
        'animal_menos_participacion': animal_menos_participacion,
        'escena_menor_grandeza': escena_menor_grandeza,
        'escena_mayor_grandeza': escena_mayor_grandeza,
        'promedio_grandeza': promedio_grandeza
    }


def bubble_sort(array, key):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if key(array[j]) > key(array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]


def escena_grandeza_total(escena):
    return sum(animal.grandeza for animal in escena)


def parte_grandeza_total(parte):
    return sum(escena_grandeza_total(escena) for escena in parte)


def obtener_animal_participacion(escenas):
    conteo_animal = {}
    for parte in escenas:
        for escena in parte:
            for animal in escena:
                conteo_animal[animal] = conteo_animal.get(animal, 0) + 1

    animal_mas_participacion = max(conteo_animal, key=conteo_animal.get)
    animal_menos_participacion = min(conteo_animal, key=conteo_animal.get)

    return animal_mas_participacion, animal_menos_participacion


def obtener_escenas_grandeza(escenas):
    escena_menor_grandeza = min(escenas, key=escena_grandeza_total)
    escena_mayor_grandeza = max(escenas, key=escena_grandeza_total)

    return escena_menor_grandeza, escena_mayor_grandeza


def calcular_promedio_grandeza(escenas):
    total_grandezas = sum(escena_grandeza_total(escena)
                          for parte in escenas for escena in parte)
    total_escenas = sum(len(parte) for parte in escenas)

    return total_grandezas / total_escenas
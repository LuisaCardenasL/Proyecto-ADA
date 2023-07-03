def organizar_espectaculo(escenas):
    # Ordenar las escenas de cada parte
    for parte in escenas:
        merge_sort(parte, key=lambda escena: escena_grandeza_total(escena))

    # Ordenar las partes en el espectáculo principal
    merge_sort(escenas, key=lambda parte: parte_grandeza_total(parte))

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


def merge_sort(array, key):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    left = merge_sort(left, key)
    right = merge_sort(right, key)

    return merge(left, right, key)


def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


# Las funciones 'escena_grandeza_total', 'parte_grandeza_total', 'obtener_animal_participacion',
# 'obtener_escenas_grandeza' y 'calcular_promedio_grandeza' son las mismas que en la solución 1.

# Código adicional...

def espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes):
    animales_grandezas = list(zip(animales, grandezas))

    def ordenar_escenas(escenas):
        for i in range(1, len(escenas)):
            j = i
            while j > 0 and comparar_escenas(escenas[j - 1], escenas[j]):
                escenas[j - 1], escenas[j] = escenas[j], escenas[j - 1]
                j -= 1
        return escenas

    def comparar_escenas(escena1, escena2):
        grandeza_total1 = sum(grandezas[animales.index(animal)] for animal in escena1)
        grandeza_total2 = sum(grandezas[animales.index(animal)] for animal in escena2)
        return grandeza_total1 > grandeza_total2 or (grandeza_total1 == grandeza_total2 and escena1 > escena2)

    def ordenar_escenas_por_grandeza(escenas):
        for escena in escenas:
            for i in range(1, len(escena)):
                j = i
                while j > 0 and grandezas[animales.index(escena[j - 1])] > grandezas[animales.index(escena[j])]:
                    escena[j - 1], escena[j] = escena[j], escena[j - 1]
                    j -= 1
        return escenas

    # Ordenar las escenas en la apertura según la grandeza total y la grandeza del animal utilizando inserción
    apertura_ordenada = ordenar_escenas(apertura)
    apertura_ordenada = ordenar_escenas_por_grandeza(apertura_ordenada)

    # Ordenar las partes siguientes según la grandeza total y la grandeza del animal utilizando inserción
    partes_ordenadas = []
    for parte in partes:
        parte_ordenada = ordenar_escenas(parte)
        partes_ordenadas.append(ordenar_escenas_por_grandeza(parte_ordenada))

    # Encontrar el animal que participa en más escenas
    participacion_animales = {}
    for parte in [apertura] + partes:
        for escena in parte:
            for animal in escena:
                if animal in participacion_animales:
                    participacion_animales[animal] += 1
                else:
                    participacion_animales[animal] = 1

    max_participacion = max(participacion_animales.values())
    animales_max_participacion = [animal for animal, participacion in participacion_animales.items() if participacion == max_participacion]

     # Encontrar el animal que participa en menos escenas
    min_participacion = min(participacion_animales.values())
    animales_min_participacion = [animal for animal, participacion in participacion_animales.items() if participacion == min_participacion]
    
    # Calcular el promedio de las grandezas de todas las escenas
    suma_total_grandezas = sum(grandezas)
    promedio_grandezas = suma_total_grandezas / (m * k)

    # Imprimir la información obtenida
    print("El orden en el que se debe presentar el espectáculo es:")
    print("apertura =", apertura_ordenada)
    for i, parte in enumerate(partes_ordenadas, start=1):
        print("parte{} =".format(i), parte)
    print("El animal que participó en más escenas dentro del espectáculo fue", animales_max_participacion, "con", max_participacion, "escenas.")
    print("El animal que participó en menos escenas dentro del espectáculo fue", animales_min_participacion, "con", min_participacion, "escenas.")
    print("La escena de menor grandeza total fue la escena", apertura_ordenada[0])
    print("La escena de mayor grandeza total fue la escena", apertura_ordenada[-1])
    print("El promedio de grandeza de todo el espectáculo fue de", promedio_grandezas)

# Ejemplo de uso
animales = ["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]
grandezas = [3, 2, 1, 6, 4, 5]
apertura = [["gato", "ciempies", "libelula"], ["ciempies", "tapir", "gato"], ["tapir", "perro", "gato"], ["tapir", "nutria", "perro"]]
partes = [[["ciempies", "tapir", "gato"], ["tapir", "nutria", "perro"]], [["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]]

espectaculo_zoologico(len(animales), 3, 2, animales, grandezas, apertura, partes)

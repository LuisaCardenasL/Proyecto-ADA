import time 

def espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes):
    animales_grandezas = list(zip(animales, grandezas))
    
    # Función para ordenar las escenas según la grandeza del animal utilizando counting sort
    def ordenar_escenas(escenas):
        count = [0] * (max(grandezas) + 1)
        for escena in escenas:
            for animal in escena:
                count[grandezas[animales.index(animal)]] += 1
        
        sorted_escenas = []
        for i in range(len(count)):
            for j in range(count[i]):
                sorted_escenas.append([animal for animal in animales if grandezas[animales.index(animal)] == i])
        
        return sorted_escenas
    
    # Función para ordenar cada escena según la grandeza de los animales utilizando counting sort
    def ordenar_escenas_por_grandeza(escenas):
        sorted_escenas = []
        for escena in escenas:
            count = [0] * (max(grandezas) + 1)
            for animal in escena:
                count[grandezas[animales.index(animal)]] += 1
            
            sorted_escena = []
            for i in range(len(count)):
                for j in range(count[i]):
                    sorted_escena.append(animales[grandezas.index(i)])
            
            sorted_escenas.append(sorted_escena)
        
        return sorted_escenas
    
    # Ordenar las escenas en la apertura según la grandeza total y la grandeza del animal utilizando counting sort
    apertura_ordenada = ordenar_escenas_por_grandeza(apertura)
    
    # Ordenar las partes siguientes según la grandeza total y la grandeza del animal utilizando counting sort
    partes_ordenadas = []
    for parte in partes:
        parte_ordenada = ordenar_escenas_por_grandeza(parte)
        partes_ordenadas.append(parte_ordenada)
    
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

# Función para medir el tiempo de ejecución de espectaculo_zoologico
def medir_tiempo_espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes):
    inicio = time.time()
    espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes)
    fin = time.time()
    tiempo_total = fin - inicio
    print("La función espectaculo_zoologico se ejecutó en", tiempo_total, "segundos")

# Ejemplo de uso
n = 6
m = 3
k = 2
animales = ["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]
grandezas = [3, 2, 1, 6, 4, 5]
apertura = [["gato", "ciempies", "libelula"], ["ciempies", "tapir", "gato"], ["tapir", "perro", "gato"], ["tapir", "nutria", "perro"]]
partes = [[["ciempies", "tapir", "gato"], ["tapir", "nutria", "perro"]], [["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]]

medir_tiempo_espectaculo_zoologico(n, m, k, animales, grandezas, apertura, partes)

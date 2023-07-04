def zoo_show(n, m, k, animals, scenes):
    apertura = []
    partes = []

    for i in range(m):
        apertura.append(scenes[i])

    for i in range(m, m + k):
        partes.append(scenes[i])

    animal_counts = {}
    total_grandeur = 0

    for animal in animals:
        animal_counts[animal[0]] = 0

    for scene in apertura:
        total_grandeur += sum([animal[1] for animal in scene])
        for animal in scene:
            animal_counts[animal[0]] += 1

    for part in partes:
        total_grandeur += sum([animal[1] for animal in part])

    average_grandeur = total_grandeur / (len(apertura) + len(partes))

    max_participation = max(animal_counts.values())
    min_participation = min(animal_counts.values())

    most_participated_animals = [animal for animal, count in animal_counts.items() if count == max_participation]
    least_participated_animals = [animal for animal, count in animal_counts.items() if count == min_participation]

    scenes_apertura = ", ".join([str(scene) for scene in apertura])
    scenes_partes = [", ".join([str(scene) for scene in part]) for part in partes]

    print("Apertura: ", scenes_apertura)
    print("Parte 1: ", scenes_partes[0])
    print("Parte 2: ", scenes_partes[1])
    print("Parte 3: ", scenes_partes[2])
    print("El animal que participó en más escenas dentro del espectáculo fue: ", most_participated_animals, "que participó en", max_participation, "escenas.")
    print("El animal que menos participó en escenas dentro del espectáculo fueron: ", least_participated_animals, "que participó en", min_participation, "escenas.")
    print("La escena de menor grandeza total fue la escena", min(apertura + partes, key=lambda x: sum([animal[1] for animal in x])))
    print("La escena de mayor grandeza total fue la escena", max(apertura + partes, key=lambda x: sum([animal[1] for animal in x])))
    print("El promedio de grandeza de todo el espectáculo fue de", round(average_grandeur, 2))

# Ejemplo de uso
n = 9
m = 4
k = 3

animals = [
    ("Capibara", 1),
    ("Loro", 2),
    ("Caiman", 3),
    ("Boa", 4),
    ("Cocodrilo", 5),
    ("Cebra", 6),
    ("Pantera negra", 7),
    ("Tigre", 8),
    ("León", 9)
]

scenes = [
    [("Caiman", 3), ("Capibara", 1), ("Loro", 2)],
    [("Boa", 4), ("Caiman", 3), ("Capibara", 1)],
    [("Cocodrilo", 5), ("Capibara", 1), ("Loro", 2)],
    [("Pantera negra", 7), ("Cocodrilo", 5), ("Loro", 2)],
    [("Tigre", 8), ("Loro", 2), ("Capibara", 1)],
    [("Leon", 9), ("Caiman", 3), ("Loro", 2)],
    [("León", 9), ("Cocodrilo", 5), ("Boa", 4)],
    [("León", 9), ("Pantera negra", 7), ("Cebra", 6)],
    [("Tigre", 8), ("Cebra", 6), ("Pantera negra", 7)]
]

zoo_show(n, m, k, animals, scenes)
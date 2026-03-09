from faker import Faker

fake = Faker ("es_MX")

# 1. Declaracion de un vector vacio
ciudades_la = []

#2. Operaciones de llenado (Ciclo)
for _ in range(5):
    ciudades_la.append(fake.city())

#3 . Escritura de arreglos (Mostrar resultados)
print("\n--- DATASETDE CIUDADES GENERADO ---")
for i in range(len(ciudades_la)):
    print(f"Registro  {i+1}: {ciudades_la[i]}")
    
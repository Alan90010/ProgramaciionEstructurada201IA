peliculas_accion  = ["Mad Max", "John Wick", "Inception"]
peliculas_comedia = ["Toy Story", "Minions", "Free Guy"]
peliculas_terror  = ["It", "The Conjuring", "Saw"]

def obtener_recomendacion(genero_elegido, edad_usuario):
    if edad_usuario < 13:
        return peliculas_comedia[0]
    if genero_elegido == "accion":
        return peliculas_accion[0]
    elif genero_elegido == "comedia":
        return peliculas_comedia[0]
    elif genero_elegido == "terror":
        return peliculas_terror[0]
    else:
        return peliculas_comedia[0]

print("Agente IA de Recomendación está activo.")

edad_usuario   = int(input("Ingrese su edad: "))
genero_elegido = input("¿Qué género prefiere (accion/comedia/terror)?: ").strip().lower()

if edad_usuario < 13 and genero_elegido != "comedia":
    print("\nNota: Debido a tu edad, hemos ajustado la recomendación a contenido apto para todo público.")

pelicula = obtener_recomendacion(genero_elegido, edad_usuario)
print(f"Recomendación de la IA: {pelicula}")
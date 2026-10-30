# 1. Definir la clase Libro
class Libro:
    def __init__(self, titulo, autor, precio, disponible):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.disponible = disponible

    # Método para imprimir la información de forma legible
    def __str__(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "No disponible"
        return f"'{self.titulo}' de {self.autor} - Q{self.precio} ({estado})"


# 2. Crear una lista con 5 objetos de tipo Libro (con los nuevos nombres)
libros = [
    Libro("Aprendido a programar", "Julio Cortázar", 135, True),
    Libro("El Memo", "Paulo Coelho", 95, True),
    Libro("Crónica de una muerte", "García Márquez", 105, False),
    Libro("la mente", "Juan Rulfo", 90, True),
    Libro("La sombra del viento", "Carlos Ruiz Zafón", 140, False)
]

# 3. Recorrer la lista e imprimir todos los libros
print("--- Lista inicial de libros ---")
for libro in libros:
    print(libro)

print("\n" + "="*40 + "\n")

# 4. Calcular e imprimir el precio total de todos los libros
precio_total = 0
for libro in libros:
    precio_total = precio_total + libro.precio

print(f"El precio total de todos los libros es: Q{precio_total}")

# 5. Contar e imprimir cuántos libros están disponibles (disponible == True)
disponibles_contador = 0
for libro in libros:
    if libro.disponible == True:
        disponibles_contador = disponibles_contador + 1

print(f"Cantidad de libros disponibles: {disponibles_contador}")

print("\n" + "="*40 + "\n")

# 6. Agregar un nuevo libro a la lista usando .append()
nuevo_libro = Libro("calculo", "José", 130, True)
libros.append(nuevo_libro)

# 7. Volver a imprimir la lista completa
print("--- Lista actualizada de libros ---")
for libro in libros:
    print(libro)
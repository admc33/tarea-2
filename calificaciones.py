num_estudiantes = int(input("¿Cuántos estudiantes hay en la clase? "))

calificaciones = [18, 20 ,30, 44, 53]

for i in range(num_estudiantes):
    calificacion = float(input(f"Ingrese la calificación del estudiante {i + 1}: "))
    calificaciones.append(calificacion)

suma_calificaciones = sum(calificaciones)

promedio_calificaciones = suma_calificaciones / num_estudiantes

calificacion_mas_alta = max(calificaciones)
calificacion_mas_baja = min(calificaciones)

print("Resultados:")
print(f"Suma de las calificaciones: {suma_calificaciones}")
print(f"Promedio de las calificaciones: {promedio_calificaciones:.2f}")
print(f"Calificación más alta: {calificacion_mas_alta}")
print(f"Calificación más baja: {calificacion_mas_baja}")
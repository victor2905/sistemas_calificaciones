print("-------Sistema de calificaciones--------")
nombre_estudiante = input("Favor ingrese su nombre: ")
print("Ingrese sus calificaciones")
matematicas = float(input("Matemáticas: "))
quimica = float(input("Química: "))
ingles = float(input("Inglés: "))
programacion = float(input("Programación: "))

promedio = (matematicas + quimica + ingles + programacion)/4

if promedio > 6.5:
    print("Felicitaciones " + nombre_estudiante + " aprobaste con un promedio de: " ,promedio)

else:
    print("Lo sentimos " + nombre_estudiante + "no aprobaste, tu promedio es de: " ,promedio)


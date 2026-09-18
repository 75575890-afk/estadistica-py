# Calculadora de estadisticas basicas
# Eduardo Puma Ccorimanya

def calcular_estadisticas(numeros):
    cantidad = len(numeros)
    suma = sum(numeros)
    promedio = suma / cantidad
    minimo = min(numeros)
    maximo = max(numeros)

    return cantidad, suma, promedio, minimo, maximo


entrada = input("Ingrese numeros separados por espacios: ")

try:
    numeros = [float(numero) for numero in entrada.split()]
except ValueError:
    print("Error: ingrese solo valores numericos.")
    exit()

if not numeros:
    print("Error: no ingreso ningun numero.")
    exit()

print(f"\nNumeros ingresados: {numeros}")

cantidad, suma, promedio, minimo, maximo = calcular_estadisticas(numeros)

print("\n--- Estadisticas ---")
print(f"Cantidad: {cantidad}")
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
print(f"Minimo: {minimo}")
print(f"Maximo: {maximo}")

print("\nPrograma finalizado correctamente.")
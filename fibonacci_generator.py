# fibonacci_generator.py

def fibonacci_list(n: int) -> list:
    numbers = [0, 1]
    for i in range(n - 2):
        numbers.append(int(numbers[i] + numbers[i + 1]))
        phi_estimation = numbers[-1] / numbers[-2]
        print(f"Estimación de Phi después de {len(numbers)} números: {phi_estimation}")
    return numbers

def fibonacci_index(n: int) -> int:
    numbers = [0, 1]
    for i in range(n - 2):
        numbers.append(int(numbers[i] + numbers[i + 1]))
    return numbers[n - 1]

while True:
    choice = input("¿Quieres obtener un número específico de la secuencia de Fibonacci (1) o una lista de números (2)? (Escribe 'x' para salir): ")
    if choice.lower() == 'x':
        print("Saliendo del programa.")
        break
    elif choice == '1':
        index = input("¿Qué índice de la secuencia de Fibonacci quieres obtener? ")
        while not index.isdigit() or int(index) <= 0:
            index = input("Por favor, ingresa un número entero positivo: ")
        print(f"El número en el índice {index} de la secuencia de Fibonacci es: {fibonacci_index(int(index))}")
    elif choice == '2':
        cant = input("Cuantos numeros de la secuencia de Fibonacci quieres generar? ")
        while not cant.isdigit() or int(cant) <= 0:
            cant = input("Por favor, ingresa un número entero positivo: ")
        print(f"Esta es la sacuencia de Fibonacci entera hasta con {cant} numeros: {fibonacci_list(int(cant))}")

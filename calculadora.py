def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    return a / b
def potencia(a, b):
    return a ** b
def main():
    print("=== Calculadora sencilla ===")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print(f"Suma: {sumar(a, b)}")
    print(f"Resta: {restar(a, b)}")
    print(f"Multiplicación: {multiplicar(a, b)}")
    print(f"División: {dividir(a, b)}")
    print(f"Potencia: {potencia(a, b)}")
    print("=== Fin de la calculadora ===")

if __name__ == "__main__":
    main()


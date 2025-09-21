print("*** Tabla de multiplicar ***")

numero = int(input("Ingresa un número: "))

for i in range(10):
    print(f"{numero} x {i+1} = {(i+1)*numero}")
print("*** Paridad  y signo ***")

numero = int(input("Digita un número entero: "))

if numero % 2 == 0:
    par = "par"
else: 
    par = "impar"
    
if numero < 0:
    positivo= "negativo"
elif numero == 0:
    positivo = "Cero"
else:
    positivo= "positivo"

print(f"El numero: {numero}, es {positivo} y ademas es {par}")
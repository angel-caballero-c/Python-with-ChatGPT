def  main():
    print("*** Calculadora de ma IMC ***\n")
    peso = float(input("¿Cual es tu peso en kg?: "))
    altura = int(input("¿Cual es tu altura en cm?: "))


    if peso > 0 and altura > 0:
        imc = peso/((altura/100)**2)
        print(f"\nTu IMC es: {round(imc, 2)}\n")
        if imc < 18.5:
            print(">>>> Estas baj@ de peso")
        elif imc < 24.9:
            print(">>>> Estas normal de peso")
        elif imc < 29.9:
            print(">>>> Tienes sobre peso")
        elif imc < 34.9:
            print(">>>> Tienes obecidad tipo 1")
        elif imc < 39.9:
            print(">>>> Tienes obecidad tipo 2")
        elif imc < 30:
            print(">>>> Tienes obecidad tipo 3")
        print()
    else:
        print("\nERROR. Iniciaremos de nuevo la ejecución\n")
        main()
main()
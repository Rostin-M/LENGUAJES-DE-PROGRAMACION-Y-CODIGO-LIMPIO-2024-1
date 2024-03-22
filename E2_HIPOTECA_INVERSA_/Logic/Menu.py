import Calculations as C

def Menu():
    print("╔═══════════════════════════════════════════════════╗")
    print("║    Bienvenido al Simulador de Hipoteca Inversa    ║")
    print("╠═══════════════════════════════════════════════════╣")
    print("║                                                   ║")
    print("║  Por favor, proporcione la siguiente información: ║")
    print("║                                                   ║")
    print("╠═══════════════════════════════════════════════════╣")
    print(" ")
    
    # Solicitar datos del usuario
    gender = input("Género [M/F]: ")
    age = int(input("Edad: "))
    total_amount = float(input("Valor de la casa: "))
    interest_rate = float(input("Tasa de interés deseada (%): "))
    interest_housing = float(input("Valor de interés sobre la vivienda: "))
    quotas = int(input("Número de cuotas deseadas: "))

    print("╠═══════════════════════════════════════════════════╣")
    print("║                                                   ║")
    print("║  Seleccione una opción:                           ║")
    print("║     1. Hipoteca Vitalicia                         ║")
    print("║     2. Hipoteca Temporal                          ║")
    print("║     3. Hipoteca Única                             ║")
    print("║                                                   ║")
    print("╣═══════════════════════════════════════════════════╣")

    type_mortgage = input("\nIngrese su elección: ")

    print("\n")

    if type_mortgage == "1":
        print("Calculando Hipoteca Vitalicia...")
        C.MortgageLifetimeInverse(total_amount, interest_rate, quotas, interest_housing)
    elif type_mortgage == "2":
        print("Calculando Hipoteca Temporal...")
        C.MortgageTemporaryReverse(total_amount, interest_rate, quotas, interest_housing)
    elif type_mortgage == "3":
        print("Calculando Hipoteca Única...")
        C.MortgageSingleReverse(total_amount, interest_rate, quotas, interest_housing)
    else:
        print("¡Opción no válida! Por favor, seleccione una opción válida.")
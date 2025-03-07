def calculadora():
    print("Calculadora en Python")
    
    try:
        num1 = float(input("Introdueix el primer número: "))
        operador = input("Introdueix l'operador (+, -, *, /): ")
        num2 = float(input("Introdueix el segon número: "))
        
        if operador == '+':
            resultat = num1 + num2
        elif operador == '-':
            resultat = num1 - num2
        elif operador == '*':
            resultat = num1 * num2
        elif operador == '/':
            if num2 != 0:
                resultat = num1 / num2
            else:
                print("Error: Divisió per zero no permesa.")
                return
        else:
            print("Error: Operador no vàlid.")
            return
        
        print(f"Resultat: {resultat}")
    
    except ValueError:
        print("Error: Entrada no vàlida. Si us plau, introdueix números vàlids.")

if __name__ == "__main__":
    calculadora()

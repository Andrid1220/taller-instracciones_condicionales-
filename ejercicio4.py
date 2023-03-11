altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / altura ** 2

if imc < 16:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Criterio de ingreso en hospital")
elif 16 <= imc < 17:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Infrapeso")
elif 17 <= imc < 18:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Bajo peso")
elif 18 <= imc < 25:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Peso normal (saludable)")
elif 25 <= imc < 30:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Sobrepeso (obesidad grado I)")
elif 30 <= imc < 35:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Sobrepeso crónico (obesidad grado II)")
elif 35 <= imc < 40:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Obesidad premórbida (obesidad grado III)")
else:
    print("Su índice de masa corporal es:", imc)
    print("Su diagnóstico es: Obesidad mórbida (obesidad de grado IV)")
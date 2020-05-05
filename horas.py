try:    
    horas = float(input("Introduca las Horas: "))
    tarifa = float(input("Introduzca la Tarifa por Hora: "))
    deuda = 0
    ext_tarifa = 0
    ext_deuda = 0
    extras = horas - 40

    if extras > 0:
        ext_tarifa = extras * (tarifa * 1.5 )
        print(f"Usted ha trabajado {extras} horas extras")
    elif extras < 0:
        deuda = 40 - horas
        ext_deuda = deuda * tarifa
        print(f"Usted adeuda {deuda} horas")
    else:
        print("Usted no tiene horas extras")
    salario_bruto = 40 * tarifa
    salario = salario_bruto + ext_tarifa - ext_deuda
    print(f"Su Salario será: {salario}")
except:
    print("Por favor introduzca un numero")
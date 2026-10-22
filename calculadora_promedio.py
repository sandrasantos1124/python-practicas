print('----Calculadora de Promedio----')

nota1 = float(input('ingrese nota1: '))
nota2 = float(input('ingrese nota2: '))
nota3 = float(input('ingrese nota3: '))
 
promedio = (nota1 + nota2 + nota3) / 3
print(f"Su promedio es:{promedio:.1f}")

if promedio >= 51:
    print('Aprobo! Felicidades, Lic. Sandra!')
else:
    print('Reprobó, pero a seguir intentando'

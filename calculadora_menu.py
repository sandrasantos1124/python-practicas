print('1. Suma')
print('2. Restar')
print('3. Multiplicar')
print('4. División')
opcion= int(input('Elija una opción: '))
a=int(input('Ingrese el primer numero: '))
b=int(input('Ingrese el seguno numero: '))
if opcion==1:
  print(f'La suma es: {a+b}')
elif opcion==2:
  print(f'La resta es: {a-b}')
elif opcion==3:
  print(f'La multiplicacion es: {a*b}')
elif opcion==4:
  print(f'La división es: {a/b}')
else:
  print('opción no valida')

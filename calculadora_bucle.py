while True:
  print ('1: Suma')
  print ('2: Resta')
  print ('3: Multiplicar')
  print ('4: División')
  print ('5: Salir')

  opcion=int(input('Elija una opcion:'))
  if opcion==5:
    print ('chao Sandra')
    break

  a=int(input('Ingrese primer número: '))
  b=int(input('Ingrese segundo número: '))
  if opcion==1: 
     print('La suma es: ', a+b)
  if opcion==2:
     print('La resta es: ',a-b)
  if opcion==3:
     print('La multiplicacion es: ',a*b)
  if opcion==4:
     print(f"La división es: {a/b}")

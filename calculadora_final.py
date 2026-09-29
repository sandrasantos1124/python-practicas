while True:
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Salir')
    
    try:
      opcion=int(input('Elija una opción: '))
    except ValueError:
      print('ingrese solo numero del 1 al 5')
      continue

    if opcion==5:
        print('chao Sandra') 
        break
    if opcion < 1 or opcion > 5:
      print('Opcion no válida, elija del 1 al 5')
      continue
    try:  
      a=int(input('Ingrese el primer número: '))
      b=int(input('Ingrese el segundo número: '))    
    except ValueError:
      print ('Error, debe ingresar solo numeros')
      continue
        
    if opcion ==1:
        print('La suma es: ', a+b)
    elif opcion ==2:
        print('La resta es: ',a-b)
    elif opcion==3:
        print('La multiplicacion es: ', a*b)
    elif opcion==4:
        if b==0:
            print('No se puede dividir entre cero')
        else:
            print('La division es:',a/b)

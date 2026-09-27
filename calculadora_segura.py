while True:
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Salir')

    opcion=int(input('Elija una opción: '))

    if opcion==5:
        print('chao Sandra') 
        break
  
    a=int(input('Ingrese el primer número: '))
    b=int(input('Ingrese el segundo número: '))    
  
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
    else:  
        print('Opcion no válida, elija del 1 al 5')

import random
secreto= random.randint(1,10)
intentos=3
print("!Adivine del 1 al 10! Tiene 3 intentos")

while intentos > 0:
    try:
        numero=int(input(f'Le quedan {intentos}  intentos '))
    
        if numero== secreto:
            print("Bravo !Gano Lic. Sandra")
            break
        elif  numero < secreto:
              print("Mas alto..")
        else:
             print("Mas bajo..")
        intentos = intentos-1
    except:
      print ('por favor, solo numeros')

if intentos==0:
    print(f"se acabaron los intentos. Era el {secreto}")

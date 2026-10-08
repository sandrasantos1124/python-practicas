import random
secreto= random.randint(1,10)
print('!Hola Li. Sandra! Adivine el número del 1 al 10')
intento=int(input("Su número: "))
if intento==secreto:
  print(f"¡BRAVO! ¡Adivinó! Era el {secreto} 🎉")
else:
  print(f"Casi! Yo pense en el {secreto} intentemos mañana de nuevo")

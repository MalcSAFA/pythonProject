frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")
contador = 0
for i in frase:
    if i == letra:
        contador += 1

print("La letra " + str(letra) + " aparece " + str(contador) + " en la frase " + str(frase))

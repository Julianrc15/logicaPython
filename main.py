
nivelAgua= int(input("Digite la cantidad de agua de la represa: "))
print(f"El nivel de agua es: {nivelAgua}")

if (nivelAgua<200):
    print(f"el nivel de agua es bajo")
elif (nivelAgua>=200 and nivelAgua<450):
    print(f"Niveles de agua estables")
else:
    print(f"Necesario abrir las compuertas...")
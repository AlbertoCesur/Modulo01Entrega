palabra = input("Que palabra ")
intentos = int(input("Intentos "))
print("---------------------")
listanum = []
listalet = []
listapal = []
b = False
lon = int(len(palabra))
while b is not True:
    long = int(input("¿Cuanto mide? "))
    listanum.append(long)
    if intentos == 0:
        print("Se terminaron los intentos")
        print("---------------------")
        print("Intentod de numeros | {} ".format(listanum))
        print("Lista letra         | {} ".format(listalet))
        print("Lista de palabras   | {} ".format(listapal))
        print("---------------------")
        break
    elif long == lon:
        print("Felicidades es {}".format(lon))
        b = True
    elif long > lon:
        intentos = intentos - 1
        print("l{} can {} ios".format(long, intentos))
    else:
        intentos = intentos - 1
        print("{}{} i".format(long, intentos))

b = False
# LETRAS
validar = ""
letrasalamacenadas = ""
while b is not True:
    if intentos == 0:
        print("Se terminaron los intentos")
        print("---------------------")
        print("Intentod de numeros | {} ".format(listanum))
        print("Lista letra         | {} ".format(listalet))
        print("Lista de palabras   | {} ".format(listapal))
        print("---------------------")
        break
    letrasalamacenadas = ""
    selec = input("letra 1 o palabra 0")
    if selec == "1":
        if intentos == 0:
            print("Se terminaron los intentos")
            print("---------------------")
            print("Intentod de numeros | {} ".format(listanum))
            print("Lista letra         | {} ".format(listalet))
            print("Lista de palabras   | {} ".format(listapal))
            print("---------------------")
            break
        let = input("¿Letra?")
        listalet.append(let)
        if let in palabra:
            for a in palabra:
                if a in listalet:
                    letrasalamacenadas = letrasalamacenadas + a
                else:
                    letrasalamacenadas = letrasalamacenadas + "*"
        else:
            intentos = intentos - 1
            print("La palabra no tiene {} te quedan {} intentos".format(let, intentos))

        print(letrasalamacenadas)
    # palabras
    if selec == "0":
        if intentos == 0:
            print("Se terminaron los intentos")
            print("---------------------")
            print("Intentod de numeros | {} ".format(listanum))
            print("Lista letra         | {} ".format(listalet))
            print("Lista de palabras   | {} ".format(listapal))
            print("---------------------")
            break
        pal = input("¿palabra? ")
        listapal.append(pal)
        if pal == palabra:
            print("{}".format(palabra))
            print("---------------------")
            print("Intentod de numeros | {} ".format(listanum))
            print("Lista letra         | {} ".format(listalet))
            print("Lista de palabras   | {} ".format(listapal))
            print("---------------------")
            print("te sobra {} intentos".format(intentos))
            break
        else:
            intentos -= 1
            print("No es {} te quedan {} intentos".format(pal, intentos))

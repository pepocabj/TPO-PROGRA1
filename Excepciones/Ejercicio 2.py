cadena_1 = ""
cadena_2 = ""
letra = "abcdefghijklmnñopqrstuvwxyz"
def cadena (cadena_1, cadena_2):
    try:
        cadena_1 = float(input("Ingrese un numero real"))
        cadena_2 = float(input("Ingrese un numero real"))
    except ValueError:
        print(-1)
    resultado = cadena_1 + cadena_2
    return resultado
        
print(cadena (cadena_1, cadena_2))


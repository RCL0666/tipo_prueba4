#diccionario vacio 
estudiantes ={} 


# registro de estudiantes por nombre y  validacion de nombre

def resgistrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante:")
    
    if any(i['nombre'].lower()==nombre.lower() for i in estudiantes.values()):
            print( "ERROR: El estudiante ya existe")
    # se pide al usuario su edad yse valida que este en el rango         
    try:
        edad = int(input("Ingrese la edad del estudiante:"))
        if edad<12 or edad>80:
            print("ERROR: la edad debe estar entre 12 y 80")
            return
    except ValueError:
        print("ERROR: ingrese numeros enteros positivos")


    genero=input("Ingrese el genero del estudiante M/F:").strip().upper()
    if genero not in ['M','F']:
        print("ERROR: genero incorrecto")
        return
    
#diccionario vacio 
estudiantes ={} 




def resgistrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante:")
    
    if any(i['nombre'].lower()==nombre.lower() for i in estudiantes.values()):
            print( "ERROR: El estudiante ya existe")
     
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
    
    codigo=input("Ingrese el codigo del estudiante(debe ser unico,6 caracteres y alfanumerico:)")
    if len(codigo)!=6 or not codigo.isalnum() or codigo in estudiantes:
        print("ERROR: codigo incorrecto, debe ser unico , 6 caracteres y alfanumerico")
        return

    try:
        promedio = float(input("Ingrese el promedio del estudiante (1.0 - 7.0):"))
        if promedio<1.0 or promedio>7.0:
            print("ERROR: el promedio debe estar entre 1.0 y 7.0")
            return
    except ValueError:
        print("ERROR: promedio invalido intente nuevamente")
        return
    
    estudiantes[codigo]={
        'nombre':nombre,
        'edad':edad,
        'genero':genero,
        'promedio':promedio
    }
    print("Estudiante registrado con exito")
    
    
    def buscar_estudiante():
        dato = input("ingrese el codigo del estudiante:").strip()
        for codigo,est in estudiantes.items():
            if est['nombre'].lower()==dato.lower() or codigo==dato:
                print(f"nombre: {est[nombre]}")
                print(f"edad: {est[edad]}")
                print(f"genero: {est[genero]}")
                print(f"promedio: {est[promedio]}")
                print(f"codigo:{codigo}")
                return
        print("ERROR: Estudiante no encontrado")
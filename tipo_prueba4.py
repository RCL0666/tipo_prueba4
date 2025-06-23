#diccionario vacio 
estudiantes ={} 


# registro de estudiantes por nombre y  validacion de nombre

def resgistrar_estudiante():
    nombre = input("Ingrese el nombre del estudiante:")
    
    if any(i['nombre'].lower()==nombre.lower() for i in estudiantes.values()):
            print( "ERROR: El estudiante ya existe")
  


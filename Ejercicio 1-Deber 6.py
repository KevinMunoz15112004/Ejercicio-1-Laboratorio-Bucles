#Bucle con for ejercicio 1 
#Declarando las variables a utilizar
respuesta = 0
correo = "usuario123@gmail.com"
#Utilizando el bucle FOR 
for i in range(1,4):
    print(f"¿El taller {i} presenta fugas de gas?")
    contabilizacion = input("si/no: ")
    if contabilizacion == "si":
        respuesta += 1
#Imprimiendo la condicion if 
if respuesta > 1:
    print(f"¡ALERTA! Un mensaje de alta importancia ha sido enviado a su correo: {correo}")
    
    

































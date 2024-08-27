import random
def juego_adivinanza ():
    #generar un numero del 1 al 100
    numero_secreto = random.randint(1,100)
    intentos = 0
    adivinado = False
    
    #Primeras lineas del juego donde se da la bienvenida
    print("Bienvenidos al juego de adivinanza de numeros")
    print("Debes adivinar un numero entre el 1 y el 100")
    print("Intenta adivinarlo!")
    
    while not adivinado:
        #pedir al usuario que ingrese un numero
        adivinanza = input("introduzca un numero del 1 al 100: ")
        
        #Verificar que la entrada sea un numero
        if adivinanza.isdigit():
            adivinanza = int(adivinanza) # se convierte de texto a entero
            intentos += 1 # se suma 1 a los intentos
            
            if adivinanza < numero_secreto:
                print("El numero que has introducido es menor que el numero secreto")
            elif adivinanza > numero_secreto:
                print("El numero que has introducido es mayor que el numero secreto")
            else:
               # se acaba el juego
                print(f"Felicitaciones has ganado! el numero {adivinanza} es el secreto y lo has logrado en {intentos} intentos")
                
        else:
            print("Debes introducir un numero valido entre 1 y 100")
            
juego_adivinanza()
import sys
import os
import time
import random


def Selector(Opcion1, Opcion2):
    res = 0
    while res != '1' and res != '2':
        print("Que eliges?\nOpcion A -", Opcion1)
        print("Opcion B -", Opcion2)

        res = input("A = 1, B = 2\n\n --> ")
        if res == "1":
            print("Has elegido opcion A")
        elif res == "2":
            print("Has elegido opcion B")
        else:
            print("Opcion invalida")
    time.sleep(2)
    os.system("cls")
    return res


def MenuCombate(Vida, Nombre, DeterminacionCombate, Almuerzo):
    VidaEnemiga = random.randint(1, 8)
    Turno = 0
    print("\nHas iniciado un combate contra ", Nombre)
    while Vida >= 0 or VidaEnemiga >= 0:
        Turno = Turno + 1
        print(f""" Que haces?
      1- Golpear
      2- Correr
      3- Curar""")
        print("\nVida : " + "#"*Vida)
        print(f"Vida de {Nombre}: " + "#"*VidaEnemiga)
        DecisionDeCombate = input("\n -> ")
        if DecisionDeCombate == '1':
            if Turno == 1:
                print(f'Golpeas a "{Nombre}" sin pensarlo\n')
            elif Turno > 1:
                print(f'Has golpeado a "{Nombre}\n"')
            Damage = random.randint(1, 3) + DeterminacionCombate
            print(f"Has hecho {Damage} de daño a {Nombre}\n")
            if Damage < 4:
                print("\nDemonios, ese golpe si que debio doler")
            VidaEnemiga = VidaEnemiga - Damage
            if (VidaEnemiga <= 0):
                print(f"{Nombre} queda fuera de combate")
                return Vida
            print(f"Es el turno de {Nombre} para atacar")
            Damage = random.randint(1, 3)
            print(f"Has recibido {Damage} de daño")
            if Damage == 3:
                print("\nVeo que se desquito de ese golpe")
            Vida = Vida - Damage
            if Vida <= 0:
                print(
                    f"Parece que ese golpe ha sido mas de lo que puedes soportar, quedas fuera de combate")
        elif DecisionDeCombate == '2':
            if Turno == 1:
                if VidaEnemiga > 3:
                    print(
                        f"{Nombre} no parece tener intenciones de dejarte escapar")
                elif VidaEnemiga <= 3:
                    print(
                        f"{Nombre} no tiene tantas ganas de pelear que digamos, por lo que accede a dejarte pasar sin mas")
            if Turno >= 2:
                if VidaEnemiga > 3:
                    print(
                        f"{Nombre} Aun tiene muchas energias, escapar no es una opcion")
                elif VidaEnemiga <= 3:
                    print(
                        f"{Nombre} parece cansado, a lo que no parece tener intenciones de seguirte si escapas")
                    print(f"Has escapado exitosamente!")
                    VidaEnemiga = 0
                    return Vida
        elif DecisionDeCombate == '3':
            if Almuerzo >= 1:
                print("Has recuperado 5 puntos de vida")
                Vida = Vida + 5
            else:
                print(
                    "Lo siento, parece que no tienes con que curarte, a la proxima prueba con comida0")


def Acertijo(Nombre):
    print(f"{Nombre} te reta a un acertijo")
    Dato = [random.randint(1, 9), random.randint(1, 5), random.randint(1, 10)]
    print(f"Cuanto es {Dato[0]} * {Dato[1]} + {Dato[2]}")
    Respuesta = Dato[0] * Dato[1] + Dato[2]
    TuRespuesta = int(input("\n\t-> "))
    if Respuesta == TuRespuesta:
        print("Correcto")
        return True
    elif Respuesta != TuRespuesta:
        print("Incorrecto")
        return False


print("""
██╗████████╗██╗░██████╗        ░█████╗░        ██████╗░██╗░░░██╗░█████╗░██╗░░██╗░█████╗░
██║╚══██╔══╝╚█║██╔════╝        ██╔══██╗        ██╔══██╗██║░░░██║██╔══██╗██║░██╔╝██╔══██╗
██║░░░██║░░░░╚╝╚█████╗░        ███████║        ██║░░██║██║░░░██║██║░░╚═╝█████═╝░╚═╝███╔╝
██║░░░██║░░░░░░░╚═══██╗        ██╔══██║        ██║░░██║██║░░░██║██║░░██╗██╔═██╗░░░░╚══╝░
██║░░░██║░░░░░░██████╔╝        ██║░░██║        ██████╔╝╚██████╔╝╚█████╔╝██║░╚██╗░░░██╗░░
╚═╝░░░╚═╝░░░░░░╚═════╝░        ╚═╝░░╚═╝         ╚═════╝░░╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░                                                                          
                                                                                        
                                            ██████████                                  
                                          ██░░░░░░░░░░██                                
                                        ██░░░░░░░░░░░░░░██                              
                                        ██░░░░░░░░████░░██████████                      
                            ██          ██░░░░░░░░████░░██▒▒▒▒▒▒██                      
                          ██░░██        ██░░░░░░░░░░░░░░██▒▒▒▒▒▒██                      
                          ██░░░░██      ██░░░░░░░░░░░░░░████████                        
                        ██░░░░░░░░██      ██░░░░░░░░░░░░██                              
                        ██░░░░░░░░████████████░░░░░░░░██                                
                        ██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░██                              
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                            
                        ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                              
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░██                                
                            ██████░░░░░░░░░░░░░░░░████                                  
                                  ████████████████       
                                  
                                 Preciona Enter para iniciar                                   
""")
tecla = sys.stdin.read(1)
os.system("cls")

Almuerzo = 0
Determinacion = 0
Vida = 10
Respuesta = False

print("Estas leyendo este texto, pero supongamos que escuchas una explosion, vas o te alejas?")

Decision = Selector('Vas a ver que produjo el "Sonido"',
                    'Te alejas porque puede ser peligroso')

if Decision == "2":
    print("Te alejas porque puede ser peligroso")
    time.sleep(3)
    print("QUE ABURRIDO ERES, NI SI QUIERA INICIO EL JUEGO Y YA TE ESTAS ECHANDO HACIA ATRAS!")
    print("Iras de igual forma, pero descuida, solo por esta ves te obligare a tomar una decision")


print("Caminas unos pocos segundos hacia el sonido, pero de inmediato sientes un aroma peculiar, a lo que recuerdas "
      "que dejaste la estufa prendida")
Decision = Selector("Vas a revisar la estufa?",
                    "Sigues adelante para investigar")

if Decision == "1":
    print("Efectivamente la estufa estaba prendida, afortunadamente llegaste a tiempo "
          "y no se quemo, por lo que puedes disfrutar de un buen almuerzo gracias a tu prudencia"
          "\n		-Se ha agregado almuerzo a tu inventario-")
    Almuerzo = Almuerzo + 1
elif Decision == "2":
    print("Dejando a un lado lo irresponsable que eres, sigues determinado a ver que produjo el sonido")
    print('\nParece que tienes algo de "Determinacion"')
    Determinacion = Determinacion + 1
print("--Caminas hasta llegar a un bosque sospechosamente bien cuidado--")

Decision = Selector("Entrar al bosque",
                    "Estamos en Latam, esas cosas no existen! Decides retirarte por miedo a que encuentres adentro")

if Decision == "1":
    print("Tu instinto de allanamiento a la propiedad privada se activa, y continuas determiando a averiguar que causa el sonido, p.d: No programe mas")
    Determinacion = Determinacion + 1
    print("--Ves un grupo de personas con mascaras de animales a lo lejos, que haces?--")
    Decision = Selector("Aguas, son furros, salgo corriendo de ahi",
                        "Vas a ver de manera muy irresponsable que pueden estar haciendo sabiendo que estas en medio de un bosque que posiblemente es propiedad privada")
    if Decision == "1":
        print("En la vida a veces hay que ser precavido")
        print("Sales del bosque, pero miras a alguien alguien acercarse a ti")
        Vida = MenuCombate(Vida, "El sucio bob", Determinacion, Almuerzo)
        if Vida <= 0:
            print("\n\n\tGAME OVER")
            exit()
    elif Decision == "2":
        print("Pasas junto a ellos fingiendo demencia, pero se ven buenas personas, quizas deberiamos dejar nuestros prejucios a un lado de ves en cuando")
        print("Desafortunadamente te vuelves furro luego de eso")
        print("Vuelves a escuchar el sonido, y ves un arbusto el cual parece estar produciendolo")
        Determinacion = Determinacion + 1
        Decision = Selector("Revisas el arbusto, aunque sea peligroso",
                            "Esperas un poco a ver que pasa")
        if Decision == "1":
            print("Escuchas una fuerte explosion justo antes de revisar el arbusto")
            print(
                "De este sale nada mas ni nada menos que un patito, pero parece agresivo")
            Determinacion = Determinacion + 1
            Vida = MenuCombate(Vida, "Un patito tactico",
                               Determinacion, Almuerzo)
            if Vida <= 0:
                print("\n\n\tGAME OVER")
                exit()
            print(
                "Felicidades, has logrado encontrar el origen del sonido, y has completado el juego")
        elif Decision == "2":
            print("Esperas un momento y de la nada sale un patito del arbusto, se ve muy inteligente, y se aproxima a ti")
            Respuesta = Acertijo("Un patito")
            if Respuesta == True:
                print(
                    "Has logrado resolver el acertijo del patito, como recompensa te lo puedes llevar de mascota, gracias por jugar")
            elif Respuesta == False:
                print(
                    "Bueno, no siempre se gana, aun asi felicidades por llegar al final del juego y gracias por jugar")
elif Decision == "2":
    print("Estamos en Latam, esas cosas no existen! Decides retirarte por miedo a que encuentres adentro\n")
    print("Pues valiste queso, ahora tendras un combate obligatorio, quien diria que el bosque en realidad era seguro?\n")
    Vida = MenuCombate(Vida, "El sucio bob", Determinacion, Almuerzo)
    if Vida <= 0:
        print("\n\n\tGAME OVER")
        exit()
    print("Luego de esa pelea, planeas entrar a una escuela de boxeo para mejorar tus habilidades de combate, veremos que pasara en el proximo juego, gracias por jugar")

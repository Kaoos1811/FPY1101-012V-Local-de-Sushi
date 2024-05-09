import os
import time
Limpieza_Pantalla = "cls"
boleta = 0
pika = 4500
otaku = 5000
pulpo = 5200
anguila = 4800
menu = 0
menu2 = 0
menu3 = 0
cant_roll_1 = 0
cant_roll_2 = 0
cant_roll_3 = 0
cant_roll_4 = 0
descuentofinal = 0
os.system(Limpieza_Pantalla)

while menu == 0:
    time.sleep(1)
    print("\t*Bienvenido a tenkati Sushi Rolls*\n")
    print(f"1)Pikachu Roll: {pika}")
    print(f"2)Otaku Roll: {otaku}")
    print(f"3)Pulpo Venenoso Roll: {pulpo}")
    print(f"4)Anguila Electrica: {anguila}")
    respuesta=int(input("Selecciona del 1 al 4: "))
    if respuesta == 1:
        cant_roll_1 = int(input("Cantidad: "))
        boleta += (cant_roll_1 * pika)
        try:
            salida = int(input("Quieres agregar otro roll\n1)Si\n2)No\n: "))
            if salida == 1:
                menu = 0
            elif salida == 2:
                menu2 = 1
        except ValueError:
            print("Presione 1 para continuar o 2 para salir")
    elif respuesta == 2:
        cant_roll_2 = int(input("Cantidad: "))
        boleta += (cant_roll_2 * otaku)
        try:
            salida = int(input("Quieres agregar otro roll?\n1)Si\n2)No\n: "))
            if salida == 1:
             menu = 0
            elif salida == 2:
             menu2 = 1
            
        except ValueError:
            print("Presione 1 para continuar o 2 para salir")
    elif respuesta == 3:
        cant_roll_3 = int(input("Cantidad: "))
        boleta += (cant_roll_3 * pulpo)
        try:
            salida = int(input("Quieres agregar otro roll?\n1)Si\n2)No\n: "))
            if salida == 1:
             menu = 0
            elif salida == 2:
             menu2 = 1
            
        except ValueError:
            print("Presione 1 para continuar o 2 para salir")
    elif respuesta == 4:
        cant_roll_4 = int(input("Cantidad: "))
        boleta += (cant_roll_4 * anguila)
        try:
           salida = int(input("Quieres agregar otro roll?\n1)Si\n2)No\n: "))
           if salida==1:
              menu = 0
           elif salida==2:
              menu2 = 1
        except ValueError:
           print("Presione 1 para continuar o 2 para salir")
    else:
        print("Ingrese una opción valida")
    while menu2 == 1:
            descuento = input("Ingresa un dcto:")
            if  descuento == "Soyotaku":
                descuentofinal = boleta*0.10
                menu3 = 1
            elif descuento == 1:
                menu3 = 1
            else:
                salidamenu2 = input("Codigo no valido, deseas intentarlo de nuevo?\n1)Si\n2)No\n: ")
                if salidamenu2 == 1:
                    menu2 = 1
                elif menu2 == 1:
                    menu3 = 1
                else:
                    print("Ingresa 1 si quieres volver a intentarlo o 2 para salir")
                    break
                
            while menu3 == 1:
                os.system(Limpieza_Pantalla)
                cant_total = (cant_roll_1, + cant_roll_2, + cant_roll_3, + cant_roll_4)
                print("**************************************************")
                print(f"\t TOTAL DE PRODUCTOS{cant_total}")
                print(f"\t Pikachu Roll:{cant_roll_1}")
                print(f"\t Otaku Roll:{cant_roll_2}")
                print(f"\t Pulpo Venenoso Roll:{cant_roll_3}")
                print(f"\t Anguila Electrica Roll:{cant_roll_4}")
                print("**************************************************\n")
                print(f"\t Subtotal a pagar: ${boleta}")
                print(f"\t Descuento aplicado: ${descuentofinal}")
                print(f"\t TOTAL A PAGAR: ${boleta-descuentofinal}")
                print(f"**************************************************")
                salidafinal = int(input("Deseas realizar otro pedido?:\n1)Si\n2)No\n: "))
                if salidafinal == 1:
                    cant_roll_1 = 0
                    cant_roll_2 = 0
                    cant_roll_3 = 0
                    cant_roll_4 = 0
                    descuentofinal = 0
                    respuesta = 0
                    boleta = 0
                    menu = 0
                    menu2 = 0
                    menu3 = 0
                elif salidafinal == 2:
                    print("!Gracias por su compra, vuelva pronto¡")
                else:
                    print("")
                    
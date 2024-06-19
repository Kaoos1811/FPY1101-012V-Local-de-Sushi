import os
cant_camiones = 0
cap_camion = 530
saco_adicional = 0
costo_saco_adicional = 28750
camion_completo = 14310000
saco_comida = 0
flete = 250000
CatLove = 0
DogPremium = 0
CatElitePlus = 0
L_P = "cls"
menu1 = 0
menu2 = 0
valorfinal = 0
boleta = 0
while menu1 == 0:
    os.system = (L_P)
    try:
        nom_cliente = input("Ingrese Nombre: ")
        if len(nom_cliente)>=3:
            try:
                Numero_Contacto = int(input("Ingrese su numero de contancto: "))
                if len(str(Numero_Contacto)) >=8 and len(str(Numero_Contacto)) <=9:
                    print("BIENVENIDO A LA DISTRIBUIDORA  DE COMIDA DE MASCOTAS 'LOS POLLOS'\n")
                menu2 = 1
            except ValueError:
                print("Ingrese numero de contacto valido...")
    except ValueError:
        print("Ingrese nombre valido...")
        while menu2 == 1:
            print("1) Camion completo")
            print("El costo de un camion que abarca 530 sacos de comida es de $14.310.000\n")
            print("2) Compra carga especifica")
            print("Cada adicional tiene un costo de 28750 y el valor del flete es de 250000 independiente si no va la carga completa en el camion\n")
            print("3) Imprimir boleta\n")
            print("4) Hacer otro pedido o salir")
            try: 
                respuesta = int(input("Ingrese una opcion"))
                if respuesta == 1:
                    cant_camiones = int(input(cant_camiones))
                    if cant_camiones > 0:
                        saco_comida = (530*cant_camiones)
                        print("Has ingresado", cant_camiones, "camiones")
                        print("+"*34)
                        menu2 = 1
                    else:
                        print("Ingrese una cantidad de camiones valida")
                        print("+"*34)
                elif respuesta == 2:
                    print("Tenemos disponibles los siguientes alimentos")
                    print("Cat Love")
                    print("Dog Premium")
                    print("Cat Elite Premium")
                    try:
                        tipo_comida = int(input("Ingresa la cantidad que deseas"))
                        if tipo_comida==1:
                            print("Has seleccionado la comida Cat Love")
                            c_c_catlove = int(input("Cuantas unidades desea"))
                            if c_c_catlove >= 1:
                                saco_comida +=(CatLove*c_c_catlove)
                                print("Ha agregado", c_c_catlove, "sacos de comida de Cat Love")
                                print("Su cantidad es", c_c_catlove)
                                print("+"*34)
                            else:
                                print("Ingrese un valor mayor a 0")
                                print("+"*34)
                        elif tipo_comida == 2:
                            print("Has seleccionado la comida Dog Premium")
                            c_c_DogPremium = int(input("Cuantas unidades desea"))
                            if c_c_DogPremium >= 1:
                                saco_comida +=(DogPremium*c_c_DogPremium)
                                print("Ha agregado", c_c_DogPremium, "sacos de comida Dog Premium")
                                print("Su cantidad es", c_c_DogPremium)
                                print("+"*-34)
                            else:
                                print("Ingrese un valor mayor a 0")
                                print("+"*34)
                        elif tipo_comida == 3:
                            print("Has seleccionado la comida Cat Elite Plus")
                            c_c_CatElitePlus = int(input("Cuantas unidades desea"))
                            if c_c_CatElitePlus >= 1:
                                saco_comida +=(CatElitePlus*c_c_CatElitePlus)
                                print("Ha agregado", c_c_CatElitePlus,"cantidad de Cat Elite Plus")
                                print("Su cantidad es", c_c_CatElitePlus)
                                print("+"*34)
                    except ValueError:
                        print()
            except ValueError:
                print()
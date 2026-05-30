# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
# hasta que seleccionamos la opción de “Salir”.

while True:
    print("Menú personal de mis cosas favoritas")
    print("   1. Series animadas")
    print("   2. Películas animadas")
    print("   3. Pistas de música favoritas")
    print("   4. Salir")
    opcion = int(input("Elija una opción (1-5): "))
    
    if opcion == 1:
        print("Series animadas:")
        print(" + The Midnight Gospel (Netflix 2020, Pendleton Ward & Duncan Trussell)")
        print(" + Gravity Falls (Disney Television Animation 2012, Alex Hirsch)")
        print(" + Invader Zim (Nickelodeon 2001, Jhonen Vasquez)")
    elif opcion == 2:
        print("Películas animadas:")
        print(" + Soul (Pixar 2020, Pete Docter)")
        print(" + The Wild Robot (DreamWorks Animation 2024, Chris Sanders)")
        print(" + The Land Before Time (Universal Pictures 1988, Don Bluth)")
    elif opcion == 3:
        print("Pistas de música favoritas:")
        print(" + Human Nature - Michael Jackson")
        print(" + No Es Personal - Underaiki")
        print(" + Something Comforting - Porter Robinson")
    elif opcion == 4:
        print("Gracias, vuelva prontos")
        break;
    else:
        print("Opción no válida")

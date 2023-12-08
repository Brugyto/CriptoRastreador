# crypto_tracker/principal.py

de  módulos . moneda  importacion  Moneda
de  módulos . cartera  importada  Cartera

def  iniciar_aplicacion ():
    print ( "¡Bienvenido a CryptoTracker!" )

    # Crear una cartera e iniciar con algunas criptomonedas
    mi_cartera  =  Cartera ()
    inicializar_cartera ( mi_cartera )

    # Mostrar el estado inicial de la cartera
    mostrar_estado_cartera ( mi_cartera )

    #Interacción del usuario
    mientras que  Verdadero :
        opcion  =  obtener_opcion_usuario ()

        si  opción  ==  1 :
            agregar_moneda ( mi_cartera )
         opción  elif ==  2 :
            mostrar_estado_cartera ( mi_cartera )
         opción  elif ==  3 :
            print ( "¡Gracias por usar CryptoTracker! Hasta luego." )
            romper
        demás :
            print ( "Opción no válida. Por favor, elige una opción válida." )

def  inicializar_cartera ( cartera ):
    # Iniciar la cartera con algunas criptomonedas
    bitcoin  =  Moneda ( "Bitcoin" , "BTC" , 45000 )
    ethereum  =  Moneda ( "Ethereum" , "ETH" , 3000 )

    cartera . agregar_moneda ( bitcoin )
    cartera . agregar_moneda ( ethereum )

def  mostrar_estado_cartera ( cartera ):
    print ( " \n Estado Actual de la Cartera: " )
    
    si  no  cartera . monedas :
        print ( "Tu cartera está vacía." )
    demás :
        para  moneda  en  cartera . monedas :
            imprimir ( moneda . obtener_información ())

        print ( " \n Valor Total de la Cartera: $" , cartera . valor_total ())

def  obtener_opcion_usuario ():
    imprimir ( " \n Opciones: " )
    print ( "1. Agregar Criptomoneda" )
    print ( "2. Mostrar Estado de la Cartera" )
    imprimir ( "3. Salir" )

    mientras que  Verdadero :
        intentar :
            opcion  =  int ( input ( "Elige una opción: " ))
             opción de devolución
        excepto  ValorError :
            print ( "Por favor, ingresa un número válido." )

def  agregar_moneda ( cartera ):
    nombre  =  input ( "Ingresa el nombre de la criptomoneda: " )
    símbolo  =  input ( "Ingresa el símbolo de la criptomoneda: " )

    mientras que  Verdadero :
        intentar :
            precio  =  float ( input ( "Ingresa el precio de la criptomoneda: $" ))
            romper
        excepto  ValorError :
            print ( "Por favor, ingresa un número válido para el precio." )

    nueva_moneda  =  Moneda ( nombre , símbolo , precio )
    cartera . agregar_moneda ( nueva_moneda )
    print ( f" { nombre } ha sido agregada a tu cartera." )

si  __nombre__  ==  "__principal__" :
    iniciar_aplicacion ()

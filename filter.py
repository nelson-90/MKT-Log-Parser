from functions import *


#Llama a la funcion que imprime el menu principal
opcion = Imprime_menu()
#Mientras el usuario no seleccione Salir en el menu, el programa continua
while (opcion != "0"):
     #Opcion 1, toma log.txt y lo filtra, luego vuelve a imprimir el menu
     if opcion == "1":
          Genera_Resultado("log.txt")
          opcion = Imprime_menu()
     #Opcion 2, toma log.txt y lo filtra, mapea y luego vuelve a imprimir el menu
     if opcion == "2":
          Map_Info_Log("log.txt")
          opcion = Imprime_menu()
     #Opcion 3, pide al usuario que ingrese un texto el cual sera buscado en log.txt y generara un .txt 
     #    con todas las lineas que tengan ese texto, si el valor ingresado da error el programa se cierra,
     #    si esta OK vuelve a imprimir el menu
     elif(opcion == "3"):
          texto = Elige_texto()
          #Si no existe el texto en log.txt, le avisa al usuario
          if (texto == "0"):
               print("No existen registros que contengan esa frase...\n")
               input("\n\n Presione una tecla para continuar...")
          else:
               Genera_Resultado(texto)
          opcion = Imprime_menu()
     #Opcion 4, pide al usuario que ingrese un texto el cual sera buscado en log.txt y generara un .txt 
     #    con todas las lineas que tengan ese texto, si el valor ingresado da error el programa se cierra,
     #    si esta OK vuelve a imprimir el menu
     elif(opcion == "4"):
          texto = Elige_texto()
          #Si no existe el texto en log.txt, le avisa al usuario
          if (texto == "0"):
               print("No existen registros que contengan esa frase...\n")
               input("\n\n Presione una tecla para continuar...")
          else:
               Map_Info_Log(texto)
          opcion = Imprime_menu()

     #Opcion 5, imprime menú de ayuda
     elif(opcion == "5"):
          Imprime_ayuda()
          opcion = Imprime_menu()
     #Cualquier otra opcion no contemplada, muestra nuevamente el menu
     else:
          print("Opcion no incluida en el menu...\n")
          opcion = Imprime_menu()


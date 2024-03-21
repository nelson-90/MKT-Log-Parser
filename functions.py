
import os

def Genera_Resultado(file):
#Abre el archivo que contiene los logs y lee los datos para procesarlos
    with open(file,"r") as log:
        file_content=log.read()
    dict_log: dict = {}
#Crea el archivo filtered_log.txt que guarda la info necesaria para luego darle el formato final
    with open("filtered_log.txt","w") as filtered_log:
        #Separa cada linea tomando el enter como delimitador
        file_lines=file_content.split("\n")
        #Carga un titulo al archivo filtered_log.txt
        filtered_log.write(f"FECHA;SRC-IP;DST-IP;DST-PORT;PROTOCOL\n")
        for line in file_lines:
            #Si la linea no esta vacia
            if (line!=""):
                #Separa cada linea utilizando el delimitador ","
                line=line.split(",")
                #Obtiene la Fecha con formato mmm dd
                aux_date=line[0].split(" ")
                if (aux_date[1] == ""):
                    date=aux_date[0]+" "+aux_date[2]
                else:
                    date=aux_date[0]+" "+aux_date[1]
                #Busca si en la linea existe la cadena "src-mac"
                if(line[2].find("src-mac")>=0):
#Busca si en la linea existe la cadena "ICMP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt 
                    if(line[3].find("ICMP")>=0):
                        src_ip=line[-2].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        dst_ip=line[-2].split("->")[1]
                        dst_port = "0"
                        protocol = "ICMP"
                        filtered_log.write(f"{date};{src_ip};{dst_ip};0;ICMP;\n")
#Busca si en la linea existe la cadena "TCP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                    elif(line[3].find("TCP")>=0):
                        src_ip=line[-2].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")                        
                        aux_dst=line[-2].split("->")[1].split(":")
                        dst_ip=aux_dst[0]
                        dst_port=aux_dst[1]
                        protocol = "TCP"
                        filtered_log.write(f"{date};{src_ip};{dst_ip};{dst_port};TCP\n")
#Busca si en la linea existe la cadena "UDP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                    elif(line[3].find("UDP")>=0):
                        src_ip=line[-2].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        aux_dst=line[-2].split("->")[1].split(":")
                        dst_ip=aux_dst[0]
                        dst_port=aux_dst[1]
                        protocol = "UDP"
                        filtered_log.write(f"{date};{src_ip};{dst_ip};{dst_port};UDP\n")
#Si no existe la cadena "src-mac"
                else:
#Busca si en la linea existe la cadena "ICMP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                    if(line[2].find("ICMP")>=0):
                        src_ip=line[-2].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        dst_ip=line[-2].split("->")[1]
                        dst_port = "0"
                        protocol = "ICMP"
                        filtered_log.write(f"{date};{src_ip};{dst_ip};0;ICMP;\n")
#Busca si en la linea existe la cadena "TCP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                    elif(line[2].find("TCP")>=0):
                        src_ip=line[-2].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        aux_dst=line[-2].split("->")[1].split(":")
                        dst_ip=aux_dst[0]
                        dst_port=aux_dst[1]
                        protocol = "TCP"
                        filtered_log.write(f"{date};{src_ip};{dst_ip};{dst_port};TCP\n")
#Busca si en la linea existe la cadena "UDP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                    elif(line[2].find("UDP")>=0):
                        src_ip=line[-2].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        aux_dst=line[-2].split("->")[1].split(":")
                        dst_ip=aux_dst[0]
                        dst_port=aux_dst[1]
                        protocol = "UDP"
                        filtered_log.write(f"{date};{src_ip};{dst_ip};{dst_port};UDP\n")

#Si la linea leida no estaba vacia, comienza la creación del diccionario que sumara todos los eventos repetidos
#Si la fecha no existe en el diccionario, la agrega
                if date not in dict_log:
                    dict_log[date] = {}
#Si la IP de origen no existe para la fecha que esta cargada en el diccionario, la agrega
                if src_ip not in dict_log[date]:
                    dict_log[date][src_ip] = {}
#Si la IP de destino no existe para el combo [fecha / IP origen] que estan cargados en el diccionario, la agrega
                if dst_ip not in dict_log[date][src_ip]:
                    dict_log[date][src_ip][dst_ip] = {}
#Si el protocolo no existe para el combo [fecha / IP origen / IP destino] que estan cargados en el diccionario, lo agrega
                if protocol not in dict_log[date][src_ip][dst_ip]:
                    dict_log[date][src_ip][dst_ip][protocol] = {}
#Si el puerto de destino existe para el combo [fecha / IP origen / IP destino / protocolo] que estan cargados en el diccionario, suma una iteración             
                if dst_port in dict_log[date][src_ip][dst_ip][protocol]:
                    dict_log[date][src_ip][dst_ip][protocol][dst_port] = dict_log[date][src_ip][dst_ip][protocol][dst_port] + 1
#Si el puerto de destino no existe para el combo [fecha / IP origen / IP destino / protocolo] que estan cargados en el diccionario, lo agrega y establece el contador en 1
                else:
                    dict_log[date][src_ip][dst_ip][protocol][dst_port] = 1

#Si se elige la opcion 1, crea resulta.txt
    if (file == "log.txt"):
        file = ".txt"

#Crea el archivo result<texto>.txt y guarda los datos filtrados
    with open("result"+file, "w") as f:
        #Carga el encabezado del archivo
        f.write("{:12s} | {:15s} | {:15s} | {:8s} | {:6s} | {:4s}\n".format("FECHA", "SRC_IP", "DST_IP", "PROTOCOL", "D_PORT", "CONT"))
        #Recorre el diccionario y guarda los registros en el archivo
        for d in dict_log:
            for s in dict_log[d]:
                for d_ip in dict_log[d][s]:
                    for d_prot in dict_log[d][s][d_ip]:
                        for d_port in dict_log[d][s][d_ip][d_prot]:
                            f.write("{:12s} | {:15s} | {:15s} | {:8s} | {:6s} | {:4d}\n".format(d, s, d_ip, d_prot, d_port, dict_log[d][s][d_ip][d_prot][d_port]))

    print(f"El archivo result{file} fue creado exitosamente...\n")
    input("\n\n Presione una tecla para continuar...")


def Elige_texto():
    texto = input("Ingrese el texto a filtrar: ")
    print("\n")
    #Abre log.txt y guarda el contenido en una variable
    with open("log.txt","r") as log:
        file_content=log.read()
    #Trata de crear un archivo con el texto ingresado por el usuario, si falla cierra el programa
    try:
        #Crea un archivo cuyo nombre es el texto que ingreso el usuario
        with open(texto + ".txt","w") as filtered_log:
            #Separa por lineas el contenido de log.txt
            file_lines=file_content.split("\n")
            #Evalua linea por linea hasta que no existan mas
            for line in file_lines:
                #Chequea si el texto ingresado se encuentra en esa linea, si es así lo graba en el archivo filtrado
                # si la linea esta vacia, no hace nada
                if (line!="") and (texto in line):
                    filtered_log.write(line)
                    filtered_log.write("\n")
        #Chequea que el archivo creado tenga datos
        if (os.stat(texto + ".txt").st_size == 0):
            #Si esta vacio, lo elimina y retorna 0
            os.remove(texto + ".txt")
            return "0"
        else:
            #Si contiene datos, retorna el nombre del archivo creado
            return texto + ".txt"
    except IOError:
        #Si el texto ingresado tiene un formato no permitido para crear archivos, cierra el programa
        print("El formato de la frase ingresada no es correcta...\n")
        print("Reinicie el programa...\n")
        quit()


def Imprime_ayuda():
    #Imprime la ayuda del programa
    print("""        OPCION 1-   Toma el archivo log.txt, lo filtra y genera result.txt.
        OPCION 2-   Toma el archivo log.txt, lo filtra, mapea los puertos y genera mapeo.txt.
        OPCION 3-   Deja elegir al usuario una passphrase (<texto>) y primero filtra las lineas de log.txt que contengan esa frase, 
                    el resultado se almacena en el archivo <texto>.txt, el cual luego de filtrado genera el archivo result<texto>.txt.
        OPCION 4-   Deja elegir al usuario una passphrase (<texto>) y primero filtra las lineas de log.txt que contengan esa frase, 
                    el resultado se almacena en el archivo <texto>.txt, el cual luego se mapean los puertos y genera el archivo mapeo<texto>.txt.
    """)
    input("\n\n Presione una tecla para continuar...")


def Imprime_menu():
    os.system('cls')
    print ("""

    ██╗░░░░░░█████╗░░██████╗░  ███╗░░░███╗██╗██╗░░██╗██████╗░░█████╗░████████╗██╗██╗░░██╗
    ██║░░░░░██╔══██╗██╔════╝░  ████╗░████║██║██║░██╔╝██╔══██╗██╔══██╗╚══██╔══╝██║██║░██╔╝
    ██║░░░░░██║░░██║██║░░██╗░  ██╔████╔██║██║█████═╝░██████╔╝██║░░██║░░░██║░░░██║█████═╝░
    ██║░░░░░██║░░██║██║░░╚██╗  ██║╚██╔╝██║██║██╔═██╗░██╔══██╗██║░░██║░░░██║░░░██║██╔═██╗░
    ███████╗╚█████╔╝╚██████╔╝  ██║░╚═╝░██║██║██║░╚██╗██║░░██║╚█████╔╝░░░██║░░░██║██║░╚██╗
    ╚══════╝░╚════╝░░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝╚═╝░░╚═╝
    """)


     #Imprime el menu de opciones y devuelve esa opcion al llamado
    print ("""OPCIONES DEL SITEMA:
               1- Default sin mapeo de puertos
               2- Default con mapeo de puertos
               3- Custom sin mapeo de puertos
               4- Custom con mapeo de puertos
               5- Ayuda
               0- Salir             
          """)
    opcion=input("Ingrese la opcion que desee: ")
    print ("\n")
    return opcion

#Función que crea un archivo mapeo.txt donde se arma un resumen de las conexiones
def Map_Info_Log(file):
    with open(file,"r") as log:
        file_content=log.read()
    dict_log: dict = {}
#Crea el archivo filtered_log.txt que guarda la info necesaria para luego darle el formato final
    with open("filtered_log.txt","w") as filtered_log:
        #Separa cada linea tomando el enter como delimitador
        file_lines=file_content.split("\n")
        #Carga un titulo al archivo filtered_log.txt
        filtered_log.write(f"SRC-IP;DST-IP;DST-PORT;PROTOCOL\n")
        for line in file_lines:
            #Si la linea no esta vacia
            if (line!=""):
                #Separa cada linea utilizando el delimitador ","
                line=line.split(",")
                #Busca si en la linea existe la cadena "src-mac"
                if(line[2].find("src-mac")>=0):
                    if(line[-2].find("prio")>=0):
                        index=-3
                    else:
                        index=-2 
#Busca si en la linea existe la cadena "ICMP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt 
                    if(line[3].find("ICMP")>=0):                
                        src_ip=line[index].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        dst_ip=line[index].split("->")[1]
                        dst_port = "0"
                        protocol = "ICMP"
                        filtered_log.write(f"{src_ip};{dst_ip};0;ICMP;\n")
#Busca si en la linea existe la cadena "TCP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                    elif(line[3].find("TCP")>=0):
                        src_ip=line[index].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        aux_dst=line[index].split("->")[1].split(":")
                        dst_ip=aux_dst[0]
                        dst_port=aux_dst[1]
                        protocol = "TCP"
                        filtered_log.write(f"{src_ip};{dst_ip};{dst_port};TCP\n")
#Busca si en la linea existe la cadena "UDP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                    elif(line[3].find("UDP")>=0):
                        src_ip=line[index].split("->")[0].split(":")[0]
                        src_ip=src_ip.replace(" ","")
                        aux_dst=line[index].split("->")[1].split(":")
                        dst_ip=aux_dst[0]
                        dst_port=aux_dst[1]
                        protocol = "UDP"
                        filtered_log.write(f"{src_ip};{dst_ip};{dst_port};UDP\n")
#Si no existe la cadena "src-mac"
                else:
                    if(line[-2].find("prio")>=0):
                        index=-3
                    else:
                        index=-2 
#Busca si en la linea existe la cadena "ICMP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                        if(line[2].find("ICMP")>=0):
                            src_ip=line[index].split("->")[0].split(":")[0]
                            src_ip=src_ip.replace(" ","")
                            dst_ip=line[index].split("->")[1]
                            dst_port = "0"
                            protocol = "ICMP"
                            filtered_log.write(f"{src_ip};{dst_ip};0;ICMP;\n")
#Busca si en la linea existe la cadena "TCP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                        elif(line[2].find("TCP")>=0):
                            src_ip=line[index].split("->")[0].split(":")[0]
                            src_ip=src_ip.replace(" ","")
                            aux_dst=line[index].split("->")[1].split(":")
                            dst_ip=aux_dst[0]
                            dst_port=aux_dst[1]
                            protocol = "TCP"
                            filtered_log.write(f"{src_ip};{dst_ip};{dst_port};TCP\n")
#Busca si en la linea existe la cadena "UDP" y obtiene src_ip, dst_ip, protocol y dst_port para luego guardar el registro en filtered_log.txt
                        elif(line[2].find("UDP")>=0):
                            src_ip=line[index].split("->")[0].split(":")[0]
                            src_ip=src_ip.replace(" ","")
                            aux_dst=line[index].split("->")[1].split(":")
                            dst_ip=aux_dst[0]
                            dst_port=aux_dst[1]
                            protocol = "UDP"
                            filtered_log.write(f"{src_ip};{dst_ip};{dst_port};UDP\n")

#Si la linea leida no estaba vacia, comienza la creación del diccionario que sumara todos los eventos repetidos               
#Si la IP de origen no existe en el diccionario, la agrega
                if src_ip not in dict_log:
                    dict_log[src_ip] = {}
#Si la IP de destino no existe para la IP origen que esta cargada en el diccionario, la agrega
                if dst_ip not in dict_log[src_ip]:
                    dict_log[src_ip][dst_ip] = {}
#Si el protocolo no existe para el combo [IP origen / IP destino] que estan cargados en el diccionario, lo agrega, asi como también el puerto de destino
                if protocol not in dict_log[src_ip][dst_ip]:
                    dst_port = dst_port.replace(")","")
                    #Si hay puertos dinamicos mayores a 40000, los agrupa
                    if (int(dst_port) > 40000):
                       dst_port = "40000 / 65535"
                    dict_log[src_ip][dst_ip][protocol] = dst_port
                else:
#Si el protocolo existe para el combo [IP origen / IP destino] que estan cargados en el diccionario, lo agrega
                    valor = dict_log[src_ip][dst_ip][protocol]
                    dst_port = dst_port.replace(")","")
                    #Si hay puertos dinamicos mayores a 40000, los agrupa
                    if (int(dst_port) > 40000):
                       dst_port = "40000 / 65535"
                    #Anexa el nuevo puerto destino al conjunto de valores repetidos
                    if dst_port not in valor:
                        dict_log[src_ip][dst_ip][protocol]= valor + " / " + dst_port
                        
#Si se elige la opcion 1, crea resulta.txt
    if (file == "log.txt"):
        file = ".txt"
#Crea el archivo mapeo<texto>.txt y guarda los datos filtrados
    with open("mapeo"+file, "w") as f:
        #Carga el encabezado del archivo
        f.write("{:15s} | {:15s} | {:8s} | {:255s}\n".format("SRC_IP", "DST_IP", "PROTOCOL", "D_PORT"))
        #Recorre el diccionario y guarda los registros en el archivo
        for s in dict_log:
            for d_ip in dict_log[s]:
                for d_prot in dict_log[s][d_ip]:
                    #Si la linea tiene más de 1 puerto
                    if "/" in dict_log[s][d_ip][d_prot]:
                        #Separa los puertos tomando la "/" como delimitador
                        puerto_str = str(dict_log[s][d_ip][d_prot]).split(" / ")
                        #Pasa los puertos de string a numeros enteros
                        puerto_int = list(map(lambda temp: int(temp), puerto_str))
                        #Ordena los puertos de menor a mayor
                        puerto_int.sort()
                        #Pasa los puertos de numeros enteros a string
                        dst_port = str(puerto_int[0])
                        #Le agrega el separador "/" a los puertos
                        for puerto in puerto_int[1:]:
                            dst_port += " / " + str(puerto)
                        #Graba los puertos ordenados en el diccionario
                        dict_log[s][d_ip][d_prot] = dst_port    
                        #Graba la linea en el archivo mapeo<texto>.txt
                        f.write("{:15s} | {:15s} | {:8s} | {:255s} \n".format(s, d_ip, d_prot, dict_log[s][d_ip][d_prot]))
                    else:
                        #Si la linea tiene un solo puerto, la agrega al archivo
                        f.write("{:15s} | {:15s} | {:8s} | {:255s} \n".format(s, d_ip, d_prot, dict_log[s][d_ip][d_prot]))

    print(f"El archivo mapeo{file} fue creado exitosamente...\n")
    input("\n\n Presione una tecla para continuar...")
        











 
        
     
        
        
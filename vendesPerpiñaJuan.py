'''Juan Perpiña Piles'''
noms=[]
preus=[]
''' Esta inicializado en 0 para mostrar en los productos que
no tienen ventas un 0 y tiene 10 espacios para que al introducir
los datos de los productos vendidos se coloquen donde les corresponde.'''
qventes=[]
opciovalida=True

while opciovalida:

    '''Menú de opciones'''
    print("MENÚ DE OPCIONES")
    print("1. Introducir un artículo")
    print("2. Hacer una venta")
    print("3. Mostrar información")
    print("4. Borrar un artículo")
    print("5. Borrar todos los artículos")
    print("6. salir")

    opcio = int(input("¿Que vas a hacer? "))
    if (opcio<=0)or (opcio>7):
        print("El número indicado no es correcto")
        print("Si quieres salir, pulsa el número 6.")

    if opcio==1:
        noms.append(input("Dime el nombre del artículo: "))
        preus.append(float(input("¿Que precio tiene este artículo? ")))       
        qventes.append(0)
    elif opcio==2:
        venta=input("¿Que artículo vas vender? ")
           
        'Mirar si existen articulos'
        siarticle=False
        for i in range (len(noms)):
            if venta==noms[i]:
                qventes[i]+=(int(input("¿Cuantos has vendido? ")))
                siarticle=True
        if siarticle==False:  
            print("El artículo no exite o no esta escrito correctamente.")
                    
    elif opcio==3:
        ''' Informar al usuario que no tiene ningún artículo y lo devuelve al menú'''
        if noms==[]:
            print("No has introducido ningún artículo")

        else:
            sumatotal=0
            print(noms)
            print(preus)
            print(qventes)
            nommaximport=noms[0]
            maxventa=qventes[0]
            nommaxventa=noms[0]
            maximport=qventes[0]*preus[0]
             
            print("NOM".center(25,' '),"PREU".center(6,' '),"QUANT".center(10,' '),"IMPORT".center(7,' '))
            print("".center(25,'-'),"".center(6,'-'),"".center(10,'-'),"".center(7,'-'))
            for i in range (len(noms)):
                if qventes[i]<=0:
                    importe=0
                    maximport=0      
                else:
                    importe=(qventes[i]*preus[i]) 

                print((noms[i].ljust(25)[:25]+""),"%4.2f"%(preus[i]),"%10d"%(qventes[i]),"%7.2f"%(importe))
                sumatotal+=(importe)

                if maximport<(qventes[i]*preus[i]):
                    maximport=(qventes[i]*preus[i])
                    nommaximport=noms[i]

                if maxventa<qventes[i]:
                    maxventa=qventes[i]
                    nommaxventa=noms[i]

            print("".center(51,"-"), )
            print("".center(31," "),"TOTAL: ".center(9," "),"%7.2f"%(sumatotal))
                    
            print("El artículo más vendido es: ", nommaxventa," con ",maxventa, " unidades vendidas")
            
            print("El artículo con mas ingresos es: ",nommaximport," con un total de: ",maximport," euros.")

    
    elif opcio==4:
        borrar=False
        borrarcompletada=False
        print(noms)
        article=input("¿Que artículo quieres borrar? ")

        'Mirar si existe el articulo'
        for i in range (len(noms)):
            if article==noms[i]:
                posicion=i
                borrar=True
            'Borrar el artículo de todas las listas'
            if borrar==True:
                del noms[posicion]
                del preus[posicion]
                del qventes[posicion]
                borrarcompletada=True
                if borrarcompletada==True:
                    print("Artículo borrado con éxito.")
                    break
        if borrar==False:
            print("El artículo no existe o no se ha escrito correctamente.")

    elif opcio==5:
        'Borrar todos los articulos (los 3 vectores)'
        resposta=input("¿Quieres borrar todos los artículos? (si/no)")

        if resposta=="Si" or resposta=="si" or resposta=="S"or resposta=="s":
            noms.clear()
            preus.clear()
            qventes.clear()
            print("Se han borrado todos los artículos.")
        else:
            print("Por favor, vuelva a seleccionar lo que quiere hacer.")

    elif opcio==6:
        salir=input("¿Seguro que quieres salir? (s/n) ")
        if salir=="Si" or salir=="si" or salir=="S"or salir=="s":
            opciovalida=False
Codigo = []
Nombre = []
Pedido = []
Telefono = []

menuprincipal = int(input("MENU PRINCIPAL : \n 1. Ver Pedidos Pendientes \n 2. Ingresar Nuevo Pedido \n 3. Entregar Pedido \n 4. Modificar Pedido \n 5. Ver Postres disponibles \n 0. Salir \n"))
while menuprincipal != 0:
    
    if menuprincipal == 1:
        print("Pedidos Pendientes")
        print("Codigo       |   Nombre                   |Pedido             |Telefono")
        for x in range(len(Codigo)):
            print(Codigo[x],"         ",Nombre[x],"                     ",Pedido[x],"           ",Telefono[x])
        
        
    elif menuprincipal == 2:
        print("Ingresar Nuevo Pedido")
        print("llena los siguientes datos: ")
        Codigo.append(input("Codigo del pedido: \n"))
        Nombre.append(input("Nombre de la persona: \n"))
        Pedido.append(input("Pedido: \n"))
        Telefono.append(int(input("Telefono de la persona: \n")))      
        
    elif menuprincipal == 3:
        print("Entregar Pedido")
        cod = input("Escribe el codigo del pedido a Entregar \n")
        for i in range(len(Codigo)-1,-1,-1):
            if Codigo[i] == cod:
                Codigo.pop(i)
                Nombre.pop(i)
                Telefono.pop(i)
                Pedido.pop(i)
        print("Pedido entregado")     
           
        
    elif menuprincipal == 4:
        print("Modificar Pedido")
        cod  = input("Ingrese el codigo del pedido a modificar: \n")
        
        for x in range(len(Codigo)):
            if Codigo[x] == cod:
                Nombre[x] = input("¿Cual es el nuevo nombre?\n")
                Pedido[x] = input("¿Cual es el nuevo pedido?\n")
                Telefono[x] = input("¿Cual es el nuevo telefono?\n")
        print("Modificando pedido")
    elif menuprincipal ==5:
        print("Postres Disponibles y tiempo de elaboración")
        print("6 Galletass con cobertura --- 1h \nRosca Danesa --- 2h \nPastel de Frutas --- 2.5h \nGalletas de jengibre ---30 min \nCupcakes Navideños --- 1.5h")
        
    else:
        print("Digite una opción correcta, por favor")
    
    menuprincipal = int(input("MENU PRINCIPAL : \n 1. Ver Pedidos Pendientes \n 2. Ingresar Nuevo Pedido \n 3. Entregar Pedido \n 4. Modificar Pedido \n 5. Ver Postres disponibles\n 0. Salir \n"))  
        
CodigoT = open('Codigo.txt','w')
NombreT = open('Nombre.txt','w')
PedidoT = open('Pedido.txt','w')
TelefonoT = open('Telefono.txt','w')

for x in range(len(Codigo)):
    CodigoT.write(Codigo[x]+',')
    NombreT.write(Nombre[x]+',')
    PedidoT.write(Pedido[x]+',')
    TelefonoT.write(str(Telefono[x])+',')
    
CodigoT.close()
NombreT.close()
PedidoT.close()
TelefonoT.close()

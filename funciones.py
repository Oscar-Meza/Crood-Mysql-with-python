#complementos del archivo master

def listar(clientes):
    print("\nClientes: ")
    contador = 0
    for cli in clientes:
        contador = contador + 1
        print(f"{contador} .- Codigo: {cli[0]} Nombre: {cli[1]} {cli[2]} {cli[3]} y Creditos: {cli[4]}")
    print("##################\n")

def DatosClientes():
    codigo = int(input("Dame el codigo: "))
    nombre = input("Dame tu nombre: ")
    ap = input("Dame tu apellido paterno: ")
    am = input("Dame tu apellido materno: ")
    creditos = int(input("Dame los creditos: "))
    
    clientes = (codigo, nombre,ap, am, creditos)
    return clientes

def DatosClientesActualizar(clientes):
    listar(clientes) #ver todos los clientes
    existe = False
    codigoActualizar = int(input("Dame el codigo a Actualizar: "))
    for cli in clientes:
        print(cli[0])
        if cli[0] == codigoActualizar:
            print(f"Dato encontrado {codigoActualizar}")
            existe = True
            break
    if existe == True:
        nombre = input("Dame tu nombre: ")
        ap = input("Dame tu apellido paterno: ")
        am = input("Dame tu apellido materno: ")
        creditos = int(input("Dame los creditos: "))
        clientes = (nombre,ap,am,creditos,codigoActualizar)
    else:
        clientes = None
        
    return clientes

def registroEliminar(clientes):
    listar(clientes)
    #print(f"Datos de clientes: {clientes}")
    existe = False
    codigoEliminar = int(input("Dame el codigo a Eliminar: "))
    for cli in clientes:
        print(cli[0])
        if cli[0] == codigoEliminar:
            print(f"Dato encontrado a eliminar {codigoEliminar}")
            existe = True
            break
    
    if not existe:
        codigoEliminar = ""
        
    return codigoEliminar
        
    
    
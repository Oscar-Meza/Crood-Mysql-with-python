#Funciones para el menu 
from conexion import DAO
import conexion 
import funciones

def MenuPrincipal():
    conectar = DAO()
    bandera = True
    while bandera == True:
        print("#### MENU PRINCIPAL ####")
        print("1.- Listar Clientes")
        print("2.- Registrar Clientes")
        print("3.- Actualizar Clientes")
        print("4.- Borrar Clientes")
        print("5.- Salir")
        opc = int(input("Seleciona una opcion: "))
        if opc > 0 and opc < 6:
            if opc == 1:
                try:
                    clientes = conectar.ListarClientesP()
                    if len(clientes) > 0:
                        funciones.listar(clientes)
                    else:
                        print("No hay registro")
                except:
                    print("No se pudo ejecutar la consulta")
                    
            elif opc == 2:
                datos_curso = funciones.DatosClientes()
                print(f"EStos son los datos a insertar: {datos_curso}")
                try:
                    conectar.registrarClientes(datos_curso)
                except:
                    print("No se pudo Agregar Datos")                    
                pass
            
            elif opc == 3:
                try:
                    clientes = conectar.ListarClientesP()
                    if len(clientes) > 0:
                        codigocliente = funciones.DatosClientesActualizar(clientes)
                        print(f"Campo codigoCliente {codigocliente}")
                        if codigocliente:
                            conectar.actualizarCliente(codigocliente)
                        else:
                            print("codigo no encontrado para actualizar .....\n")
                    else:
                        print("No hay clientes")
                except:
                    print("Error Except Master")
                pass
            
            elif opc == 4:
                try:
                    clientes = conectar.ListarClientesP()
                    if len(clientes) > 0:
                        dato_eliminar = funciones.registroEliminar(clientes)
                        print(f"Dato a eliminar {dato_eliminar}")
                        if not (dato_eliminar == ""):
                            conectar.EliminarCurso (dato_eliminar)
                            
                        else:
                            print("codigo del curso no encontrado o vacio .....\n")
                    else:
                        print("No hay Registros para eliminar")
                except:
                    print("Eliminar Error Except Master")
                
                
                pass
            
            elif opc == 5:
                print("Hasta luego")
                bandera = False
                
        else:
            print("opcion no valida selecciona una del 1 al 5")
            
MenuPrincipal()           
            
            
      
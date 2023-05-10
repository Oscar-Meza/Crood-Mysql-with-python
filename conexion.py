#Todo lo que tenga que ver con base de datos MySQL
#conexiones, consultas.

#pip install-mysql-connector-python

import mysql.connector
from mysql.connector import Error

#conectando con mysql
class DAO():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                port = 3306,
                user = "oscar",
                password = "220701",
                db = "crud_poo"
            )
            print("Conectado con exito")
        except Error as ex:
            print(f"No se pudo conectar a la base de datos  :( Error {ex}")
            
    def ListarClientesP(self):
        if self.conexion.is_connected(): #estas conectado
            try:
                cliente = self.conexion.cursor() #cursor palabra clave
                cliente.execute("SELECT * FROM clientes ORDER BY codigo ASC")
                resultados = cliente.fetchall() #guardar en un  array lista, tupla, directorio ["codigo", "nombre" "etc"]
                return resultados
            except Error as ex:
                print(f"No se pudo Lista clientes Except {ex}")
                
    def registrarClientes(self,curso):
        #print(f"Datos Recibidos {curso}")
        if self.conexion.is_connected():
            try:
                cliente = self.conexion.cursor()
                #print(cliente)
                sql = "INSERT INTO clientes (codigo, nombre, ap, am, creditos) VALUES (%s,%s,%s,%s,%s)"
                #curso = (05, "Juan", "Perez", "Solano", 34)
                #clientes = (codigo, nombre,ap, am, creditos)
                cliente.execute(sql,curso)
                self.conexion.commit() #Ejecuta el codigo
                print("Registro guardado correctamente")
            except Error as ex:
                print(f"No se pudo registrar Except {ex}")
                
                
    def actualizarCliente(self,clientes):
        if self.conexion.is_connected():
            try:
                cliente = self.conexion.cursor()
                #print(clientes)
                sql = "UPDATE clientes SET nombre = %s, ap = %s , am = %s , creditos = %s WHERE codigo = %s "
                cliente.execute(sql,clientes)
                self.conexion.commit()
                print("Registro Actualizado correctamente")
                
            except Error as ex:
                print(f"No se pudo actualizar Except conexion {ex}")
                
                
    def EliminarCurso(self,curso_eliminar):
        #print(f"Datos Recibidos {curso}")
        if self.conexion.is_connected():
            try:
                cliente = self.conexion.cursor()
                print(f"Llego a conexion {curso_eliminar}")
                sql = f"DELETE FROM clientes WHERE codigo = {curso_eliminar}"
                cliente.execute(sql)
                self.conexion.commit()
                print("Registro Eliminado correctamente")
            except Error as ex:
                print(f"No se pudo eliminar Except conexion {ex}")


            
            

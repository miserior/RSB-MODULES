import os
from dotenv import load_dotenv
import pyodbc

load_dotenv() 

direccion_servidor = os.getenv('direccion_servidor')
nombre_bd = os.getenv('nombre_bd')
nombre_usuario = os.getenv('nombre_usuario')
password = os.getenv('password')

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print("\n"*2)
    print("conexión exitosa")
    
except Exception as e:
    print("Ocurrió un error al conectar a SQL Server: ", e)
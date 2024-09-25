import pyodbc

def conectar_sql_server(direccion_servidor, nombre_bd, nombre_usuario, password):
    """
    Función para establecer una conexión a una base de datos SQL Server.

    Args:
        direccion_servidor (str): Dirección del servidor SQL Server (e.g., 'CC102-16\SA').
        nombre_bd (str): Nombre de la base de datos a la que se conectará.
        nombre_usuario (str): Nombre de usuario para la autenticación.
        password (str): Contraseña para la autenticación.

    Returns:
        pyodbc.Connection: Objeto de conexión si la conexión es exitosa, None en caso contrario.
    """
    try:
        conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + 
                                  direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
        return conexion
    except Exception as e:
        return("Ocurrió un error al conectar a SQL Server: ", e)

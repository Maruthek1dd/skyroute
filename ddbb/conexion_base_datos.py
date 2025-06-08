import mysql.connector 
from mysql.connector import Error
from ddbb.config import DB_CONFIG

def crear_conexion():
    """Establece conexión a la base de datos."""
    try:
        conexion = mysql.connector.connect(**DB_CONFIG)
        if conexion.is_connected():
            return conexion
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

def cerrar_conexion(conexion):
    """Cierra la conexión si está activa."""
    if conexion and conexion.is_connected():
        conexion.close()

def ejecutar_consulta(query, parametros=None):
    """Ejecuta una consulta INSERT/UPDATE/DELETE."""
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        cursor.execute(query, parametros)
        conexion.commit()
        return True
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        cerrar_conexion(conexion)

def ejecutar_select(query, parametros=None):
    """Ejecuta una consulta SELECT y devuelve los resultados."""
    conexion = crear_conexion()
    if not conexion:
        return []
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(query, parametros)
        resultados = cursor.fetchall()
        return resultados
    except Error as e:
        print(f"Error en la consulta SELECT: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        cerrar_conexion(conexion)

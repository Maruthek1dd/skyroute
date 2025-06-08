import re
from conexion_base_datos import ejecutar_consulta

def es_email_valido(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def cliente_existe(id_cliente):
    query = "SELECT id FROM clientes WHERE id = %s"
    resultado = ejecutar_consulta(query, (id_cliente,), fetch=True)
    return bool(resultado)

def agregar_cliente():
    razon_social = input("Razón Social: ").strip()
    cuit = input("CUIT: ").strip()
    email = input("Correo electrónico: ").strip()

    if not es_email_valido(email):
        print("Correo electrónico no válido.")
        return

    query = "INSERT INTO clientes (razon_social, cuit, email) VALUES (%s, %s, %s)"
    try:
        ejecutar_consulta(query, (razon_social, cuit, email))
        print("Cliente agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar cliente: {e}")

def listar_clientes():
    query = "SELECT * FROM clientes"
    try:
        clientes = ejecutar_consulta(query, fetch=True)
        print("\nLista de clientes:")
        print("ID | Razón Social | CUIT | Email")
        print("--------------------------------------")
        for c in clientes:
            print(f"{c['id']} | {c['razon_social']} | {c['cuit']} | {c['email']}")
    except Exception as e:
        print(f"Error al listar clientes: {e}")

def modificar_cliente():
    listar_clientes()
    id_cliente = input("ID del cliente a modificar: ").strip()

    if not cliente_existe(id_cliente):
        print("Cliente no encontrado.")
        return

    nuevo_email = input("Nuevo correo electrónico: ").strip()
    if not es_email_valido(nuevo_email):
        print("Correo electrónico no válido.")
        return

    query = "UPDATE clientes SET email = %s WHERE id = %s"
    try:
        ejecutar_consulta(query, (nuevo_email, id_cliente))
        print("Cliente actualizado.")
    except Exception as e:
        print(f"Error al modificar cliente: {e}")

def eliminar_cliente():
    listar_clientes()
    id_cliente = input("ID del cliente a eliminar: ").strip()

    if not cliente_existe(id_cliente):
        print("Cliente no encontrado.")
        return

    confirmacion = input(f"¿Estás seguro que deseas eliminar el cliente {id_cliente}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("Eliminación cancelada.")
        return

    query = "DELETE FROM clientes WHERE id = %s"
    try:
        ejecutar_consulta(query, (id_cliente,))
        print("Cliente eliminado.")
    except Exception as e:
        print(f"Error al eliminar cliente: {e}")

from ddbb.conexion_base_datos import ejecutar_consulta, ejecutar_select

def destino_existe(id_destino):
    query = "SELECT id_destino FROM destinos WHERE id_destino = %s"
    resultado = ejecutar_select(query, (id_destino,))
    return bool(resultado)

def agregar_destino():
    ciudad = input("Ciudad: ").strip()
    pais = input("País: ").strip()

    if not ciudad or not pais:
        print("Ciudad y País no pueden estar vacíos.")
        return

    try:
        costo_base = float(input("Costo base: "))
    except ValueError:
        print("Costo inválido. Debe ser un número.")
        return

    query = "INSERT INTO destinos (ciudad, pais, costo_base) VALUES (%s, %s, %s)"
    try:
        ejecutar_consulta(query, (ciudad, pais, costo_base))
        print("Destino agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar destino: {e}")

def listar_destinos():
    query = "SELECT * FROM destinos"
    destinos = ejecutar_select(query)

    if not destinos:
        print("No hay destinos disponibles.")
        return

    print(f"{'ID':<10} {'Ciudad':<20} {'País':<20} {'Costo Base':<10}")
    for d in destinos:
        print(f"{d['id_destino']:<10} {d['ciudad']:<20} {d['pais']:<20} ${d['costo_base']:<10.2f}")

def modificar_destino():
    listar_destinos()
    try:
        id_destino = int(input("ID del destino a modificar: "))
    except ValueError:
        print("ID inválido.")
        return

    if not destino_existe(id_destino):
        print("Destino no encontrado.")
        return

    try:
        nuevo_costo = float(input("Nuevo costo base: "))
    except ValueError:
        print("Costo inválido. Debe ser un número.")
        return

    query = "UPDATE destinos SET costo_base = %s WHERE id_destino = %s"
    try:
        ejecutar_consulta(query, (nuevo_costo, id_destino))
        print("Destino actualizado.")
    except Exception as e:
        print(f"Error al actualizar destino: {e}")

def eliminar_destino():
    listar_destinos()
    try:
        id_destino = int(input("ID del destino a eliminar: "))
    except ValueError:
        print("ID inválido.")
        return

    if not destino_existe(id_destino):
        print("Destino no encontrado.")
        return

    confirmacion = input(f"¿Está seguro que desea eliminar el destino con ID {id_destino}? (s/n): ").strip().lower()
    if confirmacion != 's':
        print("Eliminación cancelada.")
        return

    query = "DELETE FROM destinos WHERE id_destino = %s"
    try:
        ejecutar_consulta(query, (id_destino,))
        print("Destino eliminado.")
    except Exception as e:
        print(f"Error al eliminar destino: {e}")

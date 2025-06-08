from ddbb.conexion_base_datos import ejecutar_consulta, ejecutar_select
from datetime import datetime, timedelta

def registrar_venta():
    try:
        cliente_id = int(input("ID del cliente: "))
        destino_id = int(input("ID del destino: "))
        costo = float(input("Costo total: "))
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar números válidos.")
        return

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = """INSERT INTO ventas (id_cliente, id_destino, fecha, costo, estado)
               VALUES (%s, %s, %s, %s, 'Activa')"""
    try:
        ejecutar_consulta(query, (cliente_id, destino_id, fecha, costo))
        print("Venta registrada correctamente.")
    except Exception as e:
        print(f"Error al registrar venta: {e}")

def listar_ventas():
    query = "SELECT * FROM ventas"
    try:
        ventas = ejecutar_select(query)
        if not ventas:
            print("No hay ventas registradas.")
            return

        print(f"{'ID':<5} {'Cliente':<10} {'Destino':<10} {'Estado':<10} {'Fecha':<20} {'Costo':<10}")
        for v in ventas:
            fecha_str = v['fecha'].strftime("%Y-%m-%d %H:%M:%S") if isinstance(v['fecha'], datetime) else v['fecha']
            print(f"{v['id_venta']:<5} {v['id_cliente']:<10} {v['id_destino']:<10} {v['estado']:<10} {fecha_str:<20} ${v['costo']:<10.2f}")
    except Exception as e:
        print(f"Error al listar ventas: {e}")

def anular_venta():
    listar_ventas()
    try:
        id_venta = int(input("ID de la venta a anular: "))
    except ValueError:
        print("ID inválido.")
        return

    query = "SELECT fecha FROM ventas WHERE id_venta = %s AND estado = 'Activa'"
    try:
        venta = ejecutar_select(query, (id_venta,))
        if not venta:
            print("Venta no encontrada o ya anulada.")
            return

        fecha_venta = venta[0]['fecha']
        if isinstance(fecha_venta, str):
            fecha_venta = datetime.strptime(fecha_venta, "%Y-%m-%d %H:%M:%S")

        ahora = datetime.now()

        if ahora - fecha_venta <= timedelta(minutes=5):
            query = """UPDATE ventas 
                       SET estado = 'Anulada', fecha_anulacion = %s 
                       WHERE id_venta = %s"""
            ejecutar_consulta(query, (ahora.strftime("%Y-%m-%d %H:%M:%S"), id_venta))
            print("Venta anulada correctamente.")
        else:
            print("La venta no puede anularse. Han pasado más de 5 minutos.")
    except Exception as e:
        print(f"Error al anular venta: {e}")

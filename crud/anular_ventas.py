from datetime import datetime, timedelta
from ddbb.conexion_base_datos import ejecutar_select, ejecutar_consulta

def anular_venta(id_venta):
    query_select = "SELECT fecha, estado FROM ventas WHERE id_venta = %s"
    resultado = ejecutar_select(query_select, (id_venta,))
    
    if not resultado:
        print("❌ Venta no encontrada.")
        return

    venta = resultado[0]

    if venta["estado"] == "Anulada":
        print("⚠️ La venta ya está anulada.")
        return

    fecha_venta = venta["fecha"]
    ahora = datetime.now()
    
    if ahora - fecha_venta <= timedelta(minutes=5):
        query_update = """
            UPDATE ventas
            SET estado = 'Anulada', fecha_anulacion = %s
            WHERE id_venta = %s
        """
        exito = ejecutar_consulta(query_update, (ahora, id_venta))
        if exito:
            print("✅ Venta anulada correctamente.")
        else:
            print("❌ Error al anular la venta.")
    else:
        print("⏱️ No se puede anular: pasaron más de 5 minutos desde la venta.")

# Ejemplo de uso
# anular_venta_si_es_reciente(1)  # Reemplazar por ID de venta válido

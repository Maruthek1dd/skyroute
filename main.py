import os
import crud.gestion_cliente as gestion_clientes
import crud.gestion_ventas as gestion_ventas
import crud.gestion_destino as gestion_destino
from ddbb.conexion_base_datos import crear_conexion, cerrar_conexion, ejecutar_consulta, ejecutar_select
from dotenv import load_dotenv




def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_int(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("⚠️ Entrada inválida. Por favor ingrese un número.")


def pausar():
    input("\nPresione Enter para continuar...")



def gestionar_clientes():
    volver = False
    while not volver:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")
        subopcion = input("Seleccione una opción: ")

        if subopcion == "1":
            gestion_clientes.listar_clientes()
        elif subopcion == "2":
            gestion_clientes.agregar_cliente()
        elif subopcion == "3":
            gestion_clientes.modificar_cliente()
        elif subopcion == "4":
            gestion_clientes.eliminar_cliente()
        elif subopcion == "5":
            print("Volviendo al menú principal...")
            volver = True
        else:
            print("Opción inválida, intente de nuevo.")
        pausar()





def gestionar_destino():
    volver = False
    while not volver:
        print("\n-- GESTIONAR DESTINO --")
        print("1. Agregar Destino")
        print("2. Listar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menú Principal")
        subopcion = input("Seleccione una opción: ")

        if subopcion == "1":
            gestion_destino.agregar_destino()
            print("Destino agregado")
        elif subopcion == "2":
           print("DESTINOS: " )
           gestion_destino.listar_destinos()
        elif subopcion == "3":
            gestion_destino.modificar_destino()
        elif subopcion == "4":
            gestion_destino.modificar_destino()
        elif subopcion == "5":
            print("Volviendo al menú principal...")
            volver = True
        else:
            print("Opción inválida, intente de nuevo.")
        pausar()




def gestionar_ventas():
    volver = False
    while not volver:
        print("\n-- GESTIONAR VENTAS --")
        print("1. Registrar Ventas")
        print("2. Listar Ventas")
        print("3. Volver al Menú Principal")
        subopcion = input("Seleccione una opción: ")

        if subopcion == "1":
            gestion_ventas.registrar_venta()
            print("Venta Registrada")
        elif subopcion == "2":
           print("VENTAS: " )
           gestion_ventas.listar_ventas() 
        elif subopcion == "3":
            print("Volviendo al menú principal...")
            volver = True
        else:
            print("Opción inválida, intente de nuevo.")
        pausar()






def menu_principal():
    salir = False

    while not salir:
        limpiar_pantalla()
        print("📋  Menú Principal:")
        print("1. 👤  Gestionar Clientes")
        print("2. 🌍  Gestionar Destinos")
        print("3. 💰  Gestionar Ventas")
        print("4. ↩️  Botón de Arrepentimiento")
        print("5. ℹ️  Acerca del Sistema")
        print("6. ❌  Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_clientes()
            pausar()
        elif opcion == "2":
            gestionar_destino()
            pausar()
        elif opcion == "3":
            gestionar_ventas()
            pausar()
        elif opcion == "4":
            gestion_ventas.anular_venta()
        elif opcion == "5":
            print("SkyRoute v1.0 - Sistema de gestión de pasajes creado en Python.")
            print("\nPor:")
            print("- Marusich Leonardo")
            print("- Gonzalez Leonardo")
            print("- Trinidad Dario Exequiel")
            print("- Mazzei Juan Cruz")
            print("- Mancini Pereyra Marcelo Agustín")
            pausar()
        elif opcion == "6":
            print("Gracias por utilizar SkyRoute. ¡Hasta luego!")
            cerrar_conexion(conexion)
            salir = True
        else:
            print("Opción inválida, por favor intente nuevamente.")
            pausar()



if __name__ == "__main__":
    limpiar_pantalla()
    print("✈️ 🌍 Bienvenidos a SkyRoute")
    
    conexion = crear_conexion()
    if not conexion:
        print("❌ No se pudo conectar a la base de datos. Saliendo del programa.")
        exit()

    try:
        nombre = input("Nombre: ").strip()
        documento = input_int("Documento: ")
        menu_principal()
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")
    finally:
        cerrar_conexion(conexion)
        print("🔒 Conexión cerrada.")

    # # Al terminar el programa, cerrar conexión
    # cerrar_conexion(conexion)


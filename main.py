import uuid
import os


"""
---------------------------------------------------------------
SkyRoute - Sistema de Gestión de Pasajes Aéreos 
---------------------------------------------------------------

Propósito del sistema:
Este programa permite gestionar la información básica de una agencia de viajes.
Funciones disponibles:
- Gestión de clientes
- Consulta de ventas
- Visualización de reportes generales

Instrucciones de instalación y ejecución:
1. Asegurarse de tener Python instalado (versión 3.7 o superior).
2. Descargar o clonar el archivo 'main.py'.
3. Ejecutar el programa desde la terminal o consola con el siguiente comando:

    python main.py


Integrantes: 
- Marusich Leonardo 39475993
- Gonzalez Leonardo 39058972
- Trinidad Dario Exequiel 36480217
- Mazzei Juan Cruz 40443228
- Mancini Pereyra Marcelo Agustín 40110119

"""
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')


    print("✈️ 🌍 Bienvenidos a SkyRoute")

    # nombre = "sky" + str(uuid.uuid4())
    nombre =str(input("Nombre: "))
    documento= int(input("Documento: "))

    salir = False

    while not salir:
        print("📋 Menú Principal:")
        print("1. 👤 Gestionar Clientes")
        print("2. 🌍 Gestionar Destinos")
        print("3. 💰 Gestionar Ventas")
        print("4. 📊 Consultar Ventas")
        print("5. ↩️ Botón de Arrepentimiento")
        print("6. 📈 Ver Reporte General")
        print("7. ℹ️ Acerca del Sistema")
        print("8. ❌ Salir")

        
        opcion = input("Seleccione una opción: ")


        if opcion == "1":
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
                        print("Mostrando lista de clientes...")
                    elif subopcion == "2":
                        nombre = input("Ingrese el nombre del cliente: ")
                        dni = input("Ingrese el DNI del cliente: ")
                        print(f"Cliente agregado: Nombre: {nombre}, DNI: {dni}")
                    elif subopcion == "3":
                        print("Modificar cliente seleccionado...")
                    elif subopcion == "4":
                        print("Eliminar cliente seleccionado...")
                    elif subopcion == "5":
                        print("Volviendo al menú principal...")
                        volver = True
                    else:
                        print("Opción inválida, intente de nuevo.")

        elif opcion == "2":
            print("Gestión de destinos aún no implementada.")

        elif opcion == "3":
            print("Gestión de ventas aún no implementada.")

        elif opcion == "4":
            volver = False
            while not volver:
                print("\n-- CONSULTAR VENTAS --")
                print("1. Ventas del día")
                print("2. Ventas del mes")
                print("3. Ventas de la última semana")
                print("4. Volver al Menú Principal")
                subopcion = input("Seleccione una opción: ")

                if subopcion == "1":
                    print("Mostrando ventas del día...")
                elif subopcion == "2":
                    print("Mostrando ventas del mes...")
                elif subopcion == "3":
                    print("Mostrando ventas de la última semana...")
                elif subopcion == "4":
                    print("Volviendo al menú principal...")
                    volver = True
                else:
                    print("Opción inválida, intente de nuevo.")

        elif opcion == "5":
            print("Botón de arrepentimiento presionado. Operación cancelada.")

        elif opcion == "6":
            print("Mostrando reporte general...")

        elif opcion == "7":
            print("SkyRoute v1.0 - Sistema de gestión de pasajes creado en Python.")

        elif opcion == "8":
            print("Gracias por utilizar SkyRoute. ¡Hasta luego!")
            salir = True

        else:
            print("Opción inválida, por favor intente nuevamente.")


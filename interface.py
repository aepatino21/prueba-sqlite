import operations

# Global variables
isRunning = True

# Format SELECT
def format_select(data):
    for field in data:
        print(f"home_id: " + str(field[0]) + " | sensor_name: " + str(field[1]) + " | data: " + str(field[2]))


# Main loop
while isRunning:

    # Handler
    decision = 0

    # UI
    print("\n***** PRUEBA DE SQLite3 C++ y Python *****\n\n" \
    "1. Leer datos de la BD.\n" \
    "2. Insertar dato a la BD.\n" \
    "3. Actualizar dato de la BD.\n" \
    "4. Eliminar dato de la BD.\n\n" \
    "5. Cerrar aplicacion")

    decision = int(input("\nSelecciona operacion (1 - 5): "))

    # Action based on decision
    if decision == 1:
        print("\nDatos de la BD:\n")
        data = operations.read_data()

        format_select(data)

    elif decision == 2:
        sensor_name = input("\nIngresa el nombre del sensor: ")
        data = float(input("Ingresa la data del sensor: "))
        operations.insert_data(sensor_name, data)
        print("\nDato ingresado correctamente a la BD!")

    elif decision == 3:
        data = operations.read_data()
        format_select(data)
        home_id = input("\nIngresa el id del dato a actualizar: ")
        sensor_name = input("Ingresa el nombre del sensor a actualizar: ")
        data = float(input("Ingresa la data del sensor a actualizar: "))
        operations.update_data(sensor_name, data, home_id)
        print("\nDato actualizado correctamente!")

    elif decision == 4:
        data = operations.read_data()
        format_select(data)

        home_id = input("\nIngresa el id del dato a eliminar (entero): ")
        operations.delete_data(home_id)
        print("\nDato eliminado correctamente!")

    else:
        print("\nGracias por usar la app, bye ;)")
        operations.cursor.close()
        operations.conn.close()
        isRunning = False

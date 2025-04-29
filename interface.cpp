#include <iostream>
#include <sqlite3.h>
#include "operations.h"

int main() {
    int decision;
    bool isRunning = true;
    sqlite3 *db;  // Pointer for the database
    sqlite3_stmt *stmt;  // Pointer for the cursor

    // Creating or opening database
    int rc = sqlite3_open("database/home.db", &db);

    // Ejemplo de preparación de sentencia (cursor)
    const char* sql = "SELECT sqlite_version();";

    // Preparacion de uso del cursor
    rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);

    while (isRunning) {

        // Handler
        decision = 0;

        // UI
        std::cout << "\n***** PRUEBA DE SQLite3 C++ y Python *****\n\n"
                  << "1. Leer datos de la BD.\n"
                  << "2. Insertar dato a la BD.\n"
                  << "3. Cerrar aplicacion." << std::endl;

        std::cout << "\nSelecciona operacion (1 - 3): " << std::endl;
        std::cin >> decision;

        // Action based on decision
        if (decision == 1) {
            std::cout << "\nDatos de la BD:\n" << std::endl;
            readData(db);
        } else if (decision == 2) {

            char sensorName[30];
            float data;

            std::cout << "\nIngresa el nombre del sensor: " << std::endl;
            std::cin >> sensorName;

            std::cout << "\nIngresa la data del sensor: " << std::endl;
            std::cin >> data;

            insertData(db, sensorName, data);

            std::cout << "\nDato ingresado a la BD!" << std::endl;

        } else {
            std::cout << "\nGracias por usar la app, bye ;)" << std::endl;

            // Finalizar (cerrar) el cursor.
            sqlite3_finalize(stmt);

            // Cerrar la conexión a la base de datos.
            sqlite3_close(db);

            isRunning = false;
        }
    }

    return 0;
}

#include "operations.h"
#include <iostream>
#include <sqlite3.h>

bool insertData(sqlite3* db, char* sensorName, float data) {

    const char* sql = "INSERT INTO Homes(sensor_name, data) VALUES (?, ?);";
    sqlite3_stmt* stmt = nullptr;

    // Se prepara la sentencia. El -1 indica que se toma la longitud completa de la cadena.
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);

    // Vincular el primer parámetro: sensorName.
    rc = sqlite3_bind_text(stmt, 1, sensorName, -1, SQLITE_STATIC);

    // Vincular el segundo parámetro: data (se usa double ya que SQLite no tiene tipo float).
    rc = sqlite3_bind_double(stmt, 2, static_cast<double>(data));

    // Ejecutar la sentencia con sqlite3_step.
    rc = sqlite3_step(stmt);

    // Finalizar el statement para liberar recursos.
    sqlite3_finalize(stmt);
    return true;
}


bool readData(sqlite3* db) {
    // Sentencia SQL
    const char* sql = "SELECT * FROM Homes";

    sqlite3_stmt* stmt = nullptr;

    // Preparamos la sentencia SQL. El -1 indica que se toma la longitud completa de la cadena.
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, nullptr);

    // Ejecutamos la consulta y recorremos las filas de resultados
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        // La primaria columna es el id (INTEGER)
        // Se asume que la segunda columna es el nombre del sensor (TEXT)
        // y la tercera columna es el valor (DECIMAL)
        int homeId = sqlite3_column_int(stmt, 0);
        const unsigned char* sensor = sqlite3_column_text(stmt, 1);
        double data = sqlite3_column_double(stmt, 2);
        std::cout << "home_id: " << homeId << " | sensor_name: " << sensor << "| data: " << data << std::endl;
    }

    // Liberamos los recursos asociados al statement
    sqlite3_finalize(stmt);
    return true;
}

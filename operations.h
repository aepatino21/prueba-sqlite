#ifndef OPERATIONS_H
#define OPERATIONS_H
#include <sqlite3.h>

    // Prototipo de las funciones
    bool insertData(sqlite3* db, char* sensorName, float data);

    bool readData(sqlite3* db);

#endif

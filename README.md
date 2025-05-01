# Prueba SQLite3 + Python + C++
An app that uses SQLite3 databases with a CRUD in Python and data load/lecture in C++.

## Table of Contents
- [PaToDo List Backend](#patodo-list-backend)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [License](#license)

## Installation

1. Clone the repo:

```bash
git clone https://github.com/aepatino21/prueba-sqlite.git
cd prueba-sqlite
```

2. Install VSCode Extension:

- SQLite Viewer.
- Include Autocomplete.
- C/C++ (Microsoft)

## Usage

Run any of the Interfaces files: interface.cpp or interface.py

For interface.cpp:
```bash
g++ interface.cpp operations.cpp -o dataProgram -lsqlite3
```

For interface.py:
```bash
python3 interface.py
```

## License
This project is not under any license.

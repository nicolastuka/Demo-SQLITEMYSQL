import sqlite3


connection = sqlite3.connect("students.db")
cursor = connection.cursor()


def CreateTable():
    sql = """CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50),
    clase1 BOOLEAN,
    clase2 BOOLEAN,
    clase3 BOOLEAN,
    clase4 BOOLEAN
    )"""
    cursor.execute(sql)


def SaveRow(name, attendance):
    sql = f"""INSERT INTO students(name, clase1, clase2, clase3, clase4)
    VALUES('{name}', {attendance[0]}, {attendance[1]}, {attendance[2]}, {attendance[3]})"""
    cursor.execute(sql)
    connection.commit()


def PrintRows():
    sql = """SELECT * FROM students ORDER BY name ASC"""
    cursor.execute(sql)
    connection.commit()
    rows = cursor.fetchall()
    if len(rows) > 0:
        print("Alumnos cargados:\n")
        print("ID\tNOMBRE Y APELLIDO\t\t\t\t\t\tCLASE 1\tCLASE 2\tCLASE 3\tCLASE 4")
        for row in rows:
            print(f"{row[0]}\t{row[1]:50}\t\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")


CreateTable()

print("Bienvenido a AsistenciApp")
print()
running = input("¿Deseas registrar la asistencia de un estudiante? (SI/NO)")

while "s" in running.lower():
    name = input("Ingrese el nombre del estudiante: ")
    attendance = []
    for day in range(4):
        attendance.append(
            int(
                input(
                    f"Ingrese 1 si concurrió / 0 si no concurrió a la clase {day + 1}: "
                )
            )
        )
    queryUser = input(
        f"El estudiante {name} concurrió a las siguientes clases {attendance}. ¿Está seguro que desea guardar? (SI/NO)"
    )
    if "s" in queryUser.lower():
        SaveRow(name, attendance)
    running = input("¿Deseas volver registrar la asistencia de un estudiante? (SI/NO)")

PrintRows()

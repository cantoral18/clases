
from sqlite3 import*
def crearConexion():

    conn=connect("./BASE_DATOS/tenologico.db")
    conn.commit()
    conn.close()
def crearTablaAlumno():
    conn=connect("./BASE_DATOS/tenologico.db")
    cursor=conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Alumnos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT(250),
        edad INTEGER
        )

    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
        
def crearTablaCurso():
    conn=connect("./BASE_DATOS/tenologico.db")
    cursor=conn.cursor()
    sentencia="""
        CREATE TABLE IF NOT EXISTS Cursos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT(250),
        id_alumno INTEGER,
        FOREIGN KEY(id_alumno)REFERENCES Alumnos(id)
        )

    """
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
        
    
if __name__=="__main__":
    # crearConexion()
    crearTablaAlumno()
    crearTablaCurso()

def insertAlumno(nombre,edad):
    conn=connect("./BASE_DATOS/tenologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES('{nombre}',{edad})"
    cursor.execute(sentencia)
    conn.commit()
    conn.close()
if __name__=="__main__":
    # # crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    insertAlumno('jory',23) 
    insertAlumno('china',16)  

def insertAlumnos(lista):
    conn=connect("./BASE_DATOS/tenologico.db")
    cursor=conn.cursor()
    sentencia=f"INSERT INTO Alumnos(nombre,edad) VALUES(?,?)"
    cursor.executemany(sentencia,lista)
    conn.commit()
    conn.close()
if __name__=="__main__":
    # # crearConexion()
    # crearTablaAlumno()
    # crearTablaCurso()
    # insertAlumno('jory',23) 
    # insertAlumno('china',16) 
    alum=[
        ('jory',41),
        ('china',52),
        ('nadine',54)
    ]
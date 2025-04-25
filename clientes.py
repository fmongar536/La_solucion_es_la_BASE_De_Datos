import sqlite3  # Importamos la librería necesaria

class Clientes:
    def abrir(self):
        conexion = sqlite3.connect("bdclientes.db")
        try:
            conexion.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                nombre TEXT,
                apellidos TEXT,
                dni TEXT PRIMARY KEY,
                telefono TEXT,
                correo TEXT,
                direccion TEXT
            )
            """)
            conexion.commit()
        except Exception as e:
            print("❌ Ha ocurrido un error:", e)
        return conexion

    def alta(self, datos):
        conexion = self.abrir()
        try:
            conexion.execute("""
            INSERT INTO clientes(nombre, apellidos, dni, telefono, correo, direccion)
            VALUES (?, ?, ?, ?, ?, ?)
            """, datos)
            conexion.commit()
        except Exception as e:
            print("❌ Error al insertar cliente:", e)
        finally:
            conexion.close()

    def consulta(self, datos):
        conexion = self.abrir()
        try:
            cursor = conexion.execute("""
            SELECT nombre, apellidos, dni, telefono, correo, direccion
            FROM clientes
            WHERE dni = ?
            """, datos)
            resultado = cursor.fetchall()
        except Exception as e:
            print("❌ Error en la consulta:", e)
            resultado = []
        finally:
            conexion.close()
        return resultado

    def recuperar_todos(self):
        conexion = self.abrir()
        try:
            cursor = conexion.execute("SELECT nombre, apellidos, dni, telefono, correo, direccion FROM clientes")
            resultado = cursor.fetchall()
        except Exception as e:
            print("❌ Error al recuperar datos:", e)
            resultado = []
        finally:
            conexion.close()
        return resultado

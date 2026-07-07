import sqlite3
from datetime import datetime

DB_PATH = "productos.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL,
            fechaRegistro TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()


def add_producto(nombre: str, descripcion: str, cantidad: int, precio: float, categoria: str) -> None:
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute('''
        INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria, fechaRegistro)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        nombre,
        descripcion,
        cantidad,
        precio,
        categoria,
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))
    conexion.commit()
    conexion.close()


def fetch_all_productos():
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conexion.close()
    return productos


def fetch_producto_by_id(producto_id: int):
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
    producto = cursor.fetchone()
    conexion.close()
    return producto


def delete_producto_by_id(producto_id: int) -> bool:
    conexion = get_connection()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (producto_id,))
    conexion.commit()
    eliminado = cursor.rowcount > 0
    conexion.close()
    return eliminado

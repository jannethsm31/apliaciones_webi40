import web
import sqlite3

class ModeloProductos:

    def connect(self):
        try:
            self.conn = sqlite3.connect("productos.db")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as error:
            raise Exception(f"Error al conectar a la base de datos: {error}")
    
    def ObtenerTodosProductos(self):
        response = []
        try:
            self.connect()
            query = "SELECT * FROM productos"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                product = {
                    "id_productos": row[0],
                    "nombre": row[1],
                    "descripcion": row[2],
                    "precio": row[3],
                    "existencias": row[4]
                }
                response.append(product)
        except sqlite3.Error as error:
            raise Exception(f"Error al mostrar todos los productos: {error}")
        finally:
            self.conn.close()
        return response

    def ActualizarProducto(self, producto):
        try:
            with sqlite3.connect("productos.db") as conn:
                cursor = conn.cursor()
                query = "UPDATE productos SET nombre = ?, descripcion = ?, precio = ?, existencias = ? WHERE id_productos = ?"
                cursor.execute(query, (producto["nombre"], producto["descripcion"], producto["precio"], producto["existencias"], producto["id_productos"]))
                result = cursor.rowcount
                conn.commit()
                return bool(result)
        except sqlite3.Error as error:
            raise Exception(f"Error en la base de datos al actualizar el producto: {error}")

    def DetallesProductos(self, idProducto):
        try:
            print("id", idProducto)
            with sqlite3.connect("productos.db") as conn:
                cursor = conn.cursor()
                query = 'SELECT * FROM productos WHERE id_productos = ? '
                cursor.execute(query, (idProducto,))
                row = cursor.fetchone()
                if row:
                    product = {
                        "id_productos": row[0],
                        "nombre": row[1],
                        "descripcion": row[2],
                        "precio": row[3],
                        "existencias": row[4]
                    }
                    return product
                else:
                    return None
        except sqlite3.Error as error:
            raise Exception(f"Error en la base de datos al obtener los detalles del producto: {error}")

    def insertarProducto(self, producto):
        respuesta = False
        try:
            with sqlite3.connect("productos.db") as conn:
                cursor = conn.cursor()
                query = 'INSERT INTO productos (nombre, descripcion, precio, existencias) VALUES (?,?,?,?)'
                cursor.execute(query, (producto["nombre"], producto["descripcion"], int(producto["precio"]), int(producto["existencias"])))
                result = cursor.rowcount
                if result:
                    respuesta = True
                conn.commit()
        except sqlite3.Error as error:
            raise Exception(f"Error en la base de datos al insertar el producto: {error}")
        return respuesta

    def BorrarProductos(self, idProducto):
        result = False
        try:
            with sqlite3.connect("productos.db") as conn:
                cursor = conn.cursor()
                query = 'DELETE FROM productos WHERE id_productos = ?'
                cursor.execute(query, (idProducto,))
                producto_borrado = cursor.rowcount
                conn.commit()
                if producto_borrado > 0:
                    result = True
        except sqlite3.Error as error:
            raise Exception(f"Error en la base de datos al borrar el producto: {error}")
        return result

    def BuscarProductos(self, nombreProducto):
        resultado = []
        try:
            with sqlite3.connect("productos.db") as conn:
                cursor = conn.cursor()
                nombreProducto = nombreProducto.lower()
                query = 'SELECT * FROM productos WHERE LOWER(nombre) LIKE ?'
                cursor.execute(query, ('%' + nombreProducto + '%', ))
                print('nombre', cursor)
                for row in cursor:
                    producto = {
                        "id_productos": row[0],
                        "nombre": row[1],
                        "descripcion": row[2],
                        "precio": row[3],
                        "existencias": row[4]
                    }
                    resultado.append(producto)
        except sqlite3.Error as error:
            raise Exception(f"Error en la base de datos al buscar productos: {error}")
        return resultado
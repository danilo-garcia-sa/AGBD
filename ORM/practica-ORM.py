from sqlalchemy import create_engine, Column, Integer, String, Numeric, Boolean, and_
from sqlalchemy.orm import declarative_base, sessionmaker

# Ejercicio 1

Base = declarative_base()


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, nullable=False)
    activo = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio})>"


engine = create_engine("sqlite:///productos.db", echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Ejercicio 2

def cargar_productos():
    if session.query(Producto).count() > 0:
        print("Ya hay productos cargados, no se insertan de nuevo.")
        return

    productos = [
        Producto(nombre="Teclado mecanico", categoria="perifericos", precio=8500, stock=15),
        Producto(nombre="Mouse inalambrico", categoria="perifericos", precio=4200, stock=30),
        Producto(nombre="Monitor 24 pulgadas", categoria="monitores", precio=62000, stock=8),
        Producto(nombre="Auriculares bluetooth", categoria="audio", precio=12300, stock=20),
        Producto(nombre="Webcam Full HD", categoria="perifericos", precio=9800, stock=12),
        Producto(nombre="SSD 1TB", categoria="almacenamiento", precio=18500, stock=25),
        Producto(nombre="RAM 16GB", categoria="componentes", precio=15600, stock=18),
        Producto(nombre="Mousepad XL", categoria="perifericos", precio=2100, stock=40),
        Producto(nombre="Hub USB-C", categoria="accesorios", precio=5400, stock=6, activo=False),
        Producto(nombre="Cable HDMI", categoria="accesorios", precio=1800, stock=50),
    ]

    session.add_all(productos)
    session.commit()

    cantidad = session.query(Producto).count()
    print(f"Se cargaron los productos. Cantidad en la tabla: {cantidad}")

# Ejercicio 3

def productos_perifericos():
    print("\nProductos de la categoria 'perifericos'")
    resultado = session.query(Producto).filter(Producto.categoria == "perifericos").all()
    for p in resultado:
        print(f"{p.nombre} - ${p.precio}")

# Ejercicio 4

def productos_caros():
    print("\nProductos con precio mayor a $10000")
    resultado = (
        session.query(Producto)
        .filter(Producto.precio > 10000)
        .order_by(Producto.precio.desc())
        .all()
    )
    for p in resultado:
        print(f"{p.nombre} - ${p.precio}")

# Ejercicio 5

def productos_bajo_stock_activos():
    print("\nProductos con stock <= 12 y activos")
    resultado = (
        session.query(Producto)
        .filter(Producto.stock <= 12, Producto.activo == True)
        .all()
    )
    for p in resultado:
        print(f"{p.nombre} - stock: {p.stock}")

# Ejercicio 6

def productos_rango_precio():
    print("\nProductos con precio entre $5000 y $20000")
    resultado = (
        session.query(Producto)
        .filter(Producto.precio >= 5000)
        .filter(Producto.precio <= 20000)
        .all()
    )
    for p in resultado:
        print(f"{p.nombre} - ${p.precio}")

    # Misma consulta usando and_()
    resultado_and = (
        session.query(Producto)
        .filter(and_(Producto.precio >= 5000, Producto.precio <= 20000))
        .all()
    )
    print(f"Cantidad con and_(): {len(resultado_and)}")

# Ejercicio 7

def producto_mas_caro():
    print("\nProducto mas caro de la tabla")
    resultado = session.query(Producto).order_by(Producto.precio.desc()).first()
    print(f"{resultado.nombre} - ${resultado.precio}")

# Ejercicio 8

def productos_inactivos():
    print("\nProductos inactivos")
    resultado = session.query(Producto).filter(Producto.activo == False).all()
    for p in resultado:
        print(f"{p.nombre} - activo: {p.activo}")


if __name__ == "__main__":
    cargar_productos()
    productos_perifericos()
    productos_caros()
    productos_bajo_stock_activos()
    productos_rango_precio()
    producto_mas_caro()
    productos_inactivos()

    session.close()
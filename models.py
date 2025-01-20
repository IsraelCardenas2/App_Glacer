from conexion_db import Database
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Date

class Admin(Database):
    __tablename__ = 'administradores'
    Id_Admin = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Apellidos = Column(String(50))
    Usuario = Column(String(50), unique=True)
    Contrasena = Column(String(256))
    Privilegio = Column(String(50))
    activo = Column(Boolean, default=False) 

class SubAdmin(Database):
    __tablename__ = 'subadministradores'
    Id_Sub_Admin = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Apellidos = Column(String(50))
    Usuario = Column(String(50), unique=True)
    Contrasena = Column(String(256))
    Direccion = Column(String(50))
    Privilegio = Column(String(50))
    activo = Column(Boolean, default=False) 
    
class Productos(Database):
    __tablename__ = 'productos'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Marca = Column(String(30))
    Modelo = Column(String(50))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    IMG3 = Column(String(256))
    IMG4 = Column(String(256))

    
# class Marca(Database):
#     __tablename__ = 'marcas'
#     Id_Marca = Column(Integer, primary_key=True)
#     Nombre = Column(String(50))
#     Id_Categoria = Column(String(50))
#     Id_Departamento = Column(String(50))
    
class Medidas(Database):
    __tablename__ = 'medidas'
    Id_Medida = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Id_Marca = Column(String(50))
    Id_Categoria = Column(String(50))
    
# ----------------------------------------------- Departamento de pisos Vitromex------------------------------------
class Vitro_20x20(Database):
    __tablename__ = 'vitro_20x20'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Vitro_20x30(Database):
    __tablename__ = 'vitro_20x30'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Vitro_30x60(Database):
    __tablename__ = 'vitro_30x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Vitro_36x36(Database):
    __tablename__ = 'vitro_36x36'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Vitro_36x50(Database):
    __tablename__ = 'Vitro_36x50'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Vitro_37x37(Database):
    __tablename__ = 'vitro_37x37'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Vitro_45x45(Database):
    __tablename__ = 'vitro_45x45'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_50x100(Database):
    __tablename__ = 'vitro_50x100'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_55x55(Database):
    __tablename__ = 'vitro_55x55'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_60x60(Database):
    __tablename__ = 'vitro_60x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_60x120(Database):
    __tablename__ = 'vitro_60x120'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_61x61(Database):
    __tablename__ = 'vitro_61x61'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_62x62(Database):
    __tablename__ = 'vitro_62x62'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_duelas(Database):
    __tablename__ = 'vitro_duelas'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Vitro_otras(Database):
    __tablename__ = 'vitro_otras'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    


# --------------------------------------------- Daltile ------------------------------
class Dal_30x45(Database):
    __tablename__ = 'dal_30x45'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Dal_37x37(Database):
    __tablename__ = 'dal_37x37'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Dal_45x45(Database):
    __tablename__ = 'dal_45x45'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    


class Dal_60x60(Database):
    __tablename__ = 'dal_60x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      
    
class Dal_duelas(Database):
    __tablename__ = 'dal_duelas'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Dal_otras(Database):
    __tablename__ = 'dal_otras'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      


#-------------------------------------- Tecnopisos ----------------------------------------------
class Tecno_30x60(Database):
    __tablename__ = 'tecno_30x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
          

class Tecno_duelas(Database):
    __tablename__ = 'tecno_duelas'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Tecno_otras(Database):
    __tablename__ = 'tecno_otras'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
     

# # ------------------------------------------- Castel -------------------------------------

class Cast_60x60(Database):
    __tablename__ = 'cast_60x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))

    
class Cast_60x120(Database):
    __tablename__ = 'cast_60x120'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))

class Cast_duela(Database):
    __tablename__ = 'cast_duelas'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))

#---------------------------------------------- Minato ---------------------------------
    
class Min_30x45(Database):
    __tablename__ = 'min_30x45'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Min_30x60(Database):
    __tablename__ = 'min_30x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Min_60x60(Database):
    __tablename__ = 'min_60x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
     

class Min_60x120(Database):
    __tablename__ = 'min_60x120'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
           

class Min_otras(Database):
    __tablename__ = 'min_otras'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))    
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

#----------------------------------------------- Cesantoni -------------------------------------------

class Ces_30x60(Database):
    __tablename__ = 'ces_30x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Ces_otras(Database):
    __tablename__ = 'ces_otras'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Ces_duelas(Database):
    __tablename__ = 'ces_duelas'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
          

#----------------------------------------------------- Greda ------------------------------------------------

class Gre_30x45(Database):
    __tablename__ = 'gre_30x45'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

class Gre_30x60(Database):
    __tablename__ = 'gre_30x60'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      
    
class Gre_otras(Database):
    __tablename__ = 'gre_otras'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Id_Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
      

#-------------------------------------------------- Sobran estos modelos ----------------------------------------

# class Dal_60x60(Database):
#     __tablename__ = 'productos'
#     Id_Producto = Column(Integer, primary_key=True)
#     Nombre = Column(String(35))
#     Precio = Column(String(10))
#     Marca = Column(String(30))
#     Modelo = Column(String(50))
#     Material = Column(String(50))
#     Acabado = Column(String(50))
#     Color = Column(String(30))
#     Id_Medida = Column(String(15))
#     Contenido = Column(String(30))
#     Calidad = Column(String(50))
#     Imagen = Column(String(256))
#     IMG2 = Column(String(256))
#     IMG3 = Column(String(256))
#     IMG4 = Column(String(256))  

# class Dal_60x60(Database):
#     __tablename__ = 'productos'
#     Id_Producto = Column(Integer, primary_key=True)
#     Nombre = Column(String(35))
#     Precio = Column(String(10))
#     Marca = Column(String(30))
#     Modelo = Column(String(50))
#     Material = Column(String(50))
#     Acabado = Column(String(50))
#     Color = Column(String(30))
#     Id_Medida = Column(String(15))
#     Contenido = Column(String(30))
#     Calidad = Column(String(50))
#     Imagen = Column(String(256))
#     IMG2 = Column(String(256))
#     IMG3 = Column(String(256))
#     IMG4 = Column(String(256))      

# class Dal_60x60(Database):
#     __tablename__ = 'productos'
#     Id_Producto = Column(Integer, primary_key=True)
#     Nombre = Column(String(35))
#     Precio = Column(String(10))
#     Marca = Column(String(30))
#     Modelo = Column(String(50))
#     Material = Column(String(50))
#     Acabado = Column(String(50))
#     Color = Column(String(30))
#     Id_Medida = Column(String(15))
#     Contenido = Column(String(30))
#     Calidad = Column(String(50))
#     Imagen = Column(String(256))
#     IMG2 = Column(String(256))
#     IMG3 = Column(String(256))
#     IMG4 = Column(String(256))  

# class Dal_60x60(Database):
#     __tablename__ = 'productos'
#     Id_Producto = Column(Integer, primary_key=True)
#     Nombre = Column(String(35))
#     Precio = Column(String(10))
#     Marca = Column(String(30))
#     Modelo = Column(String(50))
#     Material = Column(String(50))
#     Acabado = Column(String(50))
#     Color = Column(String(30))
#     Id_Medida = Column(String(15))
#     Contenido = Column(String(30))
#     Calidad = Column(String(50))
#     Imagen = Column(String(256))
#     IMG2 = Column(String(256))
#     IMG3 = Column(String(256))
#     IMG4 = Column(String(256))  
    
# class Dal_60x60(Database):
#     __tablename__ = 'productos'
#     Id_Producto = Column(Integer, primary_key=True)
#     Nombre = Column(String(35))
#     Precio = Column(String(10))
#     Marca = Column(String(30))
#     Modelo = Column(String(50))
#     Material = Column(String(50))
#     Acabado = Column(String(50))
#     Color = Column(String(30))
#     Id_Medida = Column(String(15))
#     Contenido = Column(String(30))
#     Calidad = Column(String(50))
#     Imagen = Column(String(256))
#     IMG2 = Column(String(256))
#     IMG3 = Column(String(256))
#     IMG4 = Column(String(256))  

# class Dal_60x60(Database):
#     __tablename__ = 'productos'
#     Id_Producto = Column(Integer, primary_key=True)
#     Nombre = Column(String(35))
#     Precio = Column(String(10))
#     Marca = Column(String(30))
#     Modelo = Column(String(50))
#     Material = Column(String(50))
#     Acabado = Column(String(50))
#     Color = Column(String(30))
#     Id_Medida = Column(String(15))
#     Contenido = Column(String(30))
#     Calidad = Column(String(50))
#     Imagen = Column(String(256))
#     IMG2 = Column(String(256))
#     IMG3 = Column(String(256))
#     IMG4 = Column(String(256))  

    




    




    




    




# ------------------------------------------------ Categorías de Grifería ---------------------------------------------
class G_Categorias(Database):
    __tablename__ = 'categorias_grif'
    Id_Sub_Admin = Column(Integer, primary_key=True)
    Nombre = Column(String(50))

class Perfil(Database):
    __tablename__ = 'perfiles'
    Id_Perfil = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(30)) 
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Cenefa(Database):
    __tablename__ = 'cenefas'
    Id_Cenefa = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Maya(Database):
    __tablename__ = 'mallas'
    Id_Maya = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Maneral(Database):
    __tablename__ = 'manerales'
    Id_Maneral = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Tipo_install = Column(String(20))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Regadera(Database):
    __tablename__ = 'regaderas'
    Id_Regadera = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Flujo_agua = Column(String(70))
    Presion = Column(String(60))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Brazo(Database):
    __tablename__ = 'brazos'
    Id_Brazo = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Flujo_agua = Column(String(70))
    Presion = Column(String(60))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Tocador(Database):
    __tablename__ = 'tocadores'
    Id_Tocador = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Parrilla(Database):
    __tablename__ = 'parrillas'
    Id_Parrilla = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Campana(Database):
    __tablename__ = 'campanas'
    Id_Campana = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
#--------------------------- analisis -----------------------    
    
class Tarja(Database):
    __tablename__ = 'tarjas'
    Id_Tarja = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Accesorio(Database):
    __tablename__ = 'accesorios_banos'
    Id_Accesorio = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Complementos = Column(String(70))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Dispensador(Database):
    __tablename__ = 'dispensadores_jabon'
    Id_Dispensador = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Capacidad = Column(String(70))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Mezcladora(Database):
    __tablename__ = 'mezcladoras'
    Id_Mezcladora = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Presion = Column(String(70))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Monomando(Database):
    __tablename__ = 'monomandos'
    Id_Monomando  = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Presion = Column(String(70))
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Kits_install(Database):
    __tablename__ = 'kits_instalacion'
    Id_Kit_install = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Marca = Column(String(20))
    Medida_llaves = Column(String(20))
    Material = Column(String(35))
    Contracanasta = Column(String(70))
    Alimentador = Column(String(70))
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Persiana(Database):
    __tablename__ = 'persianas'
    Id_Persiana = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(35))
    Complementos = Column(String(200))
    Tiempo_entrega = Column(String(70))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))

class Organizador(Database):
    __tablename__ = 'organizadores_bano'
    Id_Oganizador = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Asiento(Database):
    __tablename__ = 'asientos'
    Id_Asiento = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Tipo = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Ovalin(Database):
    __tablename__ = 'ovalines'
    Id_Ovalin = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Tipo_colocacion = Column(String(35))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
#-------------------------------------------------
class Separador(Database):
    __tablename__ = 'separadores'
    Id_Separador = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Herramienta_Col(Database):
    __tablename__ = 'herramientas_colocacion'
    Id_Herramienta = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Calentador_S(Database):
    __tablename__ = 'calentadores_sol'
    Id_CalentadorS = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Capacidad= Column(Integer)
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Calentador_P(Database):
    __tablename__ = 'calentadores_pas'
    Id_CalentadorP = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Capacidad= Column(Integer)
    Servicios = Column(String(60))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Espejo(Database):
    __tablename__ = 'espejos'
    Id_Espejo = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    color = Column(String(20))
    Material = Column(String(55))
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Repisa(Database):
    __tablename__ = 'repisas'
    Id_Repisa = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(40))
    Marca = Column(String(40))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Resumidero(Database):
    __tablename__ = 'resumideros'
    Id_Resumidero = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Contra_Can(Database):
    __tablename__ = 'contracanastas'
    Id_Contra_C = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Cespol(Database):
    __tablename__ = 'cespols'
    Id_Cespol = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Impermeabilizante(Database):
    __tablename__ = 'impermeabilizantes'
    Id_Imper = Column(Integer, primary_key=True)
    Nombre = Column(String(50))
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Color = Column(String(20))
    Marca = Column(String(20))
    Contenido = Column(String(20))
    Duracion = Column(String(40))
    Caracteristicas = Column(String(300))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Panel_Cancel(Database):
    __tablename__ = 'paneles_canceles'
    Id_Panel_Can = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Tina(Database):
    __tablename__ = 'tinas'
    Id_Tina = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Capacidad = Column(String(70))
    Tipo = Column(String(50))
    Complementos = Column(String(200))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

# --------------------------------------------------- Departamento de Baños ---------------------------------------------

class Inodoro(Database):
    __tablename__ = 'inodoros'
    Id_Inodoro = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Modelo = Column(String(200))
    Calidad = Column(String(50))
    Consumo_agua = Column(String(70))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Migitorio(Database):
    __tablename__ = 'migitorios'
    Id_Migitorio = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Acabado = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Lavabo(Database):
    __tablename__ = 'lavabos'
    Id_Lavabo = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Kit_Sanitario(Database):
    __tablename__ = 'kits_san'
    Id_Kit_S = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Calidad = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Tinacos(Database):
    __tablename__ = 'tinacos'
    Id_Tinaco = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Precio = Column(String(10))
    PrecioAnt = Column(String(6))
    Codigo = Column(String(15))
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Calidad = Column(String(55))
    Capacidad = Column(String(55))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
    #---------------------------------- Sección de Ofertas ----------------------------------------------------
    
class Pisos_Mur (Database):
    __tablename__ = 'pisos_muros'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Codigo = Column(String(15))
    Precio = Column(String(10))
    Precio_ant = Column(String(10))
    Medida = Column(String(15))
    Color = Column(String(30))
    Marca = Column(String(30))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    

class Grif_Ban(Database):
    __tablename__ = 'grif_bans'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(50)) 
    Codigo = Column(String(15))
    Precio = Column(Integer)
    Precio_ant = Column(Integer)
    Medida = Column(String(20))
    Color = Column(String(20))
    Marca = Column(String(20))
    Material = Column(String(55))
    Detalles = Column(String(500))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
#-------------------------------------------- Sección de los más productos por marca -------------------------------------------------

class Vitro_MasVen(Database):
    __tablename__ = 'vitro_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Daltile_MasVen(Database):
    __tablename__ = 'daltile_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Tecno_MasVen(Database):
    __tablename__ = 'Tecno_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Minato_MasVen(Database):
    __tablename__ = 'minato_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Castel_MasVen(Database):
    __tablename__ = 'castel_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Cesantoni_MasVen(Database):
    __tablename__ = 'Cesantoni_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
class Greda_MasVen(Database):
    __tablename__ = 'Greda_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
    
    
class Arko_MasVen(Database):
    __tablename__ = 'arko_mas_vend'
    Id_Producto = Column(Integer, primary_key=True)
    Nombre = Column(String(35))
    Precio = Column(String(10))
    Codigo = Column(String(15))
    Marca = Column(String(30))
    PrecioAnt = Column(String(6))
    Material = Column(String(50))
    Acabado = Column(String(50))
    Color = Column(String(30))
    Medida = Column(String(15))
    Contenido = Column(String(30))
    Calidad = Column(String(50))
    Imagen = Column(String(256))
    IMG2 = Column(String(256))
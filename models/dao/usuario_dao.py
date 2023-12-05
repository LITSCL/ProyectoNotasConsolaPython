from database.conexion import Conexion
from models.dto.usuario import Usuario

class UsuarioDAO:
    __db: Conexion = Conexion()
    
    def save(self, usuario: Usuario) -> bool:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"INSERT INTO usuario VALUES('{usuario.get_correo()}', '{usuario.get_nombre()}', '{usuario.get_apellido()}', '{usuario.get_clave()}', NOW())"
                
                cursor.execute(query)
                conexion.commit()
                
                if (cursor.rowcount >= 1):
                    return True
                else:
                    return False
            except:
                return False 
            finally:
                cursor.close()
                conexion.close()
        else:
            return False
        
    def find(self, correo: str) -> Usuario:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"SELECT * FROM usuario WHERE correo = '{correo}'"
                
                cursor.execute(query)
                resultado: tuple = cursor.fetchone()

                if (cursor.rowcount >= 1):
                    usuario: Usuario = Usuario(resultado[0], resultado[1], resultado[2], resultado[3], resultado[4])
                    return usuario
                else:
                    return None
            except:
                return None
            finally:
                cursor.close()
                conexion.close()
        else:
            return None
            
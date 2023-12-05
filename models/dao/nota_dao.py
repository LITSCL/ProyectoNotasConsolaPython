from typing import List

from database.conexion import Conexion
from models.dto.nota import Nota

class NotaDAO:
    __db: Conexion = Conexion()
    
    def save(self, nota: Nota) -> bool:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"INSERT INTO nota VALUES(null, '{nota.get_titulo()}', '{nota.get_descripcion()}', NOW(), '{nota.get_usuario_fk()}')"
                
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
        
    def get_all(self) -> List[Nota]:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"SELECT * FROM nota"
                
                cursor.execute(query)
                resultado = cursor.fetchall()
                
                if (cursor.rowcount >= 1):
                    notas: List[Nota] = []
                    for fila in resultado:
                        nota: Nota = Nota(fila[0], fila[1], fila[2], fila[3], fila[4])
                        notas.append(nota)
                    return notas
                else:
                    return None
            except:
                return None 
            finally:
                cursor.close()
                conexion.close()
        else:
            return None
        
    def delete(self, id: int) -> bool:
        if (self.__db.conectar() == True):
            conexion: object = self.__db.get_conexion()
            cursor: object = self.__db.get_cursor()
            
            try:
                query: str = f"DELETE FROM nota WHERE id = {id}"
                
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
import mysql.connector

class Conexion:
    __conexion: object = None
    
    def get_conexion(self) -> object:
        if (self.__conexion != None):
            return self.__conexion
        else:
            return None
    
    def conectar(self) -> bool:
        try:       
            self.__conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "root",
                database = "dbproyectonotasconsolapython",
                port = 3306
            )
            return True
        except:
            self.__conexion = None
            return False
    
    def get_cursor(self) -> object:
        if (self.__conexion != None):
            return self.__conexion.cursor()
        else:
            return None
        
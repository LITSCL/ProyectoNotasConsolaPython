import hashlib

from models.dto.usuario import Usuario
from models.dao.usuario_dao import UsuarioDAO

class UsuarioControlador:
    __dao_usuario: UsuarioDAO = UsuarioDAO()
    
    #Método controlador (Registro).
    def registro(self) -> None:
        print("Seleccionaste Registro")
        
        correo: str = input("Introduce tu correo: ")
        nombre: str = input("¿Cual es tu nombre?: ")
        apellido: str = input("¿Cual es tu apellido?: ")
        
        clave: str = input("Introduce tu contraseña: ")
        clave_encriptada: str = (hashlib.sha256(clave.encode("UTF8"))).hexdigest()
        
        usuario: Usuario = Usuario(nombre, apellido, correo, clave_encriptada, None)
        
        if (self.__dao_usuario.save(usuario) == True):
            print("Usuario creado correctamente")
        else:
            print("Error al crear el usuario")
        
    #Método controlador (Identificación).
    def identificacion(self) -> Usuario:
        print("Seleccionaste Login")
        
        correo: str = input("Introduce tu correo: ")
        
        clave: str = input("Introduce tu contraseña: ")
        clave_encriptada: str = (hashlib.sha256(clave.encode("UTF8"))).hexdigest()
        
        if (self.__dao_usuario.find(correo) != None):
            usuario: Usuario = self.__dao_usuario.find(correo)
            if (usuario.get_clave() == clave_encriptada):
                print(f"Bienvenido: {usuario.get_correo()}, eres miembro desde {usuario.get_fecha()}")
                return usuario
            else:
                print("Clave incorrecta")
                return None
        else:
            print("El correo ingresado no existe en el sistema")
            return None
            
        
        
        
        
        
        
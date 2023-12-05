from models.dto.usuario import Usuario
from controllers.usuario_controlador import UsuarioControlador
from controllers.nota_controlador import NotaControlador

class Main:
    __usuario_controlador: UsuarioControlador = UsuarioControlador()
    __nota_controlador: NotaControlador = NotaControlador()
    
    #Menu Principal.
    def menu(self) -> bool:
        continuar: bool = True
        
        print("Acciones disponibles:")
        print("1. Registro")
        print("2. Identificarse")
        print("0. Salir")
        
        opcion: str = input("¿Que quieres hacer?")
        
        if (opcion == "1"):
            self.__usuario_controlador.registro()
        elif (opcion == "2"):
            usuario: Usuario = self.__usuario_controlador.identificacion()
            if (usuario != None):
                while (self.menu_sesion(usuario) == True):
                    None
        elif (opcion == "0"):
            continuar = False
        else:
            print("Opción incorrecta")
        return continuar
    
    #Menu de sesión.
    def menu_sesion(self, usuario: Usuario) -> bool:
        continuar: bool = True
        
        print("Acciones disponibles:")
        print("1. Crear nota")
        print("2. Mostrar notas")
        print("3. Eliminar nota")
        print("0. Cerrar sesión")
              
        opcion: str = input("¿Que quieres hacer?")
        
        if (opcion == "1"):
            self.__nota_controlador.crear(usuario)
        elif (opcion == "2"):
            self.__nota_controlador.mostrar()
        elif (opcion == "3"):
            self.__nota_controlador.eliminar()
        elif (opcion == "0"):
            print("0")
            continuar = False
        else:
            print("Opción incorrecta")
        return continuar
    
main: Main = Main()
while (main.menu() == True):
    None
    

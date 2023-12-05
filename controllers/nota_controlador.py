from typing import List

from models.dto.nota import Nota
from models.dto.usuario import Usuario
from models.dao.nota_dao import NotaDAO

class NotaControlador:
    __dao_nota: NotaDAO = NotaDAO()
    
    #Método controlador (Crear).
    def crear(self, usuario: Usuario) -> None:
        print("Seleccionaste Crear")
        
        titulo: str = input("Introduce el título: ")
        descripcion: str = input("Introduce la descripción: ")
        correo_usuario: str = usuario.get_correo()
        
        nota: Nota = Nota(None, titulo, descripcion, None, correo_usuario)
        
        if (self.__dao_nota.save(nota) == True):
            print("Nota creada correctamente")
        else:
            print("Error al crear la nota")
    
    #Método controlador (Mostrar).  
    def mostrar(self) -> None:
        print("Seleccionaste Mostrar")
        
        notas: List[Nota] = self.__dao_nota.get_all()
        for nota in notas:
            print(f"ID: {nota.get_id()}; Título: {nota.get_titulo()}; Descripción: {nota.get_descripcion()}; Fecha: {nota.get_fecha()}; Correo: {nota.get_usuario_fk()}")
    
    #Método controlador (Mostrar).  
    def eliminar(self):
        print("Seleccionaste Eliminar")
        
        id: int = int(input("Introduce el ID de la nota que deseas eliminar: "))
        
        if (self.__dao_nota.delete(id) == True):
            print("Nota eliminada correctamente")
        else:
            print("Error al eliminar la nota")
                
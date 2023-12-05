class Nota:
    __id: int = None
    __titulo: str = None
    __descripcion: str = None
    __fecha: str = None
    __usuario_fk: int = None
    
    def __init__(self, id: int, titulo: str, descripcion: str, fecha: str, usuario_fk: int) -> None:
        self.__id = id
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__fecha = fecha
        self.__usuario_fk = usuario_fk

    def get_id(self) -> int:
        return self.__id

    def get_titulo(self) -> str:
        return self.__titulo

    def get_descripcion(self) -> str:
        return self.__descripcion

    def get_fecha(self) -> str:
        return self.__fecha

    def get_usuario_fk(self) -> int:
        return self.__usuario_fk

    def set_id(self, id: int) -> None:
        self.__id = id

    def set_titulo(self, titulo: str) -> None:
        self.__titulo = titulo

    def set_descripcion(self, descripcion: str) -> None:
        self.__descripcion = descripcion

    def set_fecha(self, fecha: str) -> None:
        self.__fecha = fecha

    def set_usuario_fk(self, usuario_fk: int) -> None:
        self.__usuario_correo = usuario_fk
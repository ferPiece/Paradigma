from abc import ABCMeta, abstractmethod
import util
from i18n import msg

def coalesce(objeto, default):
    if not objeto:
        return default
    else:
        return objeto

class Modulo(metaclass=ABCMeta):

    def __init__(self, titulo_menu='**** MENU ****'):
        self.__titulo_menu = titulo_menu
        self.__terminar_ejecucion = False

    def get_terminar_ejecucion(self):
        return self.__terminar_ejecucion

    def set_terminar_ejecucion(self, terminar_ejecucion):
        self.__terminar_ejecucion = terminar_ejecucion

    def get_titulo_menu(self):
        return self.__titulo_menu

    def set_titulo_menu(self, titulo_menu):
        self.__titulo_menu = titulo_menu

    @abstractmethod
    def get_menu_dict(self):
        pass

    def pausa(self):
       util.pausa(msg('presionar.enter.continuar'))

    def mostrar_menu(self):
        print(self.get_titulo_menu())
        for key  in self.get_menu_dict().keys():
            menu = self.get_menu_dict().get(key)
            print(key, menu.get_titulo())

        print("")

    def iniciar(self):
        self.set_terminar_ejecucion(False)
        cant_menu = len(self.get_menu_dict())
        while (not self.get_terminar_ejecucion()):
            util.limpiar_pantalla()
            self.mostrar_menu()
            opcion = util.leer_entero(msg('ingresar.opcion'), min_value=1, max_value=cant_menu)
            menu_seleccionado = self.get_menu_dict()[opcion]
            menu_seleccionado.ejecutar_funcion()


class Menu():
    def __init__(self, titulo, funcion):
        self.__titulo = titulo
        self.__funcion = funcion

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_funcion(self):
        return self.__funcion

    def set_funcion(self, funcion):
        self.__funcion = funcion

    def ejecutar_funcion(self):
        self.__funcion()

########################################################################
# Solo para operar la vista del sistema
class Usuario:
    """Estructura de la persona que opera un sistema, al ser un usuario
    hereda propiedades de persona fisica"""

    def __init__(self, codigo='<SD>', nombre='<SD>', apellido='<SD>'):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__apellido = apellido
    
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido
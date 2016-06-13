import sys
sys.path.append("../")  # referencia al directorio base
from model import Modulo, Menu
from modelo import Contacto
from controladores import ControladorContacto
from i18n import msg
import util
from contexto import *
import ZODB
import BTrees.OOBTree
import transaction, persistent

class ModuloContacto(Modulo):
    __controlador = ControladorContacto()

    def __init__(self):
        Modulo.__init__(self, msg('abm.contacto.menu.titulo'))
        self.__menu_dict = None

    def listar(self):
        contactos = self.get_controlador().get_lista_objetos()
        print(msg('abm.contacto.titulo.lista'))
        for cont in contacto:
            print(cont.__str__())        
        self.pausa()

    def registrar(self):
        print(msg('abm.contacto.titulo.registrar'))
        obligatorio = True

        numero_telefonico = util.leer_cadena(msg('contacto.ingrese.numero_telefonico'), obligatorio)
        correo_electronico = str(util.leer_cadena(msg('contacto.ingrese.correo_electronico'), obligatorio))
        
        contacto = Contacto(numero_telefonico,correo_electronico)

        try:
            self.get_controlador().crear(contacto)
            print(msg("registro.creado"))
        except Exception as e:
            print(e)
        self.pausa()

    def borrar(self):
        print(msg('abm.contacto.titulo.borrar'))
        obligatorio = True
        numero_telefonico = util.leer_cadena(msg('contacto.ingrese.numero_telefonico'), obligatorio)
        try:
            contacto = self.get_controlador().buscar_codigo(numero_telefonico)
            if not contacto:
                print(msg('contacto.cedula.no.existe'), ":", numero_telefonico)
            else:
                self.get_controlador().borrar(contacto)
                print(msg('contacto.borrado'))
        except Exception as e:
            print(e)
        self.pausa()

    def consultar_contacto(self):
        obligatorio = True
        numero_telefonico = util.leer_cadena(msg('contacto.ingrese.numero_telefonico'), obligatorio)
        
        try:
            if not util.es_numerico(numero_telefonico):
                raise Exception("El numero_telefonico debe ser numerico!")
                
            contacto = ControladorContacto().buscar_codigo(numero_telefonico)
            return contacto
        except Exception as e:
            print(e)

    def ir_menu_principal(self):
        self.set_terminar_ejecucion(True)

    def get_controlador(self):
        return self.__controlador

    def get_menu_dict(self):
        #crear en caso de que aun no se haya creado
        if not self.__menu_dict:
            menu_listar = Menu(msg('abm.contacto.listar'), self.listar)
            menu_registrar = Menu(msg('abm.contacto.registrar'), self.registrar)
            #menu_borrar = Menu(msg('abm.contacto.borrar'), self.borrar)
            menu_principal = Menu(msg('abm.ir.menu.principal'),self.ir_menu_principal)
            menus = {1: menu_listar, 2: menu_registrar, 3: menu_principal}
            self.__menu_dict = menus

        return self.__menu_dict


if __name__ == "__main__":
    ma = ModuloContacto()
    ma.iniciar()            

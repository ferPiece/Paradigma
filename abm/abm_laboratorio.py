import sys
sys.path.append("../")  # referencia al directorio base
from model import Modulo, Menu
from modelo import Laboratorio
from controladores import ControladorLaboratorio
from i18n import msg
import util
from contexto import *
import ZODB
import BTrees.OOBTree
import transaction, persistent

class ModuloLaboratorio(Modulo):
    __controlador = ControladorLaboratorio()

    def __init__(self):
        Modulo.__init__(self, msg('abm.laboratorio.menu.titulo'))
        self.__menu_dict = None

    def listar(self):
        laboratorios = self.get_controlador().get_lista_objetos()
        print(msg('abm.laboratorio.titulo.lista'))
        for lab in laboratorio:
            print(lab.__str__())        
        self.pausa()

    def registrar(self):
        print(msg('abm.laboratorio.titulo.registrar'))
        obligatorio = True

        codigo = util.leer_cadena(msg('laboratorio.ingrese.codigo'), obligatorio)
        nombre = str(util.leer_cadena(msg('laboratorio.ingrese.nombre'), obligatorio))
        cantidad_maquinas = str(util.leer_cadena(msg('laboratorio.ingrese.cantidad_maquinas'), obligatorio))
        
        laboratorio = Laboratorio(codigo, nombre, cantidad_maquinas)

        try:
            self.get_controlador().crear(laboratorio)
            print(msg("registro.creado"))
        except Exception as e:
            print(e)
        self.pausa()

    def borrar(self):
        print(msg('abm.laboratorio.titulo.borrar'))
        obligatorio = True
        codigo = util.leer_cadena(msg('laboratorio.ingrese.codigo'), obligatorio)
        try:
            laboratorio = self.get_controlador().buscar_codigo(codigo)
            if not laboratorio:
                print(msg('laboratorio.codigo.no.existe'), ":", codigo)
            else:
                self.get_controlador().borrar(laboratorio)
                print(msg('laboratorio.borrado'))
        except Exception as e:
            print(e)
        self.pausa()

    def consultar_laboratorio(self):
        obligatorio = True
        codigo = util.leer_cadena(msg('laboratorio.ingrese.codigo'), obligatorio)
        
        try:
            if not util.es_numerico(codigo):
                raise Exception("La codigo debe ser numerica!")
                
            laboratorio = ControladorLaboratorio().buscar_codigo(codigo)
            return laboratorio
        except Exception as e:
            print(e)

    def ir_menu_principal(self):
        self.set_terminar_ejecucion(True)

    def get_controlador(self):
        return self.__controlador

    def get_menu_dict(self):
        #crear en caso de que aun no se haya creado
        if not self.__menu_dict:
            menu_listar = Menu(msg('abm.laboratorio.listar'), self.listar)
            menu_registrar = Menu(msg('abm.laboratorio.registrar'), self.registrar)
            #menu_borrar = Menu(msg('abm.laboratorio.borrar'), self.borrar)
            menu_principal = Menu(msg('abm.ir.menu.principal'),self.ir_menu_principal)
            menus = {1: menu_listar, 2: menu_registrar, 3: menu_principal}
            self.__menu_dict = menus

        return self.__menu_dict


if __name__ == "__main__":
    ma = ModuloLaboratorio()
    ma.iniciar()            

import sys
sys.path.append("../")  # referencia al directorio base
from model import Modulo, Menu
from modelo import Ficha
from controladores import ControladorFicha
from i18n import msg
import util
from contexto import *
import ZODB
import BTrees.OOBTree
import transaction, persistent
from datetime import datetime, date, time, timedelta
import calendar

class ModuloFicha(Modulo):
    __controlador = ControladorFicha()

    def __init__(self):
        Modulo.__init__(self, msg('abm.ficha.menu.titulo'))
        self.__menu_dict = None

    def listar(self):
        fichas = self.get_controlador().get_lista_objetos()
        print(msg('abm.ficha.titulo.lista'))
        for cont in fichas:
            print(cont.__str__())        
        self.pausa()

    def registrar(self):
        print(msg('abm.ficha.titulo.registrar'))
        obligatorio = True

        codigo = util.leer_cadena(msg('ficha.ingrese.codigo'), obligatorio)
        hora_inicio = str(util.leer_cadena(msg('ficha.ingrese.hora_inicio'), obligatorio))
        hora_fin = str(util.leer_cadena(msg('ficha.ingrese.hora_fin'), obligatorio))
        fecha = str(util.leer_cadena(msg('ficha.ingrese.fecha'), obligatorio))
        
        ficha = Ficha(codigo, hora_inicio, hora_fin, fecha)

        self.get_controlador().crear(ficha)
        try:
            print(msg("registro.creado"))
        except Exception as e:
            print(e)
        self.pausa()

    def borrar(self):
        print(msg('abm.ficha.titulo.borrar'))
        obligatorio = True
        codigo = util.leer_cadena(msg('ficha.ingrese.codigo'), obligatorio)
        try:
            ficha = self.get_controlador().buscar_codigo(codigo)
            if not ficha:
                print(msg('ficha.codigo.no.existe'), ":", codigo)
            else:
                self.get_controlador().borrar(ficha)
                print(msg('ficha.borrado'))
        except Exception as e:
            print(e)
        self.pausa()

    def consultar_ficha(self):
        obligatorio = True
        codigo = util.leer_cadena(msg('ficha.ingrese.codigo'), obligatorio)
        
        try:
            if not util.es_numerico(codigo):
                raise Exception("El codigo debe ser numerico!")
                
            ficha = ControladorFicha().buscar_codigo(codigo)
            return ficha
        except Exception as e:
            print(e)

    def ir_menu_principal(self):
        self.set_terminar_ejecucion(True)

    def get_controlador(self):
        return self.__controlador

    def get_menu_dict(self):
        #crear en caso de que aun no se haya creado
        if not self.__menu_dict:
            menu_listar = Menu(msg('abm.ficha.listar'), self.listar)
            menu_registrar = Menu(msg('abm.ficha.registrar'), self.registrar)
            #menu_borrar = Menu(msg('abm.ficha.borrar'), self.borrar)
            menu_principal = Menu(msg('abm.ir.menu.principal'),self.ir_menu_principal)
            menus = {1: menu_listar, 2: menu_registrar, 3: menu_principal}
            self.__menu_dict = menus

        return self.__menu_dict


if __name__ == "__main__":
    ma = ModuloFicha()
    ma.iniciar()            

import sys
sys.path.append("../")  # referencia al directorio base
from model import Modulo, Menu
from modelos import *
from controladores import *
from i18n import msg
import util
from contexto import *
import ZODB
import BTrees.OOBTree
import transaction, persistent

class Moduloreserva(Modulo):
    __controlador = ControladorFicha()

    def __init__(self):
        Modulo.__init__(self, msg('abm.Reserva.menu.titulo'))
        self.__menu_dict = None

    def listar(self):
        fichas = self.get_controlador().get_lista_objetos()
        print(msg('abm.reserva.titulo.lista'))
        for ficha in fichas:
            print(ficha.__str__())
        self.pausa()

    def registrar(self):
        print(msg('abm.reserva.titulo.registrar'))
        obligatorio = True

        codigo = str(util.leer_cadena(msg('reserva.ingrese.codigo'), obligatorio))
        codigo_libro = str(util.leer_cadena(msg('reserva.ingrese.libro'), obligatorio))
        codigo_alumno = str(util.leer_cadena(msg('reserva.ingrese.alumno'), obligatorio))

        libro = ControladorLibro().buscar_codigo(codigo_libro)
        
        alumno = ControladorAlumno().buscar_codigo(codigo_alumno)
        
        if libro.get_tipo() == 'Consultable':
            raise Exception("No puede prestar temporalmente un libro de Consulta, favor realice un reserva de Consulta!")
        
        if ControladorAlumno().puede_prestar(alumno) == False:
            raise Exception("Alumno no puede prestar mas libros")
            
        if libro.get_estado() == 'Prestado':
            raise Exception("No puede prestar libro, no se encuentra disponible")
            
        ficha = Ficha(codigo, libro, alumno)

        try:
            self.get_controlador().crear(ficha)
            print(msg("registro.creado"))
        except Exception as e:
            print(e)
        return ficha
        self.pausa()

    def borrar(self):
        print(msg('abm.reserva.titulo.borrar'))
        obligatorio = True
        codigo = util.leer_cadena(msg('reserva.ingrese.codigo'), obligatorio)

        try:
            ficha = self.get_controlador().buscar_codigo(codigo)
            self.get_controlador().borrar(ficha)
            print(msg('reserva.borrado'))
        except Exception as e:
            print(e)
        self.pausa()

    def ir_menu_principal(self):
        self.set_terminar_ejecucion(True)

    def get_controlador(self):
        return self.__controlador

    def get_menu_dict(self):
        #crear en caso de que aun no se haya creado
        if not self.__menu_dict:
            menu_listar = Menu(msg('abm.reserva.listar'), self.listar)
            menu_registrar = Menu(msg('abm.reserva.registrar'), self.registrar)
            menu_borrar = Menu(msg('abm.reserva.borrar'), self.borrar)
            menu_principal = Menu(msg('abm.ir.menu.principal'),self.ir_menu_principal)
            menus = {1: menu_listar, 2: menu_registrar, 3: menu_borrar, 4: menu_principal}
            self.__menu_dict = menus

        return self.__menu_dict


if __name__ == "__main__":
    ma = Moduloreserva()
    ma.iniciar()

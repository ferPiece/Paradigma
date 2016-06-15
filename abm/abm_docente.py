import sys
sys.path.append("../")  # referencia al directorio base
from model import Modulo, Menu
from modelo import Docente
from controladores import ControladorDocente
from i18n import msg
import util
from contexto import *
import ZODB
import BTrees.OOBTree
import transaction, persistent

class ModuloDocente(Modulo):
    __controlador = ControladorDocente()

    def __init__(self):
        Modulo.__init__(self, msg('abm.docente.menu.titulo'))
        self.__menu_dict = None

    def listar(self):
        docentes = self.get_controlador().get_lista_objetos()
        print(msg('abm.docente.titulo.lista'))
        for doc in docentes:
            print(doc.__str__())        
        self.pausa()

    def registrar(self):
        print(msg('abm.docente.titulo.registrar'))
        obligatorio = True

        cedula = util.leer_cadena(msg('docente.ingrese.cedula'), obligatorio)
        nombre = str(util.leer_cadena(msg('docente.ingrese.nombre'), obligatorio))
        apellido = str(util.leer_cadena(msg('docente.ingrese.apellido'), obligatorio))
        fecha_nacimiento = str(util.leer_cadena(msg('docente.ingrese.fecha_nacimiento'), obligatorio))
        asignatura = str(util.leer_cadena(msg('docente.ingrese.asignatura'), obligatorio))
        telefono = str(util.leer_cadena(msg('docente.ingrese.telefono'), obligatorio))
        departamento = str(util.leer_cadena(msg('docente.ingrese.departamento'), obligatorio))
        
        docente = Docente(asignatura, departamento, telefono, cedula, nombre, apellido, fecha_nacimiento)

        try:
            self.get_controlador().crear(docente)
            print(msg("registro.creado"))
        except Exception as e:
            print(e)
        self.pausa()

    def borrar(self):
        print(msg('abm.docente.titulo.borrar'))
        obligatorio = True
        cedula = util.leer_cadena(msg('docente.ingrese.cedula'), obligatorio)
        try:
            docente = self.get_controlador().buscar_codigo(cedula)
            if not docente:
                print(msg('docente.cedula.no.existe'), ":", cedula)
            else:
                self.get_controlador().borrar(docente)
                print(msg('docente.borrado'))
        except Exception as e:
            print(e)
        self.pausa()

    def consultar_docente(self):
        obligatorio = True
        cedula = util.leer_cadena(msg('docente.ingrese.cedula'), obligatorio)
        
        try:
            if not util.es_numerico(cedula):
                raise Exception("La cedula debe ser numerica!")
                
            docente = ControladorDocente().buscar_codigo(cedula)
            return docente
        except Exception as e:
            print(e)

    def ir_menu_principal(self):
        self.set_terminar_ejecucion(True)

    def get_controlador(self):
        return self.__controlador

    def get_menu_dict(self):
        #crear en caso de que aun no se haya creado
        if not self.__menu_dict:
            menu_listar = Menu(msg('abm.docente.listar'), self.listar)
            menu_registrar = Menu(msg('abm.docente.registrar'), self.registrar)
            #menu_borrar = Menu(msg('abm.docente.borrar'), self.borrar)
            menu_principal = Menu(msg('abm.ir.menu.principal'),self.ir_menu_principal)
            menus = {1: menu_listar, 2: menu_registrar, 3: menu_principal}
            self.__menu_dict = menus

        return self.__menu_dict


if __name__ == "__main__":
    ma = ModuloDocente()
    ma.iniciar()            

import sys
sys.path.append("../")  # referencia al directorio base
from model import Modulo, Menu
from modelo import Funcionario
from controladores import ControladorFuncionario
from i18n import msg
import util
from contexto import *
import ZODB
import BTrees.OOBTree
import transaction, persistent

class ModuloFuncionario(Modulo):
    __controlador = ControladorFuncionario()

    def __init__(self):
        Modulo.__init__(self, msg('abm.funcionario.menu.titulo'))
        self.__menu_dict = None

    def listar(self):
        funcionarios = self.get_controlador().get_lista_objetos()
        print(msg('abm.funcionario.titulo.lista'))
        for doc in funcionarios:
            print(doc.__str__())        
        self.pausa()

    def registrar(self):
        print(msg('abm.funcionario.titulo.registrar'))
        obligatorio = True

        cedula = util.leer_cadena(msg('funcionario.ingrese.cedula'), obligatorio)
        nombre = str(util.leer_cadena(msg('funcionario.ingrese.nombre'), obligatorio))
        apellido = str(util.leer_cadena(msg('funcionario.ingrese.apellido'), obligatorio))
        fecha_nacimiento = str(util.leer_cadena(msg('funcionario.ingrese.fecha_nacimiento'), obligatorio))
        departamento = str(util.leer_cadena(msg('funcionario.ingrese.departamento'), obligatorio))
        cargo = str(util.leer_cadena(msg('funcionario.ingrese.cargo'), obligatorio))
        telefono = str(util.leer_cadena(msg('funcionario.ingrese.telefono'), obligatorio))
        
        funcionario = Funcionario(cargo, departamento, telefono, cedula, nombre, apellido, fecha_nacimiento)

        try:
            self.get_controlador().crear(funcionario)
            print(msg("registro.creado"))
        except Exception as e:
            print(e)
        self.pausa()

    def borrar(self):
        print(msg('abm.funcionario.titulo.borrar'))
        obligatorio = True
        cedula = util.leer_cadena(msg('funcionario.ingrese.cedula'), obligatorio)
        try:
            funcionario = self.get_controlador().buscar_codigo(cedula)
            if not funcionario:
                print(msg('funcionario.cedula.no.existe'), ":", cedula)
            else:
                self.get_controlador().borrar(funcionario)
                print(msg('funcionario.borrado'))
        except Exception as e:
            print(e)
        self.pausa()

    def consultar_funcionario(self):
        obligatorio = True
        cedula = util.leer_cadena(msg('funcionario.ingrese.cedula'), obligatorio)
        
        try:
            if not util.es_numerico(cedula):
                raise Exception("La cedula debe ser numerica!")
                
            funcionario = ControladorFuncionario().buscar_codigo(cedula)
            return funcionario
        except Exception as e:
            print(e)

    def ir_menu_principal(self):
        self.set_terminar_ejecucion(True)

    def get_controlador(self):
        return self.__controlador

    def get_menu_dict(self):
        #crear en caso de que aun no se haya creado
        if not self.__menu_dict:
            menu_listar = Menu(msg('abm.funcionario.listar'), self.listar)
            menu_registrar = Menu(msg('abm.funcionario.registrar'), self.registrar)
            #menu_borrar = Menu(msg('abm.funcionario.borrar'), self.borrar)
            menu_principal = Menu(msg('abm.ir.menu.principal'),self.ir_menu_principal)
            menus = {1: menu_listar, 2: menu_registrar, 3: menu_principal}
            self.__menu_dict = menus

        return self.__menu_dict


if __name__ == "__main__":
    ma = ModuloFuncionario()
    ma.iniciar()            

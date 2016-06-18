import sys
sys.path.append("../")  # referencia al directorio base
from model import Modulo, Menu
from controladores import *
from abm_docente import ModuloDocente
from abm_funcionario import ModuloFuncionario
from abm_laboratorio import ModuloLaboratorio
from abm_contacto import ModuloContacto
from abm_ficha import ModuloFicha
from i18n import msg
import util
from contexto import *
import ZODB
import BTrees.OOBTree
import transaction, persistent
import getpass

class ModuloApp(Modulo):
    __controlador = ControladorLaboratorio()

    def __init__(self):
        Modulo.__init__(self, msg('abm.app.menu.titulo'))
        self.__menu_dict = None
    
    def login(self):
        '''Metodo que sirve para loguearse desde la terminal ingresando el usuario y la contraseña.'''

        util.limpiar_pantalla()
        band = False
        while band != True:
            codigo = input("USUARIO: ")
            password = getpass.getpass("CONTRASEÑA: ")#para ocultar la contraseña que se esta escribiendo
            if codigo == 'root' and password == 'pass':
                band = True
                return band
            print("ERROR--> USUARIO O PASSWORD!!!!!\n")
            band = False 
                
    def crear(self):
        self.login()
        self.iniciar()
             
    def listar(self):
        #lista los laboratorios existentes
        laboratorios = self.get_controlador().get_lista_objetos()
        print(msg('abm.laboratorio.titulo.lista'))
        for lab in laboratorios:
            print(lab.__str__())
        self.pausa()
        
    def abm_docente(self):
        modulo_docente = ModuloDocente()
        modulo_docente.iniciar()    
        
    def abm_funcionario(self):
        modulo_funcionario = ModuloFuncionario()
        modulo_funcionario.iniciar()   
        
    def abm_contacto(self):
        modulo_contacto = ModuloContacto()
        modulo_contacto.iniciar()       
        
    def abm_ficha(self):
        modulo_ficha = ModuloFicha()
        modulo_ficha.iniciar()         
        
    def abm_laboratorio(self):
        modulo_laboratorio = ModuloLaboratorio()
        modulo_laboratorio.iniciar()   
        
    def abm_reservas(self):
        #modulo_reservas = ModuloReservas()
        #modulo_reservas.iniciar() 
        self.salir() 
        
    def abm_consultas(self):
        #modulo_consultas = ModuloConsultas()
        #modulo_consultas.iniciar() 
        self.salir()              
              
    def salir(self):
        self.set_terminar_ejecucion(True)
    
    def get_controlador(self):
        return self.__controlador

    def get_menu_dict(self):
        #crear en caso de que aun no se haya creado
        if not self.__menu_dict:
            menu_listar = Menu(msg('abm.app.listar'), self.listar)
            menu_docente = Menu(msg('abm.docente'), self.abm_docente)
            menu_funcionario = Menu(msg('abm.funcionario'), self.abm_funcionario)
            menu_contacto = Menu(msg('abm.contacto'), self.abm_contacto)
            menu_ficha = Menu(msg('abm.ficha'), self.abm_ficha)
            menu_laboratorio = Menu(msg('abm.laboratorio'), self.abm_laboratorio)
            menu_reservas = Menu(msg('abm.reservas'), self.abm_reservas)
            menu_consultas = Menu(msg('abm.consultas'), self.abm_consultas)
            menu_salir = Menu(msg('abm.salir'),self.salir)
            menus = {1: menu_listar, 2: menu_docente, 3: menu_funcionario, 4: menu_contacto, 5: menu_ficha, 6: menu_laboratorio, 7: menu_reservas, 8: menu_consultas, 9: menu_salir}
            self.__menu_dict = menus
        return self.__menu_dict
        


if __name__ == "__main__":
    ma = ModuloApp()
    ma.crear()            

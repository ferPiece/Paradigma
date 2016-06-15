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

class ModuloApp(Modulo):
    __controlador = ControladorLaboratorio()

    def __init__(self):
        Modulo.__init__(self, msg('abm.app.menu.titulo'))
        self.__menu_dict = None
        
    def crear(self):
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
    ''' 
    def informacion_biblioteca(self):
        biblioteca = self.get_controlador().get_lista_objetos()[0]
        print(msg('abm.biblioteca.nombre'), biblioteca.get_institucion(), ', version 0.9.0')
        print('Autor: Fernando Lopez')
        self.pausa()
    
    def registrar_alumno(self):
        modulo_alumno = ModuloAlumno()
        modulo_alumno.iniciar()

    def prestamos(self):
        modulo_prestamos = ModuloPrestarLibro()
        modulo_prestamos.iniciar()

    def consultar_libro(self):
        print('Consulta de Libros')
        obligatorio = True
        
        try:
            codigo = util.leer_cadena(msg('libro.ingrese.codigo'), obligatorio)
            libros = self.get_controlador().get_lista_objetos()[0].get_libros()
            libro = self.get_controlador().buscar_por_codigo(codigo, libros)
            if libro:
                print(libro.__str__())

        except Exception as e:
            print(e)
        self.pausa()
        
    def consultar_alumno(self):
        modulo_alumno = ModuloAlumno()
        alumno = modulo_alumno.consultar_alumno()
        if alumno:
            print('Alumno: ', alumno.get_nombre(), alumno.get_apellido())
            print(msg('abm.alumno.libros'))
            for libro in alumno.get_lista_libros():
                print(libro.__str__())

            if alumno.mostrar_la_multa():
                print(msg('abm.alumno.multa'), alumno.mostrar_la_multa())
            else:
                print(msg('abm.alumno.multa'), 'ninguno')

            if alumno.get_fin_de_multa():
                print(msg('abm.alumno.fin.multa'), alumno.get_fin_de_multa())
            else:
                print(msg('abm.alumno.fin.multa'), 'ninguno')
        self.pausa()
        
    def registro(self):
        modulo_registro = ModuloRegistro()
        modulo_registro.iniciar()

    def estadisticas(self):
        modulo_estadistica = ModuloEstadisticas()
        modulo_estadistica.iniciar()
    ''' 
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
            menu_salir = Menu(msg('abm.salir'),self.salir)
            menus = {1: menu_listar, 2: menu_docente, 3: menu_funcionario, 4: menu_contacto, 5: menu_laboratorio, 6: menu_salir}
            self.__menu_dict = menus
        return self.__menu_dict


if __name__ == "__main__":
    ma = ModuloApp()
    ma.crear()            

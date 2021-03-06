import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
from tkinter import messagebox, PhotoImage
from controladores import ControladorUsuario, ControladorLaboratorio
from vistas.reservas import FormsReserva
from vistas.listar_laboratorio import ListarLaboratorio
from vistas.forms_docente import FormsDocente
from vistas.forms_laboratorio import FormsLaboratorio
from vistas.forms_funcionario import FormsFuncionario
from vistas.forms_contacto import FormsContacto
from vistas.informacion import Informacion
from vistas.consultas import FormsConsulta
class VistaLogin(tk.PanedWindow):

    """Vista que es utilizada para loggear el ingreso al sistema"""
    __color_bg = 'pink'
    __error_lbl = None
    __usuario_lbl = None
    __usuario_entry = None 
    __password_lbl = None
    __password_entry = None
    __login_btn = None
    __controlador_usuario = ControladorUsuario()
    __listener = None #función que será ejecutada después de ingresar usuario y contrasenha correctamente
    
    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master, bg = self.__color_bg)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()
 
    def inicializar(self):
        #self.__panel_master.config(bg='skyblue')
        self.__panel_master.geometry('300x150')
        self.__panel_master.title("Inicio de Sesión")
        self.__panel_master.config(bg = self.__color_bg)
        self.get_error_lbl()
        self.get_usuario_lbl()
        self.get_usuario_entry()
        self.get_password_lbl()
        self.get_password_entry()
        self.get_login_btn()

    def get_error_lbl(self):
        '''crear etiqueta para mensaje de error'''
        if not self.__error_lbl:
            self.__error_lbl = tk.Label(master=self, text="", fg="red")
            self.__error_lbl.grid(row=0, column=0, columnspan=2)
        return self.__error_lbl
                   
    def get_usuario_lbl(self):
        '''crear etiqueta usuario'''
        if not self.__usuario_lbl:
            self.__usuario_lbl = tk.Label(master=self, text="Usuario: ", font=('Ubuntu', 11), width=10, bg = self.__color_bg)
            self.__usuario_lbl.grid(row=1, column=0)
        return self.__usuario_lbl
        
    def get_usuario_entry(self):
        '''crear input para usuario'''
        if not self.__usuario_entry:
            self.__usuario_entry = tk.Entry(master=self, width=20)
            self.__usuario_entry.focus()
            self.__usuario_entry.grid(row=1, column=1)
        return self.__usuario_entry
        
    def get_password_lbl(self):
        '''crear etiqueta password'''
        if not self.__password_lbl:
            self.__password_lbl = tk.Label(master=self, text="Password: ", font=('Ubuntu', 11), width=10, bg = self.__color_bg)
            self.__password_lbl.grid(row=2, column=0)
        return self.__password_lbl
        
    def get_password_entry(self):
        if not self.__password_entry:
            self.__password_entry = tk.Entry(master=self, width=20, show="*")
            self.__password_entry.grid(row=2, column=1)
        return self.__password_entry        
        
    def get_login_btn(self):
        if not self.__login_btn:
            self.__login_btn = tk.Button(master=self, text="Login", command=self.verificar_usuario)
            self.__login_btn.grid(row=3, column=1)
        return self.__login_btn      
        
    def verificar_usuario(self):
        codigo_usuario = self.get_usuario_entry().get()
        password = self.get_password_entry().get()
        usuario = self.__controlador_usuario.buscar(codigo_usuario, password)
        
        if usuario:
            self.destroy()
            self.__listener(usuario)
        else:
            self.get_error_lbl().config(text="Usuario o password incorrectos")    
      
    def set_listener(self, listener):
        self.__listener = listener



class PanelPrincipal(tk.Frame):

    """Vista principal que es cargada cuando se verifica correctamente el acceso de los datos de usuario"""

    __vista_actual = None
    __controlador = ControladorLaboratorio()


    def __init__(self,  panel_master):
        tk.Frame.__init__(self,  panel_master)            
        self.__panel_master =  panel_master     
        self.inicializar()
        self.pack()

    def get_controlador(self):
        return self.__controlador

    def inicializar(self):
        #self.__panel_master.config(bg='skyblue')
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("Reserva de Laboratorios")
        menu_bar = tk.Menu(self.__panel_master)
        self.__panel_master.config(menu=menu_bar)

        informacion_menu = tk.Menu(menu_bar)
        informacion_menu.add_command(label="Información", command=self.informacion)
        informacion_menu.add_command(label="Salir", command=self.salir)
        informacion_menu.add_separator()
        
        reservas_menu = tk.Menu(menu_bar)
        reservas_menu.add_command(label="Reservar", command=self.reservar)
        reservas_menu.add_command(label="Consultas", command=self.consultar)
        reservas_menu.add_separator()
        
        listar_laboratorio_menu = tk.Menu(menu_bar)
        listar_laboratorio_menu.add_command(label='Listar Laboratorios',command=self.listar_laboratorio)

        docente_menu = tk.Menu(menu_bar)
        docente_menu.add_command(label='Registrar Docente',command=self.crear_docente)

        laboratorio_menu = tk.Menu(menu_bar)
        laboratorio_menu.add_command(label='Registrar Laboratorio',command=self.crear_laboratorio)
        
        funcionario_menu = tk.Menu(menu_bar)
        funcionario_menu.add_command(label='Registrar Funcionario',command=self.crear_funcionario)
        funcionario_menu.add_command(label='Registrar Contacto',command=self.crear_contacto)
        
        menu_bar.add_cascade(label="Informacion", menu=informacion_menu)
        menu_bar.add_cascade(label="Reservas y Consultas",menu=reservas_menu)
        menu_bar.add_cascade(label='Lista de Laboratorios', menu=listar_laboratorio_menu)
        menu_bar.add_cascade(label='Docentes', menu=docente_menu)
        menu_bar.add_cascade(label='Laboratorios', menu=laboratorio_menu)
        menu_bar.add_cascade(label='Configuracion', menu=funcionario_menu)
    
    

    '''llamo a la vista de reservas la cual pertirira crear reservas para los laboratorios'''
    def reservar(self):
        self.limpiar()
        form = FormsReserva(self.__panel_master)
        self.__vista_actual = form

    def listar_laboratorio(self):
        '''Lista los laboratorios registrados'''
        self.limpiar()
        lista = ListarLaboratorio(self.__panel_master)
        self.__vista_actual = lista
    
    def crear_docente(self):
        '''Permite el registro de docentes'''
        self.limpiar()
        form = FormsDocente(self.__panel_master)
        self.__vista_actual = form
    
    def crear_laboratorio(self):
        '''Permite el registro de laboratorios'''
        self.limpiar()
        form = FormsLaboratorio(self.__panel_master)
        self.__vista_actual = form
        
    def crear_funcionario(self):
        '''Permite el registro de funcionarios'''
        self.limpiar()
        form = FormsFuncionario(self.__panel_master)
        self.__vista_actual = form

    def crear_contacto(self):
        '''Permite el registro de contactos tanto para funcionarios y docentes'''
        self.limpiar()
        form = FormsContacto(self.__panel_master)
        self.__vista_actual = form
    
    def consultar(self):
        self.limpiar()
        form = FormsConsulta(self.__panel_master)
        self.__vista_actual = form

    def informacion(self):
        self.limpiar()
        form = Informacion(self.__panel_master)
        self.__vista_actual = form

    def salir(self):
        self.quit()
        
    def limpiar(self):
        if self.__vista_actual:
            self.__vista_actual.destroy()
                
    def accion(self):
        messagebox.showinfo("Info", "No implementado")



import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
from tkinter import messagebox
from controladores import ControladorUsuario, ControladorLaboratorio

class VistaLogin(tk.PanedWindow):

    """Vista que es utilizada para loggear el ingreso al sistema"""

    __error_lbl = None
    __usuario_lbl = None
    __usuario_entry = None 
    __password_lbl = None
    __password_entry = None
    __login_btn = None
    __controlador_usuario = ControladorUsuario()
    __listener = None #función que será ejecutada después de ingresar usuario y contrasenha correctamente
    
    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()
 
    def inicializar(self):
        self.__panel_master.geometry('300x150')
        self.__panel_master.title("Inicio de Sesión")
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
            self.__usuario_lbl = tk.Label(master=self, text="Usuario: ", font=('Ubuntu', 11), width=10)
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
            self.__password_lbl = tk.Label(master=self, text="Password: ", font=('Ubuntu', 11), width=10)
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
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("Reserva de Laboratorios")
        menu_bar = tk.Menu(self.__panel_master)
        self.__panel_master.config(menu=menu_bar)
        
        informacion_menu = tk.Menu(menu_bar)
        informacion_menu.add_command(label="Información", command=self.accion)
        informacion_menu.add_command(label="Salir", command=self.salir)
        informacion_menu.add_separator()
        
        registro_prestamo_menu = tk.Menu(menu_bar)
        registro_prestamo_menu.add_command(label="Prestamos", command=self.registro_prestamo)
        registro_prestamo_menu.add_command(label="Consultas", command=self.registro_consulta)
        registro_prestamo_menu.add_separator()
        
        menu_bar.add_cascade(label="Informacion", menu=informacion_menu)
        menu_bar.add_cascade(label="Reservas y Consultas",menu=registro_prestamo_menu)
    
    
    def registro_prestamo(self):
        messagebox.showinfo("Info","No implementado")
        
    def registro_consulta(self):
        messagebox.showinfo("Info","No implementado")

    def salir(self):
        self.quit()
        
    def limpiar(self):
        if self.__vista_actual:
            self.__vista_actual.destroy()
                
    def accion(self):
        messagebox.showinfo("Info", "No implementado")





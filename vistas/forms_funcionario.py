import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
from tkinter import messagebox
from controladores import ControladorFuncionario
from modelo import Funcionario

class FormsFuncionario(tk.PanedWindow):
    '''Clase que permite realizar el formulario para introducir un Funcionario desde el 
    teclado'''
    __cedula_etiqueta = None
    __cedula_entry = None
    __nombre_etiqueta = None
    __nombre_entry = None
    __apellido_etiqueta = None
    __apellido_entry = None
    __fecha_nacimiento_etiqueta = None
    __fecha_nacimiento_entry = None
    __cargo_etiqueta = None
    __cargo_entry = None
    __departamento_etiqueta = None
    __departamento_entry = None
    __telefono_etiqueta = None
    __telefono_entry = None
    __guardar_boton = None
    __controlador = ControladorFuncionario()

    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("ABM Funcionarios")
        self.get_cedula_etiqueta() 
        self.get_cedula_entry()   
        self.get_nombre_etiqueta()
        self.get_nombre_entry()
        self.get_apellido_etiqueta()
        self.get_apellido_entry()
        self.get_fecha_nacimiento_etiqueta()
        self.get_fecha_nacimiento_entry()
        self.get_cargo_etiqueta()
        self.get_cargo_entry()
        self.get_departamento_etiqueta()
        self.get_departamento_entry()
        self.get_telefono_etiqueta()
        self.get_telefono_entry()
        self.get_guardar_boton()

    def get_controlador(self):
        return self.__controlador

    def get_cedula_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__cedula_etiqueta:
            self.__cedula_etiqueta = tk.Label(master=self, text="Cedula: ", width=20)
            self.__cedula_etiqueta.grid(row=1, column=0)
        return self.__cedula_etiqueta

    def get_cedula_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__cedula_entry:
            self.__cedula_entry = tk.Entry(master=self, width=20)
            self.__cedula_entry.focus()
            self.__cedula_entry.grid(row=1, column=1)
        return self.__cedula_entry

    def get_nombre_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__nombre_etiqueta:
            self.__nombre_etiqueta = tk.Label(master=self, text="Nombre: ", width=20)
            self.__nombre_etiqueta.grid(row=2, column=0)
        return self.__nombre_etiqueta
        
    def get_nombre_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__nombre_entry:
            self.__nombre_entry = tk.Entry(master=self, width=20)
            self.__nombre_entry.grid(row=2, column=1)
        return self.__nombre_entry

    def get_apellido_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__apellido_etiqueta:
            self.__apellido_etiqueta = tk.Label(master=self, text="Apellido: ", width=20)
            self.__apellido_etiqueta.grid(row=3, column=0)
        return self.__apellido_etiqueta

    def get_apellido_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__apellido_entry:
            self.__apellido_entry = tk.Entry(master=self, width=20)
            self.__apellido_entry.grid(row=3, column=1)
        return self.__apellido_entry

    def get_fecha_nacimiento_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__fecha_nacimiento_etiqueta:
            self.__fecha_nacimiento_etiqueta = tk.Label(master=self, text="Fecha Nacimiento: ", width=20)
            self.__fecha_nacimiento_etiqueta.grid(row=4, column=0)
        return self.__fecha_nacimiento_etiqueta

    def get_fecha_nacimiento_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__fecha_nacimiento_entry:
            self.__fecha_nacimiento_entry = tk.Entry(master=self, width=20)
            self.__fecha_nacimiento_entry.grid(row=4, column=1)
        return self.__fecha_nacimiento_entry

    def get_cargo_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__cargo_etiqueta:
            self.__cargo_etiqueta = tk.Label(master=self, text="cargo: ", width=20)
            self.__cargo_etiqueta.grid(row=5, column=0)
        return self.__cargo_etiqueta

    def get_cargo_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__cargo_entry:
            self.__cargo_entry = tk.Entry(master=self, width=20)
            self.__cargo_entry.grid(row=5, column=1)
        return self.__cargo_entry

    def get_departamento_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__departamento_etiqueta:
            self.__departamento_etiqueta = tk.Label(master=self, text="DEpartamento: ", width=20)
            self.__departamento_etiqueta.grid(row=6, column=0)
        return self.__departamento_etiqueta

    def get_departamento_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__departamento_entry:
            self.__departamento_entry = tk.Entry(master=self, width=20)
            self.__departamento_entry.grid(row=6, column=1)
        return self.__departamento_entry

    def get_telefono_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__telefono_etiqueta:
            self.__telefono_etiqueta = tk.Label(master=self, text="Telefono: ", width=20)
            self.__telefono_etiqueta.grid(row=7, column=0)
        return self.__telefono_etiqueta

    def get_telefono_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__telefono_entry:
            self.__telefono_entry = tk.Entry(master=self, width=20)
            self.__telefono_entry.grid(row=7, column=1)
        return self.__telefono_entry

    def get_guardar_boton(self):
        if not self.__guardar_boton:
            self.__guardar_boton = tk.Button(master=self, text="Guardar", command=self.guardar_funcionario)
            self.__guardar_boton.grid(row=8, column=1)
        return self.__guardar_boton

    def guardar_funcionario(self):
        cedula = self.get_cedula_entry().get()
        nombre = self.get_nombre_entry().get()
        apellido = self.get_apellido_entry().get()
        fecha_nacimiento = self.get_fecha_nacimiento_entry().get()
        cargo = self.get_cargo_entry().get()
        departamento = self.get_departamento_entry().get()
        telefono = self.get_telefono_entry().get()
        
        try:
            #creo el objeto del tipo funcionario
            funcionario = Funcionario(cargo, departamento, telefono, cedula, nombre, apellido, fecha_nacimiento)
            #lo creo por medio del controlador
            self.get_controlador().crear(funcionario)
            messagebox.showinfo("Registro funcionario","Se creo el funcionario con exito")
        except Exception as e:
            messagebox.showinfo("Error", e)



if __name__ == '__main__':
    root = tk.Tk()
    forms_funcionario = FormsFuncionario(root)
    root.mainloop()     

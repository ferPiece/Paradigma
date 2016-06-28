import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
from tkinter import messagebox
from controladores import ControladorLaboratorio
from modelo import Laboratorio

class FormsLaboratorio(tk.PanedWindow):
    '''Clase que permite realizar el formulario para introducir un laboratorio desde el 
    teclado'''
    __codigo_etiqueta = None
    __codigo_entry = None
    __nombre_etiqueta = None
    __nombre_entry = None
    __cantidad_maquinas_etiqueta = None
    __cantidad_maquinas_entry = None
    __guardar_boton = None
    __controlador = ControladorLaboratorio()

    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("ABM Laboratorios")
        self.get_codigo_etiqueta() 
        self.get_codigo_entry()   
        self.get_nombre_etiqueta()
        self.get_nombre_entry()
        self.get_cantidad_maquinas_etiqueta()
        self.get_cantidad_maquinas_entry()
        self.get_guardar_boton()

    def get_controlador(self):
        return self.__controlador

    def get_codigo_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__codigo_etiqueta:
            self.__codigo_etiqueta = tk.Label(master=self, text="Codigo: ", width=20)
            self.__codigo_etiqueta.grid(row=1, column=0)
        return self.__codigo_etiqueta

    def get_codigo_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__codigo_entry:
            self.__codigo_entry = tk.Entry(master=self, width=20)
            self.__codigo_entry.focus()
            self.__codigo_entry.grid(row=1, column=1)
        return self.__codigo_entry

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

    def get_cantidad_maquinas_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__cantidad_maquinas_etiqueta:
            self.__cantidad_maquinas_etiqueta = tk.Label(master=self, text="Cantidad de Maquinas: ", width=20)
            self.__cantidad_maquinas_etiqueta.grid(row=3, column=0)
        return self.__cantidad_maquinas_etiqueta

    def get_cantidad_maquinas_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__cantidad_maquinas_entry:
            self.__cantidad_maquinas_entry = tk.Entry(master=self, width=20)
            self.__cantidad_maquinas_entry.grid(row=3, column=1)
        return self.__cantidad_maquinas_entry

    def get_guardar_boton(self):
        if not self.__guardar_boton:
            self.__guardar_boton = tk.Button(master=self, text="Guardar", command=self.guardar_laboratorio)
            self.__guardar_boton.grid(row=8, column=1)
        return self.__guardar_boton

    def guardar_laboratorio(self):
        codigo = self.get_codigo_entry().get()
        nombre = self.get_nombre_entry().get()
        cantidad_maquinas = self.get_cantidad_maquinas_entry().get()
     
        try:
            #creo el objeto del tipo docente
            laboratorio = Laboratorio(codigo, nombre, cantidad_maquinas)
            #lo creo por medio del controlador
            self.get_controlador().crear(laboratorio)
            messagebox.showinfo("Registro Laboratorio","Se creo el Laboratorio con exito")
        except Exception as e:
            messagebox.showinfo("Error", e)



if __name__ == '__main__':
    root = tk.Tk()
    forms_laboratorio = FormsLaboratorio(root)
    root.mainloop()     

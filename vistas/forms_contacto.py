import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
from tkinter import messagebox
from controladores import ControladorContacto
from modelo import Contacto

class FormsContacto(tk.PanedWindow):
    '''Clase que permite realizar el formulario para introducir un Contacto desde el 
    teclado'''
    __correo_etiqueta = None
    __correo_entry = None
    __telefono_etiqueta = None
    __telefono_entry = None
    __guardar_boton = None
    __controlador = ControladorContacto()

    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("ABM Contactos")
        self.get_correo_etiqueta() 
        self.get_correo_entry()   
        self.get_telefono_etiqueta()
        self.get_telefono_entry()
        self.get_guardar_boton()

    def get_controlador(self):
        return self.__controlador

    def get_correo_etiqueta(self):
        '''creo la etiqueta para la vista'''
        if not self.__correo_etiqueta:
            self.__correo_etiqueta = tk.Label(master=self, text="Correo: ", width=20)
            self.__correo_etiqueta.grid(row=1, column=0)
        return self.__correo_etiqueta

    def get_correo_entry(self):
        '''creo la caja de texto para cargar datos'''
        if not self.__correo_entry:
            self.__correo_entry = tk.Entry(master=self, width=20)
            self.__correo_entry.focus()
            self.__correo_entry.grid(row=1, column=1)
        return self.__correo_entry

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
            self.__guardar_boton = tk.Button(master=self, text="Guardar", command=self.guardar_contacto)
            self.__guardar_boton.grid(row=8, column=1)
        return self.__guardar_boton

    def guardar_contacto(self):
        correo = self.get_correo_entry().get()
        telefono = self.get_telefono_entry().get()
        
        try:
            #creo el objeto del tipo contacto
            contacto = Contacto(telefono,correo)
            #lo creo por medio del controlador
            self.get_controlador().crear(contacto)
            messagebox.showinfo("Registro contacto","Se creo el contacto con exito")
        except Exception as e:
            messagebox.showinfo("Error", e)



if __name__ == '__main__':
    root = tk.Tk()
    forms_contacto = FormsContacto(root)
    root.mainloop()     

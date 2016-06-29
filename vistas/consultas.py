import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, StringVar
from modelo import Ficha, Laboratorio
from controladores import ControladorLaboratorio, ControladorDocente, ControladorFicha


class FormsConsulta(tk.PanedWindow):
    __laboratorio_lbl = None
    __laboratorio_cbx = None
    __laboratorio_dicc = None
    __consultar_btn = None
    __title_lbl = None
    __ficha_lbl = None

    '''defino los controladores necesarios a ser utilizados'''
    __controlador_ficha = ControladorFicha()
    __controlador_laboratorio = ControladorLaboratorio()

    
    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("ABM Consultas")
        self.get_laboratorio_lbl()
        self.get_laboratorio_cbx()
        self.get_consultar_btn()
        
        
    def get_laboratorio_lbl(self):
        '''etiqueta para desplegar los nombres de laboratorios'''
        if not self.__laboratorio_lbl:
            self.__laboratorio_lbl = tk.Label(master=self, text="LABORATORIO", width=20)
            self.__laboratorio_lbl.grid(row=2, column=0)
        return self.__laboratorio_lbl

    def get_laboratorio_cbx(self):
        '''Combobox que recupera los objetos del tipo laboratorio para poder mostrar sus nombres'''
        if not self.__laboratorio_cbx:
            self.__box_value = StringVar()
            self.__laboratorio_cbx = ttk.Combobox(master=self,textvariable=self.__box_value, width=20, state='readonly')
            
            #obtener la lista de laboratorios actual
            laboratorios = self.__controlador_laboratorio.get_lista_objetos()
            lista = []
            self.__laboratorio_dicc = {}
            for lab in laboratorios:
                lista.append(lab.get_nombre())
                self.__laboratorio_dicc[lab.get_nombre()] = lab
                self.__laboratorio_cbx["value"] = lista
            self.__laboratorio_cbx.focus()
            self.__laboratorio_cbx.grid(row=2, column=1)
        return self.__laboratorio_cbx

    def get_consultar_btn(self):
        '''Boton utilizado para la creacion de un consulta'''
        if not self.__consultar_btn:
            self.__consultar_btn = tk.Button(master=self, text="Consultar", bg='orange3', font=('Ubuntu', 11), command=self.consultar)
            self.__consultar_btn.grid(row=3, column=1)
        return self.__consultar_btn

    '''Consultar laboratorio, consiste en que un docente debe poder seleccionar un laboratorio y poder realizar
    dicha consulta de la siguiente manera'''
    def consultar(self):
        #recupero los datos ingresados por el usuario, de manera a poder consultar la ficha
        nombre_lab = self.get_laboratorio_cbx().get()
        laboratorio = self.__laboratorio_dicc[nombre_lab]
        fichas = laboratorio.consultar()
        '''Si hay reservas en el laboratorio, listara las fichas de reservas'''
        if nombre_lab == None:
            messagebox.showinfo("Info", "Debe seleccionar ese laboratorio")

        if fichas:
                self.get_title_lbl()
                if not self.__ficha_lbl:
                    fila = 5
                    for ficha in fichas:
                        self.__title_lbl = tk.Label(master=self, text=ficha.__str__())
                        self.__title_lbl.grid(row=fila, column=1)
                        fila = fila + 1
        else:
                messagebox.showinfo("Info", "No hay reservas para ese laboratorio")

    def get_title_lbl(self):
        '''crea la etiqueta para el titulo'''
        if not self.__title_lbl:
            self.__title_lbl = tk.Label(master=self, text="Lista de Fichas", font=('Ubuntu', 11),width=20)
            self.__title_lbl.grid(row=4,column=1)
        return self.__title_lbl


    '''funcion utilizada para partes del programa que no estan en desarrollo'''
    def accion(self):
        messagebox.showinfo("Info", "No implementado")

if __name__ == '__main__':
    root = tk.Tk()
    forms = FormsConsulta(root)
    root.mainloop()

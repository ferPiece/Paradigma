import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from modelo import Ficha, Docente, Laboratorio
from controladores import ControladorLaboratorio, ControladorDocente, ControladorFicha

class FormsReserva(tk.PanedWindow):
    __laboratorio_lbl = None
    __laboratorio_cbx = None
    __cedula_docente_lbl = None
    __cedula_docente_entry = None
    __crear_btn = None
    __fecha_lbl = None
    __fecha_entry = None
    __hora_inicio_lbl = None
    __hora_inicio_entry = None
    __hora_fin_lbl = None
    __hora_fin_entry = None
    __controlador_laboratorio = ControladorLaboratorio()

    
    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry('600x400')
        self.__panel_master.title("ABM Reservas")
        self.get_laboratorio_lbl()
        self.get_laboratorio_cbx()
        self.get_cedula_docente_lbl()
        self.get_cedula_docente_entry()
        self.get_fecha_lbl()
        self.get_fecha_entry()
        self.get_hora_inicio_lbl()
        self.get_hora_inicio_entry()
        self.get_hora_fin_lbl()
        self.get_hora_fin_entry()
        self.get_crear_btn()
        
    def get_laboratorio_lbl(self):
        '''etiqueta para desplegar los nombres de laboratorios'''
        if not self.__laboratorio_lbl:
            self.__laboratorio_lbl = tk.Label(master=self, text="LABORATORIO", width=20)
            self.__laboratorio_lbl.grid(row=2, column=0)
        return self.__laboratorio_lbl

    def get_laboratorio_cbx(self):
        if not self.__laboratorio_cbx:
            self.__laboratorio_cbx = ttk.Combobox(master=self, values = ['Sistemas Operativos', 'Algoritmos', 'HPC', 'Base de Datos', 'Modelado y Simulacion', 'Redes de Computadoras'], width=20)
            self.__laboratorio_cbx.grid(row=2, column=1)
        return self.__laboratorio_cbx

    #def get_lista_laboratorios(self):
        #laboratorios = self.get_controlador().get_lista_objetos()
        #print(msg('abm.laboratorio.titulo.lista'))
        #for lab in laboratorios:
           # print(lab.__str__())        
        #self.pausa()
        #return laboratorios

    def get_cedula_docente_lbl(self):
        '''etiqueta para la cedula del docente'''
        if not self.__cedula_docente_lbl:
            self.__cedula_docente_lbl = tk.Label(master=self, text="CEDULA_DOCENTE: ", width=20)
            self.__cedula_docente_lbl.grid(row=3, column=0)
        return self.__cedula_docente_lbl

    def get_cedula_docente_entry(self):
        '''guarda la cedula del docente'''
        if not self.__cedula_docente_entry:
            self.__cedula_docente_entry = tk.Entry(master=self, width=20)
            self.__cedula_docente_entry.focus()
            self.__cedula_docente_entry.grid(row=3, column=1)
        return self.__cedula_docente_entry

    def get_fecha_lbl(self):
        '''etiqueta para la fecha a reservar'''
        if not self.__fecha_lbl:
            self.__fecha_lbl = tk.Label(master=self, text="FECHA ", width=20)
            self.__fecha_lbl.grid(row=4, column=0)
        return self.__fecha_lbl

    def get_fecha_entry(self):
        '''guarda la fecha reservada por el docente'''
        if not self.__fecha_entry:
            self.__fecha_entry = tk.Entry(master=self, width=20)
            self.__fecha_entry.focus()
            self.__fecha_entry.grid(row=4, column=1)
        return self.__fecha_entry

    def get_hora_inicio_lbl(self):
        '''etiqueta para la hora de inicio'''
        if not self.__hora_inicio_lbl:
            self.__hora_inicio_lbl = tk.Label(master=self, text="HORA_INICIO ", width=20)
            self.__hora_inicio_lbl.grid(row=5, column=0)
        return self.__hora_inicio_lbl

    def get_hora_inicio_entry(self):
        '''guarda la hora inicio reservada'''
        if not self.__hora_inicio_entry:
            self.__hora_inicio_entry = tk.Entry(master=self, width=20)
            self.__hora_inicio_entry.focus()
            self.__hora_inicio_entry.grid(row=5, column=1)
        return self.__hora_inicio_entry    

    def get_hora_fin_lbl(self):
        '''etiqueta para la hora de fin'''
        if not self.__hora_fin_lbl:
            self.__hora_fin_lbl = tk.Label(master=self, text="HORA_FIN ", width=20)
            self.__hora_fin_lbl.grid(row=6, column=0)
        return self.__hora_fin_lbl

    def get_hora_fin_entry(self):
        '''guarda la hora fin reservada'''
        if not self.__hora_fin_entry:
            self.__hora_fin_entry = tk.Entry(master=self, width=20)
            self.__hora_fin_entry.focus()
            self.__hora_fin_entry.grid(row=6, column=1)
        return self.__hora_fin_entry  

    def get_crear_btn(self):
        if not self.__crear_btn:
            self.__crear_btn = tk.Button(master=self, text="CREAR", bg='orange3', command=self.accion)
            self.__crear_btn.grid(row=7, column=1)
        return self.__crear_btn    

    def accion(self):
        messagebox.showinfo("Info", "No implementado")

if __name__ == '__main__':
    root = tk.Tk()
    forms = FormsReserva(root)
    root.mainloop()
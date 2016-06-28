import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox, StringVar
from modelo import Ficha, Docente, Laboratorio
from controladores import ControladorLaboratorio, ControladorDocente, ControladorFicha


class FormsReserva(tk.PanedWindow):
    __laboratorio_lbl = None
    __laboratorio_cbx = None
    __codigo_lbl = None
    __codigo_entry = None
    __cedula_docente_lbl = None
    __cedula_docente_entry = None
    __nombre_docente_entry = None
    __crear_btn = None
    __fecha_lbl = None
    __fecha_entry = None
    __hora_inicio_lbl = None
    __hora_inicio_entry = None
    __hora_fin_lbl = None
    __hora_fin_entry = None
    __asignatura_cbx = None

    '''defino los controladores necesarios a ser utilizados'''
    __controlador_ficha = ControladorFicha()
    __controlador_laboratorio = ControladorLaboratorio()
    __controlador_docente = ControladorDocente()

    
    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("ABM Reservas")
        self.get_laboratorio_lbl()
        self.get_laboratorio_cbx()
        self.get_codigo_lbl()
        self.get_codigo_entry()
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
            self.__box_value = StringVar()
            self.__laboratorio_cbx = ttk.Combobox(master=self,textvariable=self.__box_value, width=20, state='readonly')
            
            #obtener la lista de laboratorios actual
            laboratorios = self.__controlador_laboratorio.get_lista_objetos()
            lista = []

            for lab in laboratorios:
                lista.append(lab.get_nombre())
                self.__laboratorio_cbx["value"] = lista

            self.__laboratorio_cbx.focus()
            self.__laboratorio_cbx.grid(row=2, column=1)
        return self.__laboratorio_cbx

    def get_codigo_lbl(self):
        '''etiqueta para el codigo de una ficha'''
        if not self.__codigo_lbl:
            self.__codigo_lbl = tk.Label(master=self, text="Codigo: ", width=20)
            self.__codigo_lbl.grid(row=3, column=0)
        return self.__codigo_lbl

    def get_codigo_entry(self):
        '''campo que muestra en codigo de la ficha que sera autogenerado'''
        if not self.__codigo_entry:
            self.__codigo_entry = tk.Entry(master=self, width=20)
            #self.__codigo_entry.focus()
            self.__codigo_entry.grid(row=3, column=1)
            codigo = self.__controlador_ficha.ultimo_codigo()
            self.__codigo_entry.insert(0,codigo)
        return self.__codigo_entry

    def get_cedula_docente_lbl(self):
        '''etiqueta para la cedula del docente'''
        if not self.__cedula_docente_lbl:
            self.__cedula_docente_lbl = tk.Label(master=self, text="CEDULA_DOCENTE: ", width=20)
            self.__cedula_docente_lbl.grid(row=4, column=0)
        return self.__cedula_docente_lbl

    def get_cedula_docente_entry(self):
        '''guarda la cedula del docente'''
        if not self.__cedula_docente_entry:
            self.__cedula_docente_entry = tk.Entry(master=self, width=20)
            self.__cedula_docente_entry.focus()
            self.__cedula_docente_entry.grid(row=4, column=1)
        return self.__cedula_docente_entry

    def get_nombre_docente_entry(self):
        '''guarda la nombre del docente'''
        if not self.__nombre_docente_entry:
            self.__nombre_docente_entry = tk.Entry(master=self, width=20)
            #self.__nombre_docente_entry.focus()
            self.__nombre_docente_entry.grid(row=4, column=2)

            #recupero el codigo del docente
            cedula = self.get_cedula_docente_entry().get()
            #busco al docente en la base de datos
            docente = ControladorDocente().buscar_codigo(cedula)
            #inserto en nombre del docente al campo de entrada
            self.__nombre_docente_entry.insert(0,docente.get_nombre())
        return self.__nombre_docente_entry


    def get_asignatura_cbx(self):
        if not self.__asignatura_cbx:
            self.__box_value = StringVar()
            self.__asignatura_cbx = ttk.Combobox(master=self,textvariable=self.__box_value, width=20, state='readonly')
            
            #obtener la lista de asignatura actual
            docente = self.__controlador_docente.get_lista_objetos()
            lista = []

            for doc in docente:
                lista.append(doc.get_asignatura())
                self.__asignatura_cbx["value"] = lista

            self.__asignatura_cbx.focus()
            self.__asignatura_cbx.grid(row=4, column=3)
        return self.__asignatura_cbx   



    def get_fecha_lbl(self):
        '''etiqueta para la fecha a reservar'''
        if not self.__fecha_lbl:
            self.__fecha_lbl = tk.Label(master=self, text="FECHA ", width=20)
            self.__fecha_lbl.grid(row=5, column=0)
        return self.__fecha_lbl

    def get_fecha_entry(self):
        '''guarda la fecha reservada por el docente'''
        if not self.__fecha_entry:
            self.__fecha_entry = tk.Entry(master=self, width=20)
            self.__fecha_entry.focus()
            self.__fecha_entry.grid(row=5, column=1)
        return self.__fecha_entry

    def get_hora_inicio_lbl(self):
        '''etiqueta para la hora de inicio'''
        if not self.__hora_inicio_lbl:
            self.__hora_inicio_lbl = tk.Label(master=self, text="HORA_INICIO ", width=20)
            self.__hora_inicio_lbl.grid(row=6, column=0)
        return self.__hora_inicio_lbl

    def get_hora_inicio_entry(self):
        '''guarda la hora inicio reservada'''
        if not self.__hora_inicio_entry:
            self.__hora_inicio_entry = tk.Entry(master=self, width=20)
            self.__hora_inicio_entry.focus()
            self.__hora_inicio_entry.grid(row=6, column=1)
        return self.__hora_inicio_entry    

    def get_hora_fin_lbl(self):
        '''etiqueta para la hora de fin'''
        if not self.__hora_fin_lbl:
            self.__hora_fin_lbl = tk.Label(master=self, text="HORA_FIN ", width=20)
            self.__hora_fin_lbl.grid(row=7, column=0)
        return self.__hora_fin_lbl

    def get_hora_fin_entry(self):
        '''guarda la hora fin reservada'''
        if not self.__hora_fin_entry:
            self.__hora_fin_entry = tk.Entry(master=self, width=20)
            self.__hora_fin_entry.focus()
            self.__hora_fin_entry.grid(row=7, column=1)
        return self.__hora_fin_entry  

    def get_crear_btn(self):
        if not self.__crear_btn:
            self.__crear_btn = tk.Button(master=self, text="CREAR", bg='orange3', command=self.crear_reserva)
            self.__crear_btn.grid(row=8, column=1)
        return self.__crear_btn


    '''Reservar laboratorio, consiste en que un docente debe poder seleccionar un laboratorio y poder realizar
    dicha reserva de la siguiente manera'''
    def crear_reserva(self):
        #recupero los datos ingresados por el usuario, de manera a poder crear la ficha
        laboratorio = self.get_laboratorio_cbx().get()
        codigo = self.get_codigo_entry().get()
        cedula = self.get_cedula_docente_entry().get()
        fecha = self.get_fecha_entry().get()
        hora_inicio = self.get_hora_inicio_entry().get()
        hora_fin = self.get_hora_fin_entry().get()

        
        try:
            #busco al docente en la base de datos
            docente = ControladorDocente().buscar_codigo(cedula)
            self.get_nombre_docente_entry()
            self.get_asignatura_cbx()



            #creo la ficha para la reserva



        except Exception as e:
            messagebox.showinfo("Opaa", e)
        
        '''
        #instancio un objeto del tipo ficha de manera a poder crearlo en la base de datos
        codigo = get_id()
        ficha = Ficha(codigo, )


        try:
            ControladorFicha().crear(ficha)
            return ficha
        except Exception as e:
            messagebox.showinfo("Info", e)
        '''

    '''funcion utilizada para partes del programa que no estan en desarrollo'''
    def accion(self):
        messagebox.showinfo("Info", "No implementado")

if __name__ == '__main__':
    root = tk.Tk()
    forms = FormsReserva(root)
    root.mainloop()
import sys
sys.path.append("../")  # referencia al directorio base
import tkinter as tk
from tkinter import messagebox
from controladores import ControladorLaboratorio

class ListarLaboratorio(tk.PanedWindow):
    __lista_lbl = None
    __laboratorio_lbl = None
    __controlador = ControladorLaboratorio()

    def __init__(self, panel_master):
        tk.PanedWindow.__init__(self, master=panel_master)
        self.__panel_master = panel_master
        self.inicializar()
        self.pack()

    def inicializar(self):
        self.__panel_master.geometry('800x600')
        self.__panel_master.title("Laboratorios")
        self.get_lista_lbl()
        self.get_listar()

    def get_controlador(self):
        return self.__controlador

    def get_lista_lbl(self):
        if not self.__lista_lbl:
            self.__lista_lbl = tk.Label(master=self, text="Lista de Laboratorios", font=('Ubuntu', 16), width=20)
            self.__lista_lbl.grid(row=1, column=0)
        return self.__lista_lbl

    def get_listar(self):
        if not self.__laboratorio_lbl:
            i = 2
            laboratorios = self.get_controlador().get_lista_objetos()
            for lab in laboratorios:
                self.__laboratorio_lbl = tk.Label(master=self, text=lab.__str__())
                self.__laboratorio_lbl.grid(row=i, column=0)
                i = i + 1
        else:
            messagebox.showinfo("Info", "no hay disponibles")


if __name__ == '__main__':
    root = tk.Tk()
    lista = ListarLaboratorio(root)
    root.mainloop()
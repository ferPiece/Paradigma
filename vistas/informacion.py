import tkinter as tk


class Informacion(tk.PanedWindow):
	'''Clase que muestra el panel que devuelve informacion sobre la empresa'''
	__controlador_empresa = None
	__generico_titulo_lbl = None
	__generico_lbl = None
	__fila = 1
	__columna = 0

	def __init__(self, panel_master):
		tk.PanedWindow.__init__(self, master=panel_master, bg = 'pink')
		self.__panel_master = panel_master
		self.inicializar()
		self.pack()


	def inicializar(self):
		self.__panel_master.geometry('800x600')
		self.__panel_master.title('Reserva de Laboratorios')
		self.__panel_master.resizable(0,0)
		self.__panel_master.config(bg = 'pink')
		
		self.get_generico_titulo_lbl('Proyecto de Paradigmas')
		self.get_generico_lbl('Reservas de Laboratorios')
		self.get_generico_titulo_lbl('Estudiante')
		self.get_generico_lbl('Cynthia Morel')

	def get_generico_titulo_lbl(self, text):
		self.__generico_titulo_lbl = tk.Label(master = self, text = text, width = 30, bg = 'pink', font = ('Arial', 12, 'bold'))
		self.__generico_titulo_lbl.grid(row = self.__fila, column = self.__columna)
		return self.__generico_titulo_lbl

	def get_generico_lbl(self, text):
		self.__generico_lbl = tk.Label(master = self, text = text, width = 20, font = ('Arial', 12))
		self.__generico_lbl.grid(row = self.__fila, column = 1, pady = 10)
		self.__fila += 1
		return self.__generico_lbl
	

		

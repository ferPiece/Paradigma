import tkinter as tk
from vistas.vista import VistaLogin, PanelPrincipal
        

root = tk.Tk()
        
def login_listener(usuario):
    #print("Login ok!: ", usuario.get_nombre(), usuario.get_apellido())
    #se cierra ventana login y se muestra panel principal
    panel_principal = PanelPrincipal(root)
           
login = VistaLogin(root)
login.set_listener(login_listener)
root.mainloop()  

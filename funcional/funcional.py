#Programacion Funcional
import sys
sys.path.append("../")  # referencia al directorio base
from controladores import ControladorDocente, ControladorLaboratorio, ControladorFicha

def buscar_por_cedula(cedula):
	'''funcion que buscar a un docente por cedula'''
	return [docente for docente in ControladorDocente().buscar_codigo(cedula) if cedula == docente.get_cedula()]

def listar_reservas(laboratorio):
    '''funcion que lista las reservas de un solo laboratorio'''
    return laboratorio.consultar()


if __name__ == "__main__":
    #retorna una lista de laboratorios
    laboratorios = ControladorLaboratorio().get_lista_objetos()
    #recorremos los laboratorios
    for laboratorio in laboratorios:
        #preguntamos las reservas por laboratorio
        for reserva in listar_reservas(laboratorio):
            print(reserva.__str__())


    try:
        cedula = 1
        print(buscar_por_cedula(cedula))        
    except Exception as e:
        print (e)
        

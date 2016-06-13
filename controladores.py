import time
import ZODB
import BTrees.OOBTree
import persistent, transaction
from abc import ABCMeta, abstractmethod
from contexto import get_zodb_root
from modelo import Docente,Funcionario,Laboratorio
from datetime import datetime

#from model import Usuario

#####################################################################################################
class ControladorAncestro(metaclass=ABCMeta):
    """Controlador Ancestro el cual implementa las funciones basicas para manejar objetos,
    validando los si cumplen con las especificaciones dadas"""
    __diccionario_objetos = None

    def crear(self, objeto):
        if not objeto:
             raise Exception('OBJETO_NULO_NO_PERMITIDO')        
        self.validar_objeto(objeto) 
        self.validar_insercion_registro(objeto)
        self.get_diccionario_objetos()[self.get_id_objeto(objeto)] = objeto
        transaction.commit()

    def borrar(self, objeto):
        if not objeto:
           raise Exception("No se permite borrar objeto nulo!")
           
        self.validar_eliminacion_registro(objeto)
        #borramos objeto por su id        
        del self.get_diccionario_objetos()[self.get_id_objeto(objeto)]
        transaction.commit()

    def actualizar(self, objeto):
    	self.validar_actualizacion_registro(objeto)
    	self.get_diccionario_objetos()[self.get_id_objeto(objeto)] = objeto
    	transaction.commit()

    def get_lista_objetos(self):
        return  self.get_diccionario_objetos().values()

    @abstractmethod
    def get_diccionario_objetos(self):
        pass

    @abstractmethod
    def get_id_objeto(self, objeto):
        pass

    def validar_objeto(self, objeto):
        pass

    def validar_insercion_registro(self, objeto):
        pass

    def validar_actualizacion_registro(self, objeto):
        pass

    def validar_eliminacion_registro(self, objeto):
        pass

    def buscar_codigo(self, codigo):
    	pass

######################################################################################################
class ControladorDocente(ControladorAncestro):
    """Permite la creacion, eliminacion, actualiazacion, de un docente
    asi tambien como poder buscar un docente por cedula en la base de datos del ZODB
    tambien valida si es que un docente es capaz de prestar laboratorios de acuerdo a las
    especificaciones dadas en la logica del negocio"""

    __docente = None
    
    def get_diccionario_objetos(self):
        #si no existe el diccionario de docentes, creo uno en el root
        if not self.__docente:
            if not hasattr (get_zodb_root(), 'docente'):
                get_zodb_root().docente = BTrees.OOBTree.BTree()
            self.__docente = getattr(get_zodb_root(),'docente')
        return self.__docente

    def get_id_objeto(self, docente):
        return docente.get_cedula()

    def validar_objeto(self, docente):
        if not docente.get_cedula() or len(docente.get_cedula().strip()) == 0:
            raise Exception("Debe cargar cédula del docente!")
        if not docente.get_cedula().isdigit():
            raise Exception("La cedula debe ser numerica")
        if not docente.get_nombre():
            raise Exception("Debe ingresar un nombre para el docente!")
        if not docente.get_apellido():
            raise Exception("Debe ingresar un apellido para el docente!")
        if not (FechaControlador().validate_date(docente.get_fecha_nacimiento())):
            raise Exception("La Fecha de nacimiento ingresada es incorrecta!")
        if not docente.get_asignatura():
            raise Exception("Debe ingresar una asignatura para el docente!")
        if not docente.get_telefono() or len(docente.get_telefono().strip()) == 0:
            raise Exception("Debe ingresar un nro de telefono para el docente!")
        if not docente.get_departamento():
            raise Exception("Debe ingresar un departamento para el docente!")

    def validar_insercion_registro(self, docente):
        if docente.get_cedula() in self.get_diccionario_objetos().keys():
            raise Exception("Ya existe un docente con Cedula nro {}".format(docente.get_cedula()))

    def validar_eliminacion_registro(self, docente):
        if not docente.get_cedula() in self.get_diccionario_objetos().keys():
            raise Exception("NO existe docente con Cedula nro {}".format(docente.get_cedula()))

    def validar_actualizacion_registro(self, docente):
        if docente.get_cedula() in self.get_diccionario_objetos().keys():
            if not docente.get_cedula() or len(docente.get_cedula().strip()) == 0:
                raise Exception("Debe cargar cédula del docente!")
            if not docente.get_cedula().isdigit():
                raise Exception("La cedula debe ser numerica")
            if not docente.get_nombre():
                raise Exception("Debe ingresar un nombre para el docente!")
            if not docente.get_apellido():
                raise Exception("Debe ingresar un apellido para el docente!")
            if not (FechaControlador().validate_date(docente.get_fecha_nacimiento())):
                raise Exception("La Fecha de nacimiento ingresada es incorrecta!")
            if not docente.get_asignatura():
                raise Exception("Debe ingresar una asignatura para el docente!")
            if not docente.get_telefono() or len(docente.get_telefono().strip()) == 0:
                raise Exception("Debe ingresar un nro de telefono para el docente!")
            if not docente.get_departamento():
                raise Exception("Debe ingresar un departamento para el docente!")
            
    def buscar_codigo(self, codigo):
        if not codigo in self.get_diccionario_objetos().keys():
            raise Exception ("No existe docente con codigo {}".format(codigo))
        else:      
            return self.get_diccionario_objetos()[codigo]
 ##############################################################################################################
class ControladorFuncionario(ControladorAncestro):
    """Permite registrar y borrar funcionario, tambien facilita buscar funcionario
    en la BD del ZODB buscando por codigo de funcionario"""
    
    __funcionario = None
    
    def get_diccionario_objetos(self):
        #sino existe en diccionario de funcionario, creo uno en el root
        if not self.__funcionario:
            if not hasattr(get_zodb_root(), 'funcionario'):
                get_zodb_root().funcionario = BTrees.OOBTree.BTree()
            self.__funcionario = getattr(get_zodb_root(), 'funcionario')
        return self.__funcionario

    def get_id_objeto(self, funcionario):
        return funcionario.get_codigo()
    
    def validar_objeto(self, funcionario):
        if not funcionario.get_cedula() or len(funcionario.get_cedula().strip()) == 0:
            raise Exception("Debe cargar cédula del funcionario!")
        if not funcionario.get_cedula().isdigit():
            raise Exception("La cedula debe ser numerica")
        if not funcionario.get_nombre():
            raise Exception("Debe ingresar un nombre para el funcionario!")
        if not funcionario.get_apellido():
            raise Exception("Debe ingresar un apellido para el funcionario!")
        if not (FechaControlador().validate_date(funcionario.get_fecha_nacimiento())):
            raise Exception("La Fecha de nacimiento ingresada es incorrecta!")
        if not funcionario.get_cargo():
            raise Exception("Debe ingresar una cargo para el funcionario!")
        if not funcionario.get_telefono() or len(funcionario.get_telefono().strip()) == 0:
            raise Exception("Debe ingresar un nro de telefono para el funcionario!")
        if not funcionario.get_departamento():
            raise Exception("Debe ingresar un departamento para el funcionario!")

    def validar_insercion_registro(self, funcionario):
        if funcionario.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception("Ya existe funcionario con Codigo {}".format(funcionario.get_codigo()))

    def validar_eliminacion_registro(self, funcionario):
        if not funcionario.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception("No existe docente con Cedula nro {}".format(funcionario.get_codigo()))

    def validar_actualizacion_registro(self, funcionario):
        if funcionario.get_cedula() in self.get_diccionario_objetos().keys():
            if not funcionario.get_cedula() or len(funcionario.get_cedula().strip()) == 0:
                raise Exception("Debe cargar cédula del funcionario!")
            if not funcionario.get_cedula().isdigit():
                raise Exception("La cedula debe ser numerica")
            if not funcionario.get_nombre():
                raise Exception("Debe ingresar un nombre para el funcionario!")
            if not funcionario.get_apellido():
                raise Exception("Debe ingresar un apellido para el funcionario!")
            if not (FechaControlador().validate_date(funcionario.get_fecha_nacimiento())):
                raise Exception("La Fecha de nacimiento ingresada es incorrecta!")
            if not funcionario.get_cargo():
                raise Exception("Debe ingresar una cargo para el funcionario!")
            if not funcionario.get_telefono() or len(funcionario.get_telefono().strip()) == 0:
                raise Exception("Debe ingresar un nro de telefono para el funcionario!")
            if not funcionario.get_departamento():
                raise Exception("Debe ingresar un departamento para el funcionario!")
    
    def buscar_codigo(self, codigo):
        if not codigo in self.get_diccionario_objetos().keys():
            raise Exception ("No existe funcionario con codigo {}".format(codigo))
        else:      
            return self.get_diccionario_objetos()[codigo]
#########################################################################################################
class ControladorContacto(ControladorAncestro):
    """Permite registrar y borrar el contacto de un empleado"""
    
    __contacto = None
    
    def get_diccionario_objetos(self):
        #sino existe en diccionario de contacto, creo uno en el root
        if not self.__contacto:
            if not hasattr(get_zodb_root(), 'contacto'):
                get_zodb_root().contacto = BTrees.OOBTree.BTree()
            self.__contacto = getattr(get_zodb_root(), 'contacto')
        return self.__contacto

    def get_id_objeto(self, contacto):
        return contacto.get_numero_telefonico()
    
    def validar_objeto(self, contacto):
        if not contacto.get_numero_telefonico().isdigit():
            raise Exception("El numero telefonico debe ser numerico")
        if not contacto.get_numero_telefonico() or len(contacto.get_numero_telefonico().strip()) == 0:
            raise Exception("Debe cargar el numero telefonico del empleado!")
        if not contacto.get_correo_electronico():
            raise Exception("Debe ingresar un correo electronico para el empleado!")
       
    def validar_insercion_registro(self, contacto):
        if contacto.get_numero_telefonico() in self.get_diccionario_objetos().keys():
            raise Exception("Ya existe un empleado con el mismo numero telefonico {}".format(contacto.get_numero_telefonico()))

    def validar_eliminacion_registro(self, contacto):
        if not contacto.get_numero_telefonico() in self.get_diccionario_objetos().keys():
            raise Exception("No existe un empleado con el numero telefonico {}".format(contacto.get_numero_telefonico()))

    def validar_actualizacion_registro(self, contacto):
        if contacto.get_numero_telefonico() in self.get_diccionario_objetos().keys():
            if not contacto.get_numero_telefonico() or len(contacto.get_numero_telefonico().strip()) == 0:
                raise Exception("Debe cargar el numero telefonico!")
            if not contacto.get_numero_telefonico().isdigit():
                raise Exception("El numero telefonico debe ser numerico")
            if not contacto.get_correo_electronico():
                raise Exception("Debe ingresar un correo electronico!")
    
    def buscar_codigo(self, codigo):
        if not codigo in self.get_diccionario_objetos().keys():
            raise Exception ("No existe empleado con codigo {}".format(codigo))
        else:      
            return self.get_diccionario_objetos()[codigo]

#########################################################################################################
class FechaControlador():
    """El controlador de fecha valida que la fecha introducida sea la correta"""
    def validate_date(self,date):
        """
        Funcion para validar una fecha en formato:
            dd/mm/yyyy, dd/mm/yy, d/m/yy, dd/mm/yyyy hh:mm:ss, dd/mm/yy hh:mm:ss, d/m/yy h:m:s
        """
        for format in ['%d/%m/%Y', '%d/%m/%y', '%d/%m/%Y %H:%M:%S', '%d/%m/%y %H:%M:%S']:
            try:
                result = time.strptime(date, format)
                return True
            except:
                pass
        return False
#########################################################################################################   	
class ControladorLaboratorio(ControladorAncestro):
    """Controlador que permite la creacion de objetos del tipo laboratorio que cumplan las indicaciones dadas
    tambien permite borrarlos y buscar por codigo dentro del ZODB, un laboratorio no puede ser creado si no existe
    un empleado para el laboratorio"""
    __laboratorio = None
    
    def get_diccionario_objetos(self):
        #sino existe el diccionario de laboratorio, creo uno en el root
        if not self.__laboratorio:
            if not hasattr(get_zodb_root(), 'laboratorio'):
                get_zodb_root().laboratorio = BTrees.OOBTree.BTree()
            self.__laboratorio = getattr(get_zodb_root(), 'laboratorio')
        return self.__laboratorio

    def get_id_objeto(self, laboratorio):
        return laboratorio.get_codigo()

    def validar_objeto(self, laboratorio):
        if not laboratorio.get_codigo() or len(laboratorio.get_codigo().strip()) == 0:
            raise Exception("Debe ingresar un codigo para el laboratorio!")        
        if not contacto.get_codigo().isdigit():
            raise Exception("El codigo debe ser numerico")
        if not laboratorio.get_nombre():
            raise Exception("Debe ingresar un nombre para el laboratorio!")
        if not laboratorio.get_cantidad_maquinas():
            raise Exception("Debe ingresar la cantidad de maquina para el laboratorio!")
        if not contacto.get_cantidad_maquinas().isdigit():
            raise Exception("La cantidad de maquinas debe ser numerica")      
            
    def validar_insercion_registro(self, laboratorio):
        if laboratorio.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception("Ya existe un laboratorio con codigo {}".format(laboratorio.get_codigo()))

    def validar_actualizacion_registro(self, laboratorio):
        if laboratorio.get_codigo() in self.get_diccionario_objetos().keys():
            if not laboratorio.get_codigo() or len(laboratorio.get_codigo().strip()) == 0:
                raise Exception("Debe ingresar un codigo para el laboratorio!")        
            if not contacto.get_codigo().isdigit():
                raise Exception("El codigo debe ser numerico")
            if not laboratorio.get_nombre():
                raise Exception("Debe ingresar un nombre para el laboratorio!")
            if not laboratorio.get_cantidad_maquinas():
                raise Exception("Debe ingresar la cantidad de maquina para el laboratorio!")
            if not contacto.get_cantidad_maquinas().isdigit():
                raise Exception("La cantidad de maquinas debe ser numerica")  

    def validar_eliminacion_registro(self, laboratorio):
        if not laboratorio.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception("NO existe un laboratorio con codigo {}".format(laboratorio.get_codigo()))

    def buscar_codigo(self, codigo):
        if not codigo in self.get_diccionario_objetos().keys():
            raise Exception ("No existe laboratorio con codigo {}".format(codigo))
        else:      
            return self.get_diccionario_objetos()[codigo]

#########################################################################################################

class ControladorUsuario:
    """Retorna el usuario de acuerdo a los datos ingredatos"""
    def buscar(self, codigo, password):
        if codigo == 'root' and password == 'pass':
            return Usuario('root', 'SuperUsuario', 'Sistema')

            
#########################################################################################################

class ControladorFicha(ControladorAncestro):
    """Permite registrar y borrar la ficha """
    
    __ficha = None
    
    def get_diccionario_objetos(self):
        #sino existe en diccionario de fichas, creo uno en el root
        if not self.__ficha:
            if not hasattr(get_zodb_root(), 'ficha'):
                get_zodb_root().ficha = BTrees.OOBTree.BTree()
            self.__ficha = getattr(get_zodb_root(), 'ficha')
        return self.__ficha

    def get_id_objeto(self, ficha):
        return contacto.get_codigo()
    
    def validar_objeto(self, ficha):
        if not ficha.get_codigo().isdigit():
            raise Exception("El codigo debe ser numerico")
        if not ficha.get_hora_inicio().isdigit():
            raise Exception("la hora debe ser numerico")
        if not ficha.get_hora_fin().isdigit():
            raise Exception("la hora fin debe ser numerico")
        if not (FechaControlador().validate_date(ficha.get_fecha())):
            raise Exception("La Fecha ingresada es incorrecta!")    
       
    def validar_insercion_registro(self, ficha):
        if ficha.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception("Ya existe una ficha con el mismo codigo {}".format(ficha.get_codigo()))

    def validar_eliminacion_registro(self, ficha):
        if not ficha.get_codigo() in self.get_diccionario_objetos().keys():
            raise Exception("No existe una ficha con ese codigo {}".format(ficha.get_codigo()))

    def validar_actualizacion_registro(self, ficha):
        if ficha.get_codigo() in self.get_diccionario_objetos().keys():
            if not ficha.get_codigo().isdigit():
                raise Exception("El codigo debe ser numerico")
            if not ficha.get_hora_inicio().isdigit():
                raise Exception("la hora debe ser numerico")
            if not ficha.get_hora_fin().isdigit():
                raise Exception("la hora fin debe ser numerico")
            if not (FechaControlador().validate_date(ficha.get_fecha())):
                raise Exception("La Fecha ingresada es incorrecta!")   
    
    def buscar_codigo(self, codigo):
        if not codigo in self.get_diccionario_objetos().keys():
            raise Exception ("No existe un codigo {}".format(codigo))
        else:      
            return self.get_diccionario_objetos()[codigo]
###################################################################################################
#Pruebas
if __name__=="__main__":
    print(True)
    el_controlador = ControladorDocente()
    #cedula, nombre, apellido, fecha_nacimiento, departamento, telefono, asignatura
    el_docente = Docente('Paradigma', 'INformatica', '25-654521', '512511', 'Morel', 'Cynthia<3', '18/10/95')
    el_controlador.crear(el_docente)







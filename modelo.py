import persistent
from abc import ABCMeta, abstractmethod


#Persona debe extender de persistent.Persistent para que sea manejado por ZODB
class Persona(persistent.Persistent):
    __Metaclass__=ABCMeta
    """Clase abstracta que contiene los atributos basicos, de una persona"""
    def __init__(self, cedula, nombre, apellido, fecha_nacimiento):
        persistent.Persistent.__init__(self)
        self.__cedula = cedula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
    
    def set_cedula(self, cedula):
        self.__cedula = cedula
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_apellido(self, apellido):
        self.__apellido = apellido
    
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento
    
    def get_cedula(self):
        return self.__cedula
    
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def __str__(self):
        return "Persona['%s', '%s', '%s', '%s']" % (self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento())


class Empleado (Persona):
    """Clase que hereda las propiedades de una persona, como atributos propios de un empleado"""
    __Metaclass__=ABCMeta
    def __init__(self, departamento, telefono, *args):
        Persona.__init__ (self, *args)
        self.__departamento = departamento
        self.__telefono = telefono
    
    def set_departamento (self, departamento):
        self.__departamento = departamento

    def get_departamento (self):
        return self.__departamento
    
    def set_telefono(self, telefono):
        self.__telefono = telefono
    
    def get_telefono (self):
        return self.__telefono

    def __str__(self):
        return "Empleado['%s', '%s', '%s', '%s','%s','%s']" % (self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento(), self.get_departamento(), self.get_telefono())
	

class Docente(Empleado):
    """Clase que hereda las propiedades de una persona, 
    como atributos propios de un docente"""
    def __init__(self, asignatura, *args):
        Empleado.__init__(self,*args)
        self.__asignatura = asignatura
        """el docente se compone de contactos"""
        self.__lista_de_contacto = []
        self.__lista_laboratorios = []
    
    #agrega un laboratorio a la lista - emulando la posesion del prestamo
    def agregar_laboratorio(self, laboratorio):
        self.__lista_laboratorios.append(laboratorio)
        self._p_changed = True #permite que los datos se guarden como peristentes

    #libera al laboratorio de su prestamo
    def eliminar_laboratorio(self, laboratorio):
        self.__lista_laboratorios.remove(laboratorio)
        self._p_changed = True #permite que los datos se guarden como peristentes

    def set_asignatura(self, asignatura):
        self.__asignatura = asignatura
       
    def get_asignatura(self):
        return self.__asignatura

    #agrega un contacto a la lista
    def set_agregar_contacto(self, contacto):
        """agregar contacto"""
        self.__lista_de_contacto.append(contacto) 
        self._p_changed = True #permite que los datos se guarden como peristentes

    #elimina un contacto de la lista
    def eliminar_contacto(self, contacto):
        self.__lista_de_contacto.remove(contacto)
        self._p_changed = True #permite que los datos se guarden como persitentes

    def __str__(self):
        return "Docente['%s', '%s', '%s', '%s','%s','%s']" % (self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento(), self.get_asignatura(), self.get_telefono())


class Funcionario(Empleado):
    """Clase que hereda las propiedades de una persona, 
    como atributos propios de un funcionario"""
    __Metaclass__=ABCMeta
    def __init__(self, cargo, *args):
        Empleado.__init__(self,*args)
        self.__cargo = cargo
        """el funcionario se compone de contactos"""  
        self.__lista_de_contacto = []
        self.__lista_laboratorios = []

    #agrega un laboratorio a la lista - emulando la posesion del prestamo
    def agregar_laboratorio(self, laboratorio):
        self.__lista_laboratorios.append(laboratorio)
        self._p_changed = True #permite que los datos se guarden como peristentes

    #libera al laboratorio de su prestamo
    def eliminar_laboratorio(self, laboratorio):
        self.__lista_laboratorios.remove(laboratorio)
        self._p_changed = True #permite que los datos se guarden como peristentes

    def set_cargo(self, asignatura):
        self.__cargo = cargo
       
    def get_cargo(self):
        return self.__cargo

    #agrega un contacto a la lista
    def set_agregar_contacto(self, contacto):
        """agregar contacto"""
        self.__lista_de_contacto.append(contacto) 
        self._p_changed = True #permite que los datos se guarden como peristentes

    #elimina un contacto de la lista
    def eliminar_contacto(self, contacto):
        self.__lista_de_contacto.remove(contacto)
        self._p_changed = True #permite que los datos se guarden como persitentes

    def __str__(self):
        return "Funcionario['%s', '%s', '%s', '%s','%s','%s']" % (self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento(), self.get_departamento(), self.get_cargo(), self.get_telefono())


class Contacto:
    """ Clase que define las propiedades de un contacto"""
    def __init__ (self, numero_telefonico, correo_electronico):
        self.__numero_telefonico = numero_telefonico
        self.__correo_electronico = correo_electronico

    def set_numero_telefonico (self, numero_telefonico):
        self.__numero_telefonico = numero_telefonico
	
    def get_numero_telefonico (self):
        return self.__numero_telefonico

    def set_correo_electronico (self, correo_electronico):
        self.__correo_electronico = correo_electronico

    def get_correo_electronico (self):
        return self.__correo_electronico

    def __str__(self):
        return "Contacto['%s', '%s']" % (self.get_numero_telefonico(), self.get_correo_electronico())


class Reservable:
    """Clase que define algo reservable, de forma que se guarde los datos"""
    __Metaclass__=ABCMeta

    @abstractmethod
    def reserva(self):
        """metodo abstracto y polimorfico que define la forma de reservar de un objeto"""
        pass


class Consultable:
    """Clase que define como consultar un objeto"""
    __Metaclass__=ABCMeta
    
    @abstractmethod
    def consultar(self):
        """metodo abstracto y polimorfico que define la forma de consultar de un objeto"""
        pass


class Laboratorio(Reservable, Consultable,persistent.Persistent): 
    """Clase que define a un laboratorio con un nombre, estado, se compone de un autor, hereda las propiedades de Reservable y Consultable"""
    def __init__(self, codigo, nombre, cantidad_maquinas):
        persistent.Persistent.__init__(self)
        Reservable.__init__(self)
        Consultable.__init__(self)
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidad_maquinas = cantidad_maquinas

        #le agregue esto ya que un laboratorio puede ser prestado varias veces pero en diferentes horarios.
        self.__fichas = [] #la ficha contiene el horario y fecha del prestamo de un laboratorio - 

    #implementar las funciones abstractas
    def reserva(self,ficha):
        """Reserva el laboratorio."""
        agregar_ficha(ficha)
        

    def consultar(self):
        #Consulta la disponibilidad del laboratorio retornando el listado de fichas
        return self.__fichas

    #Pemite agregar una ficha - equivalente a un prestamo
    def agregar_ficha(self, ficha):
        self.__fichas.append(ficha)
        self._p_changed = True #permite que los datos se guarden como persitentes

    #Permite eliminar la ficha - liberando el prestamo del mismo
    def eliminar_ficha(self, ficha):
        self.__fichas.remove(ficha)
        self._p_changed = True #permite que los datos se guarden como persitentes

    def set_codigo(self, codigo):
        self.__codigo = codigo
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def agregar_cantidad_maquinas(self, cantidad_maquinas):
        self.__cantidad_maquinas = cantidad_maquinas
              
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre
    
    def get_cantidad_maquinas(self):
        return self.__cantidad_maquinas

    def __str__(self):
        return "%s" % (self.get_nombre())


class Ficha:
    """Clase que contiene los datos basico para un prestamo tales como la hora y fecha"""
    def __init__ (self, codigo, cedula, hora_inicio, hora_fin, fecha):
        self.__codigo = codigo
        self.__cedula = cedula
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin
        self.__fecha = fecha

    def set_codigo (self, codigo):
        self.__codigo = codigo 

    def set_hora_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    def get_hora_inicio(self):
        return self.__hora_inicio

    def set_hora_fin(self, hora_fin):
        self.__hora_fin = hora_fin

    def set_cedula(self, cedula):
        self.__cedula = cedula

    def get_codigo (self):
        return self.__codigo

    def get_cedula (self):
        return self.__cedula

    def get_hora_fin(self):
        return self.__hora_fin

    def set_fecha (self, fecha):
        self.__fecha = fecha

    def get_fecha(self):
        return self.__fecha

    def __str__(self):
        return "Ficha['%s', %s', '%s', '%s']"% (self.get_codigo(), self.get_hora_inicio(), self.get_hora_fin(),self.get_fecha())



class App:
    if __name__=="__main__":
        #print de pueba 
        print(True)

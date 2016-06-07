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
        Persona.__init__ (self,*args)
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
        return "Alumno['%s', '%s', '%s', '%s','%s','%s']" % (self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento(), self.get_departamento(), self.get_telefono())
	
class Docente(Empleado):
    """Clase que hereda las propiedades de una persona, 
    como atributos propios de un docente"""
    def __init__(self, asignatura, *args):
        Empleado.__init__(self,*args)
        self.__asignatura = asignatura
        """el docente se compone de contactos"""
        self.__lista_de_contacto = [] 
    
    def set_asignatura(self, asignatura):
        self.__asignatura = asignatura
       
    def get_asignatura(self):
        return self.__asignatura

    def set_agregar_contacto(self, contacto):
        """agregar contacto"""
        self.__lista_de_contacto.append(contacto) 

    def __str__(self):
        return "Docente['%s', '%s', '%s', '%s','%s','%s']" % (self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento(), self.get_carrera(), self.get_telefono())

class Funcionario(Empleado):
    """Clase que hereda las propiedades de una persona, 
    como atributos propios de un funcionario"""
    __Metaclass__=ABCMeta
    def __init__(self, cargo, *args):
        Empleado.__init__(self,*args)
        self.__cargo = cargo
        """el funcionario se compone de contactos"""  
        self.__lista_de_contacto = []  

    def set_cargo(self, asignatura):
        self.__cargo = cargo
       
    def get_cargo(self):
        return self.__cargo

    def set_agregar_contacto(self, contacto):
        """agregar contacto"""
        self.__lista_de_contacto.append(contacto) 

    def __str__(self):
        return "Funcionario['%s', '%s', '%s', '%s','%s','%s']" % (self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento(), self.get_carrera(), self.get_telefono())

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
        return "Laboratorio['%s', '%s','%s','%s']" % (self.get_codigo(), self.get_nombre(), self.get_autor() ,self.get_tipo())


class App:
    if __name__=="__main__":
        #print de pueba 
        print(True)

        #################asignatura, telefono,  cedula,  nombre,   apellido, fecha_nac
        docente = Docente('LCIK','0982581092','4490207','Jessica','Matiauda','26/01/1992')
        print(alumno.__str__())
        
        #cedula, nombre, apellido, fecha_nacimiento, departamento, telefono, asignatura
    el_docente = Docente('Paradigma', 'INformatica', '25-654521', '512511', 'Morel', 'Cynthia', '18/10/95')
        
        """############### nombre,  apellido, nacionalidad
        autor = Autor('1','Dimitri', 'Vegas', 'Magleña')
        print(autor.__str__())
        
        #nombre, estado
        libro = Libro('1','El Libro',autor)
        print (libro.__str__())
        
        la_ficha = Ficha('6','15/11/2011',libro,autor)
        print(la_ficha.__str__())
        """


        




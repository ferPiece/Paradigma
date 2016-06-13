import os
import sys
import datetime
import hashlib


def limpiar_pantalla():
    '''Limpia la pantalla. Se tiene en cuenta si el OS es windows o linux'''
    os.system('cls' if os.name=='nt' else 'clear')

def get_entero(value, value_error_msg):
  try:
     return int(value)
  except ValueError:
     raise ValueError(value_error_msg)   
     
def leer_entero(msg, min_value=None, max_value=None, default=None, min_value_error='[min_value = {}]', 
                max_value_error='[max_value = {}]', numero_invalido_msg='Numero invalido'):
    ''' (string, int, int) -> int
       Pide que se ingrese número. Solo se retorna resultado cuando se ingresa
       un valor válido.
       @Parámetros
          msg : mensaje que se muestra al usuario.
          min_value: el valor mínimo que usuario debe ingresar
          max_value: el valor máximo que usuario debe ingresar
       Ej:
          leer_numero('Ingrese un número entre 1 y 9', 1, 9)
    '''
    while ( True ): 
        cualquier_valor = input(msg)
        try:
            #tratamos de convertir en número entero
            number = get_entero(cualquier_valor, numero_invalido_msg)

            if min_value and (number < min_value):
                error_msg = min_value_error.format(str(min_value))
                raise ValueError(error_msg)

            if max_value and (number > max_value):
                error_msg = max_value_error.format(str(max_value))
                raise ValueError(error_msg)

            #se retorna valor válido ingresado por el usuario
            return number
        except ValueError as ve:
            print (ve)
        except Exception as e:
            print (e)
              

def leer_cadena(msg, obligatorio, default=''):
    while ( True ): 
        if default:
           msg = msg + default + chr(8) * len(default)

        data = input(msg)
        data = data or default
        try:
            if obligatorio and len(data.strip()) == 0:
                raise Exception("Debe ingresar valor!")
            #se retorna valor válido ingresado por el usuario
            return data
        except Exception as e:
            print (e)
            
def pausa(msg):
    input(msg)

def es_numerico( cadena):
    if cadena.isdigit():
        return True
    return False

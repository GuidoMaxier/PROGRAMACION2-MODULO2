import json
from datetime import datetime, date

#EJERCICIO N° 4 
def suma(num1, num2):
    """Suma dos números enteros y muestra el resultado."""
    resultado = num1 + num2
    return resultado
  
        
#EJERCICIO N°5
def calcular_edad(dob):
    """Calcula la edad de una persona en base a su fecha de nacimiento."""
    fecha_nacimiento = datetime.strptime(dob, '%Y-%m-%d')
    fecha_actual = datetime.now()

    if fecha_nacimiento > fecha_actual:
        return None
       
    else:
        edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        return edad

    

#EJERCICIO N°6 y N°7
def operacion(operation, num1, num2):
    """Realiza operaciones matematicas con dos numeros enteros."""    
    
    if operation == 'sum':
        return num1 + num2
    elif operation == 'sub':
        return num1 - num2
    elif operation == 'mult':
        return num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "La división por cero no está permitida"
        else:
            return num1 / num2
    else:
        return "Operacion no definida"
    
    
#EJERCICIO N°9
def formato_dni(dni):
    """Devuelve el numero de DNI convertido en entero."""

    #Usamos replace para reemplazar los punto y guiones por nada.
    numero_dni = dni.replace('.', '').replace('-', '')
    
   #Validamos que el DNI tenga  
    if not numero_dni.isdigit() or len(numero_dni) != 8 or numero_dni[0] == '0':
        return None
    
    formato_dni = int(numero_dni)
    return formato_dni


  


# Cargar el diccionario morse_code desde el archivo JSON
with open('mi_proyecto/hola_mundo/static/morse_code.json', 'r') as f:
        morse_code_data = json.load(f)

#EJERCICIO N° 11
 # Función para codificar una palabra a código morse
def encode_morse(keyword):
        """Codifica una palabra a codigo morse."""
        keyword = keyword.upper()
        encoded = []
        keyword = keyword.replace("+", " ")
        for char in keyword:
            encoded.append(morse_code_data['letters'].get(char, char))
        return '+'.join(encoded)


#EJERCICIO N° 12
# Función para decodificar un código morse a una palabra
def decode_morse_fun(morse_code):
        """Decodifica codigo morse a una palabra."""
        morse_code = morse_code.replace("+", " ")

        decoded = []

        #Creamos una Dicionario vacio
        morse_dict = {}  
        #invertimos clave por valor, y valor por clave       
        for k, v in morse_code_data['letters'].items(): #{v: k for k, v in morse_code_data['letters'].items()}
                morse_dict[v]=k

        for code in morse_code.split():
                decoded.append(morse_dict.get(code, code))
        return ''.join(decoded)


#EJERCICIO N° 13
def binary_decimal(num):
    """Convierte un numero binario a decimal."""
    if all(digit in ('0', '1') for digit in num):
        decimal_value = 0
        num = num[::-1]  # Invertimos el número binario para facilitar la conversión
        for i, digit in enumerate(num):
            if digit == '1':
                decimal_value += 2 ** i
        return decimal_value
    else:
        return None
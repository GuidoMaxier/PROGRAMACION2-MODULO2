import json


def formato_dni(dni):
    """Devuelve un json con el numero de DNI en entero"""

    #Usamos replace para reemplazar los punto y guiones por nada.
    numero_dni = dni.replace('.', '').replace('-', '')
    
   #Validamos que el DNI tenga  
    if not numero_dni.isdigit() or len(numero_dni) != 8 or numero_dni[0] == '0':
            return {'error': 'DNI inválido'}, 400
    
    formato_dni = int(numero_dni)
    return {'DNI': formato_dni}, 200

'''
#EJERCICIO 11 
# Cargamos el archivo morse_code.json
with open("static/morse_code.json", "r") as morse_code_file:
    morse_code_data = json.load(morse_code_file)

def codificar_a_morse(keyword):
    # Verificamos que la palabra clave no exceda los 100 caracteres
    if len(keyword) > 100:
        return {'error': 'La palabra clave supera los 100 caracteres.'}, 400

    # Verificamos que no haya caracteres "^" en la palabra clave
    if '^' in keyword:
        return {'error': 'La palabra clave no puede contener el carácter "^"'}, 400  

    # Verificamos que no haya caracteres no válidos en la palabra clave
    for char in keyword:
        if char not in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+'):
            return {'error': 'Carácter no válido en la palabra clave'}, 400

    # Reemplazar el carácter '+' con espacio ' ' para decodificar las palabras
    keyword = keyword.replace('+', ' ')

    # Dividir la entrada en palabras clave utilizando el carácter "^" como separador
    keywords = keyword.split('^') '''

  













    
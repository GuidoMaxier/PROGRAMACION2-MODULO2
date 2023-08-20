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



# Cargar el diccionario morse_code desde el archivo JSON
with open('mi_proyecto/hola_mundo/static/morse_code.json', 'r') as f:
        morse_code_data = json.load(f)

# with open('C:/Users/Guido Maxier/Documents/GitHub/PROGRAMACION2-MODULO2/mi_proyecto/hola_mundo/static/morse_code.json', 'r') as f:
#         morse_code_data = json.load(f)

 # Función para codificar una palabra a código morse
def encode_morse(keyword):
        keyword = keyword.upper()
        encoded = []
        keyword = keyword.replace("+", " ")
        for char in keyword:
            encoded.append(morse_code_data['letters'].get(char, char))
        return '+'.join(encoded)

# Función para decodificar un código morse a una palabra
def decode_morse_fun(morse_code):
        morse_code = morse_code.replace("+", " ")

        decoded = []

        #invertimos clave por valor, y valor por clave
        morse_dict = {} 
                
        for k, v in morse_code_data['letters'].items(): #{v: k for k, v in morse_code_data['letters'].items()}
                morse_dict[v]=k

        for code in morse_code.split():
                decoded.append(morse_dict.get(code, code))
        return ''.join(decoded)
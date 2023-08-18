
def formato_dni(dni):
    """Devuelve un json con el numero de DNI en entero"""

    #Usamos replace para reemplazar los punto y guiones por nada.
    numero_dni = dni.replace('.', '').replace('-', '')
    
   #Validamos que el DNI tenga  
    if not numero_dni.isdigit() or len(numero_dni) != 8 or numero_dni[0] == '0':
            return {'error': 'DNI inválido'}, 400
    
    formato_dni = int(numero_dni)
    return {'DNI': formato_dni}, 200
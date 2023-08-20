from flask import Flask, jsonify, request
from config import Config
from datetime import datetime, date


#importamos la util.py para el manejos de funciones 
#y pilas.py archivo visto en algoritmia (P/Ejercicio 14)
from .static.pilas import balanceador
from .static.util import suma, calcular_edad, operacion, formato_dni, binary_decimal
from .static.util import encode_morse, decode_morse_fun



def init_app():
    """Crea y configura la aplicación Flask."""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)


#EJERCICIO N° 1
    @app.route('/')
    def bienvenida():
        """Devuelve un mensaje de bienvenida en formato JSON."""
        try:
            return jsonify({'mensaje': 'Bienvenido!'}), 200
    
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        

#EJERCICIO N° 2    
    @app.route('/info')
    def informacion():
        """Devuelve un mensaje de bienvenida en formato JSON. a la aplicacion."""
        try:
            mensaje = f"Bienvenido a {Config.APP_NAME}"
            return jsonify({'mensaje': mensaje}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        

#EJERCICIO N° 3     
    @app.route('/about')
    def about():
        """Devuelve en JSON informacion sobre la aplicacion."""
        try:
            info = {
                'app_name': Config.APP_NAME,
                'description': Config.APP_DESCRIPTION,
                'developers': Config.DEVELOPERS,
                'version': Config.APP_VERSION
            }
            return jsonify(info), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        
        
#EJERCICIO N° 4 
    @app.route('/sum/<int:num1>/<int:num2>')
    def sumar(num1, num2):
        """Suma dos numeros enteros y muestra el resultado."""
        try:
            resultado = suma(num1, num2)
            return jsonify({'resultado': resultado}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        
        
#EJERCICIO N° 5 
    @app.route('/age/<dob>')
    def edad(dob): 
        """Calcula la edad de una persona en base a su fecha de nacimiento."""  
        try:
            edad = calcular_edad(dob)

            if edad == None:
                return jsonify({'error': 'La fecha de nacimiento es posterior a la fecha actual'}), 400
            
            return jsonify({'edad': edad}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400

        
        
#EJERCICIO N°6
    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def realizar_operacion(operation, num1, num2):
        """Realiza operacion matematicas con dos numeros enteros."""
        
        try:
            resultado = operacion(operation, num1, num2)

            if isinstance(resultado, (int, float)):
                return jsonify({'resultado':resultado}), 200 
            
            else:
                return jsonify({'error': resultado}), 400
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400    



#EJERCICIO N°7
    @app.route('/operate')
    def operar():
        """Realiza operacion matematicas con dos numeros enteros
        usando parametros de consulta."""

        try:
            operation = request.args.get('operation', default=None)
            num1 = int(request.args.get('num1', default=0))
            num2 = int(request.args.get('num2', default=0))

            resultado = operacion(operation, num1, num2)
            
            if isinstance(resultado, (int, float)):
                return jsonify({'resultado':resultado}), 200 
            
            else:
                return jsonify({'error': resultado}), 400
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
    


#EJERCICIO N°8
    @app.route('/title/<string:word>', methods=['GET'])
    def title(word):
        """Aplica el formato tiitulo al parametro del ruta word."""
        try:
            # Aplicamos el formato de título
            formatted_word = word.title()    
            return jsonify({'formatted_word': formatted_word}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400

        
#EJERCICIO N°9
    @app.route('/formatted/<string:dni>', methods=['GET'])
    def formato(dni):
        """Recibe como parámetro de ruta un DNI, y devuelva el DNI convertido a un entero. """
        try:
            formatted_dni = formato_dni(dni)

            if formatted_dni == None:
                return jsonify({'error':'DNI INVALIDO'}), 400  
            
            return jsonify({'formatted_dni':formatted_dni}), 200  
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400        

    

#EJERCICIO N°10
    @app.route('/format', methods=['GET'])
    def user_data():
        """recibe los datos de un usuario como parámetros de consulta"""
        try:
            firstname = request.args.get('firstname', default='').capitalize()
            lastname = request.args.get('lastname', default='').capitalize()
            dob = request.args.get('dob', default='')
            dni = request.args.get('dni', default='').replace('.', '').replace('-', '')
            
            age = calcular_edad(dob)
            formatted_dni = formato_dni(dni) 

            if age == None:
                return jsonify({'error': 'La fecha de nacimiento es posterior a la fecha actual'}), 400
            

            if formatted_dni == None:
                return jsonify({'error':'DNI INVALIDO'}), 400  
            
            
            response = {
                'firstname': firstname,
                'lastname': lastname,
                'age': age,
                'dni': formatted_dni
            }
            return jsonify(response), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        

#EJERCICIO N° 11 
    # Endpoint para codificar una palabra a código morse
    @app.route('/encode/<string:keyword>')
    def encode_keyword(keyword):
        """Encripta y devolve la palabra en código morse"""
        try:
            encoded_morse = encode_morse(keyword)
            return jsonify({'morse_code': encoded_morse}), 200
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        

#EJERCICIO N° 12 
    # Endpoint para decodificar un código morse a una palabra
    @app.route('/decode/<string:morse_code>')
    def decode_morse(morse_code):
        """Desencripta código morse y devolve la palabra en formato plano"""
        try:
            decoded_text = decode_morse_fun(morse_code)
            return jsonify({'decoded_text': decoded_text}), 200
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400

        
#EJERCICIO N° 13
    @app.route('/convert/binary/<string:num>')
    def binary_a_decimal(num):
        """Convierte un numero binario a decimal."""
        try:
            conversion = binary_decimal(num)
            if conversion == None:
                return jsonify({"error": "Numero binario invalido"}), 400
        
            return jsonify({"decimal": conversion}), 200
        
        except Exception as e:
            return jsonify({"error": "Ha ocurrido un error"}), 400        


#EJERCICIO N° 14
    @app.route('/balance/<string:input>')
    def balance(input):
        """Verificar si los símbolos están balanceados."""
        try:
            if balanceador(input):
                #print('Los limitadores estan balanceados')
                return jsonify({"balanced": True}), 200
            else:
                #print('Los limitadores NO estan balanceados') 
                return jsonify({"balanced": False}), 200
        except Exception as e:
            return jsonify({"error": "Numero binario invalido"}), 400


    return app


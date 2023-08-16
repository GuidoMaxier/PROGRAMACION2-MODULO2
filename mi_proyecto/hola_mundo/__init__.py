from flask import Flask, jsonify, request
from config import Config
from datetime import datetime, date

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)


#EJERCICIO N° 1
    @app.route('/')
    def bienvenida():
        """Devuelve un mensaje de bienvenida en formato JSON."""
        try:
            return jsonify({'mensaje': 'Bienvenido!'}, 200)
    
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}, 400)
        

#EJERCICIO N° 2    
    @app.route('/info')
    def informacion():
        try:
            mensaje = f"Bienvenido a {app.config['APP_NAME']}"
            return jsonify({'mensaje': mensaje}, 200)
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'},400)
        

#EJERCICIO N° 3     
    @app.route('/about')
    def about():
        try:
            info = {
                'app_name': app.config['APP_NAME'],
                'description': app.config['APP_DESCRIPTION'],
                'developers': app.config['DEVELOPERS'],
                'version': app.config['APP_VERSION']
            }
            return jsonify(info, 200)
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}, 400)
        
        
#EJERCICIO N° 4 
    @app.route('/sum/<int:num1>/<int:num2>')
    def suma(num1, num2):
        try:
            resultado = num1 + num2
            return jsonify({'resultado': resultado}, 200)
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}, 400)
        

#EJERCICIO N° 5 
    @app.route('/age/<dob>')
    def calcular_edad(dob):   
        try:
            fecha_nacimiento = datetime.strptime(dob, '%Y-%m-%d').date()
            fecha_actual = date.today()

            if fecha_nacimiento > fecha_actual:
                return jsonify({'error': 'La fecha de nacimiento es posterior a la fecha actual'}), 400

            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            return jsonify({'edad': edad}, 200)
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}, 400)  
        
        
#EJERCICIO N°6
    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operate(operation, num1, num2):
        if operation == 'sum':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mult':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return jsonify({'error': 'La división por cero no está permitida'}, 400)
            result = num1 / num2
        else:
            return jsonify({'error': 'Operación no válida'}, 400)

        return jsonify({'result': result}, 200)  


#EJERCICIO N°7
    @app.route('/operate')
    def operate_query_params():
        operation = request.args.get('operation', default=None)
        num1 = int(request.args.get('num1', default=0))
        num2 = int(request.args.get('num2', default=0))

        if operation is None:
            return jsonify({'error': 'Operación no especificada'}), 400

        if operation == 'sum':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mult':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return jsonify({'error': 'La división por cero no está permitida'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Operación no válida'}), 400

        return jsonify({'result':result}), 200


#EJERCICIO N°8
    @app.route('/title/<string:word>', methods=['GET'])
    def title(word):
        try:
            # Aplicamos el formato de título
            formatted_word = word.title()    
            return jsonify({'formatted_word': formatted_word}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400


#EJERCICIO N°9
    @app.route('/formatted/<string:dni>', methods=['GET'])
    def formatO_dni(dni):
        try:
            # Reemplazamos los caracteres no numéricos, puntos, guiones
            numero_dni = dni.replace('.', '').replace('-', '')
            
            # Verificamos que el DNI tenga 8 caracteres numéricos y que no empiece con ceros
            if len(numero_dni) != 8 or numero_dni[0] == '0':
                return jsonify({'error': 'DNI inválido'}), 400
            
            formatted_dni = int(numero_dni)
            return jsonify({'formatted_dni': formatted_dni}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400

    

#EJERCICIO N°10
    @app.route('/format', methods=['GET'])
    def user_data():
        try:
            firstname = request.args.get('firstname', default='').capitalize()
            lastname = request.args.get('lastname', default='').capitalize()
            dob = request.args.get('dob', default='')
            dni = request.args.get('dni', default='').replace('.', '').replace('-', '')

            # Validamos la fecha de nacimiento
            dob_date = datetime.strptime(dob, '%Y-%m-%d')
            current_date = datetime.now()
            
            if dob_date > current_date:
                return jsonify({'error': 'La fecha de nacimiento es posterior a la fecha actual'}), 400
            
            # Calculamos la edad de la persona en base a su fecha de nacimiento y devolvemos dicho valor.
            age = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))
        
            # Verificamos que el DNI tenga 8 caracteres numéricos y que no empiece con ceros
            if len(dni) != 8 or dni[0] == '0':
                return jsonify({'error': 'DNI inválido'}), 400
            
            formatted_dni = int(dni)
        
            response = {
                'firstname': firstname,
                'lastname': lastname,
                'age': age,
                'dni': formatted_dni
            }
            return jsonify(response), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400




#EJERCICIO N° 13
    @app.route('/convert/binary/<string:num>')
    def convert_binary_to_decimal(num):
        try:
            if all(digit in ('0', '1') for digit in num):
                decimal_value = 0
                num = num[::-1]  # Invertimos el número binario para facilitar la conversión

                for i, digit in enumerate(num):
                    if digit == '1':
                        decimal_value += 2 ** i

                return jsonify({"decimal": decimal_value}), 200
            else:
                return jsonify({"error": "Numero binario invalido"}), 400
        except ValueError:
            return jsonify({"error": "Numero binario invalido"}), 400



#EJERCICIO N° 14
    @app.route('/balance/<string:input>')
    def balance(input):
        stack = []
        opening_symbols = "([{"
        closing_symbols = ")]}"

        for symbol in input:
            if symbol in opening_symbols:
                stack.append(symbol)
            elif symbol in closing_symbols:
                if not stack:
                    return jsonify({"balanced": False}), 200

                top_symbol = stack.pop()
                if opening_symbols.index(top_symbol) != closing_symbols.index(symbol):
                    return jsonify({"balanced": False}), 200

        if not stack:
            return jsonify({"balanced": True}), 200

        return jsonify({"balanced": False}), 200
    

    return app


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
            return jsonify({'mensaje': 'Bienvenido!'}), 200
    
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        

#EJERCICIO N° 2    
    @app.route('/info')
    def informacion():
        try:
            mensaje = f"Bienvenido a {app.config['APP_NAME']}"
            return jsonify({'mensaje': mensaje}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        

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
            return jsonify({'error': 'Ha ocurrido un error'}), 400
        
        
#EJERCICIO N° 4 
    @app.route('/sum/<int:num1>/<int:num2>')
    def suma(num1, num2):
        try:
            resultado = num1 + num2
            return jsonify({'resultado': resultado}), 200
        
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400 
        

#EJERCICIO N° 5 
    @app.route('/age/<dob>')
    def calcular_edad(dob):   
        try:
            fecha_nacimiento = datetime.strptime(dob, '%Y-%m-%d').date()
            fecha_actual = date.today()

            if fecha_nacimiento > fecha_actual:
                return jsonify({'error': 'La fecha de nacimiento es posterior a la fecha actual'}), 400

            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            return jsonify({'edad': edad}), 200
        except Exception as e:
            return jsonify({'error': 'Ha ocurrido un error'}), 400               

#EJERCICIO N° 6
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
                return jsonify({'error':'La división por cero no está permitida'}), 400
            result = num1 / num2
        else:
            return jsonify({'error': 'Operación no válida'}), 400
        return jsonify({'result': result}), 200

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





    return app



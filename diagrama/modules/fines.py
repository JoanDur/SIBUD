from flask import Blueprint, request, jsonify
import json

fines_bp = Blueprint('fines', __name__)
FINES_FILE = 'fines.json'
FINE_PER_DAY = 2  # Monto de la multa por día de retraso

# Cargar multas desde archivo JSON
def load_fines():
    try:
        with open(FINES_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guardar multas en archivo JSON
def save_fines(fines):
    with open(FINES_FILE, 'w', encoding='utf-8') as file:
        json.dump(fines, file, indent=4)

# Obtener todas las multas
@fines_bp.route('/', methods=['GET'])
def get_fines():
    fines = load_fines()
    return jsonify({'fines': fines})

# Obtener multas de un usuario específico
@fines_bp.route('/user/<user_id>', methods=['GET'])
def get_fines_by_user(user_id):
    fines = load_fines()
    user_fines = {k: v for k, v in fines.items() if v['user_id'] == user_id}
    return jsonify({'user_fines': user_fines})

# Agregar una multa manualmente
@fines_bp.route('/', methods=['POST'])
def add_fine():
    fines = load_fines()
    data = request.get_json()
    fine_id = str(len(fines) + 1)
    fines[fine_id] = {'user_id': data['user_id'], 'book_id': data['book_id'], 'fine': data['fine']}
    save_fines(fines)
    return jsonify({'message': 'Multa agregada', 'fine': fines[fine_id]})
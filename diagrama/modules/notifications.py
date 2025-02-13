import json
from flask import Blueprint, request, jsonify

notifications_bp = Blueprint('notifications', __name__)
NOTIFICATIONS_FILE = 'notifications.json'

# Cargar notificaciones desde archivo JSON
def load_notifications():
    try:
        with open(NOTIFICATIONS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guardar notificaciones en archivo JSON
def save_notifications(notifications):
    with open(NOTIFICATIONS_FILE, 'w') as file:
        json.dump(notifications, file, indent=4)

# Obtener todas las notificaciones
@notifications_bp.route('/', methods=['GET'])
def get_notifications():
    notifications = load_notifications()
    return jsonify({'notifications': notifications})

# Agregar una nueva notificación
@notifications_bp.route('/', methods=['POST'])
def add_notification():
    notifications = load_notifications()
    data = request.get_json()
    notification_id = str(len(notifications) + 1)
    notifications[notification_id] = {'user_id': data['user_id'], 'message': data['message']}
    save_notifications(notifications)
    return jsonify({'message': 'Notificación agregada', 'notification': notifications[notification_id]})

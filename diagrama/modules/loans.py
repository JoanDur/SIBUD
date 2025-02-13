from flask import Blueprint, request, jsonify
from datetime import datetime, timedelta
from modules.books import check_availability, mark_as_borrowed

loans_bp = Blueprint('loans', __name__)

# Simulación de base de datos
loans = {}
LOAN_DAYS = 7

@loans_bp.route('/', methods=['GET'])
def get_loans():
    calculate_fines()  # Se calculan las multas antes de devolver los préstamos
    return jsonify({'loans': loans})

@loans_bp.route('/', methods=['POST'])
def add_loan():
    data = request.get_json()
    book_id = data.get('book_id')
    user_id = data.get('user_id')

    if not check_availability(book_id):
        return jsonify({'error': 'Libro no disponible'}), 400

    due_date = datetime.now() + timedelta(days=LOAN_DAYS)
    loan_id = str(len(loans) + 1)
    loans[loan_id] = {'user_id': user_id, 'book_id': book_id, 'due_date': due_date.strftime('%Y-%m-%d')}
    mark_as_borrowed(book_id)

    return jsonify({'message': 'Préstamo registrado', 'loan': loans[loan_id]}), 201

def calculate_fines():
    from modules.fines import load_fines, save_fines, FINE_PER_DAY
    fines = load_fines()
    today = datetime.now().date()
    
    for loan_id, loan in loans.items():
        due_date = datetime.strptime(loan['due_date'], '%Y-%m-%d').date()
        if today > due_date:
            overdue_days = (today - due_date).days
            fine_amount = overdue_days * FINE_PER_DAY
            fines[loan_id] = {'user_id': loan['user_id'], 'book_id': loan['book_id'], 'fine': fine_amount}
    
    save_fines(fines)

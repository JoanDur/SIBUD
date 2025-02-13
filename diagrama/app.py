from flask import Flask
from modules.books import books_bp
from modules.loans import loans_bp
from modules.fines import fines_bp
from modules.notifications import notifications_bp

app = Flask(__name__)

# Registrar Blueprints
app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(loans_bp, url_prefix='/loans')
app.register_blueprint(fines_bp, url_prefix='/fines')
app.register_blueprint(notifications_bp, url_prefix='/notifications')

if __name__ == '__main__':
    app.run(debug=True)

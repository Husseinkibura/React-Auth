from flask import Flask
from flask_cors import CORS
from extensions import db, bcrypt, jwt

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost/react_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'

# Initialize extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

# Import routes
from routes.auth_routes import bp as auth_bp
from routes.item_routes import bp as item_bp

# Register routes
app.register_blueprint(auth_bp)
app.register_blueprint(item_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

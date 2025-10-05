from flask import Flask
from src.db.mongo_connection import init_db, mongo
from src.middleware.auth_middleware import init_jwt
from src.modules.auth_routes import user_bp
from src.modules.admin_routes import admin_bp
from src.modules.book_module import book_bp
from src.modules.borrow_module import borrow_bp
from src.modules.search_module import search_bp

def create_app():
    app = Flask(__name__)

    # Initialize MongoDB and JWT
    init_db(app)
    init_jwt(app)

    
    app.register_blueprint(user_bp, url_prefix="/api/users")

    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    
    app.register_blueprint(book_bp, url_prefix="/api")
    app.register_blueprint(borrow_bp, url_prefix="/api/borrow")

    app.register_blueprint(search_bp, url_prefix="/api")
    
    return app

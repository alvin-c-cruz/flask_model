from flask import Flask
from .extensions import db, migrate
from .blueprints import user, disbursement


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SECRET_KEY"] = "Set secret key here"

    @app.route("/")
    def index():
        return "Hello World"
    
    app.register_blueprint(user.bp)
    app.register_blueprint(disbursement.bp)
    
    db.init_app(app)
    migrate.init_app(app=app, db=db)

    
    return app
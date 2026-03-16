from flask import Flask,flash,render_template
import os
from .extensions import login_manager,db,migrate
from .config import Config
from .auth.routes import auth_bp
from .games.routes import games_bp
from .favorites.routes import favorites_bp
from app.models.user import Anonymous

def create_app():
    app=Flask(__name__)
    app.config.from_object(Config) #Config sınıfındaki tüm değişkenleri al, uygulamanın ayarlarına yükle
    

    #extensions.py’de tanımladığın kütüphaneleri Flask uygulamasına bağlama adımı
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.anonymous_user=Anonymous
    migrate.init_app(app,db)
    
    from . import models
    
    #blueprintleri bağlama
    app.register_blueprint(auth_bp)
    app.register_blueprint(games_bp)
    app.register_blueprint(favorites_bp)

    return app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


db=SQLAlchemy()
migrate=Migrate()
login_manager=LoginManager()

login_manager.login_view="auth_bp.login" #giriş yapılmamış kullanıcılar için zorunlu yönlendirme adresini tanımlar.


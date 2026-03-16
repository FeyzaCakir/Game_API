from app.extensions import db
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from app.extensions import db, login_manager


class User(UserMixin,db.Model):
    __tablename__="users"
    user_id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(200),nullable=False,unique=True)
    email=db.Column(db.String(200),nullable=False,unique=True)
    password_hash=db.Column(db.String(200),nullable=True)
    role= db.Column(db.String(20),default="user",nullable=False)
    token_version=db.Column(db.Integer(),default=0,nullable=False)
    
    
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)
        
    def check_password(self,password):
       return check_password_hash( self.password_hash,password)
   
    def get_id(self):
        return str(self.user_id)

class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username="Guest"
        self.user_id= None
        

@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.query.get(int(user_id))

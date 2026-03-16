from app.extensions import db

class Favorite(db.Model):
    __tablename__="favorites"
    favorite_id= db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    game_id= db.Column(db.Integer,db.ForeignKey('games.game_id'),nullable=False)
    game_name=db.Column(db.String(255),nullable=True)
    game_image=db.Column(db.String(500),nullable=True)
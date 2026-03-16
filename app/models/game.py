from app.extensions import db
from datetime import datetime,timezone

class Game(db.Model):
    __tablename__="games"
    game_id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200))
    created_at= db.Column(db.DateTime, default=datetime.now(timezone.utc))
    description = db.Column(db.String(255))
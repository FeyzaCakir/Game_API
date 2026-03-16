from app.extensions import db
from app.models.game import Game
from app.models.favorite import Favorite
from flask_login import current_user


def add_favorite(game_id: int, game_name: str, game_image: str):

    existing_fav = Favorite.query.filter_by(
        user_id=current_user.user_id,
        game_id=game_id
    ).first()

    if existing_fav:
        return None

    game=Game.query.filter_by(game_id=game_id).first()
    
    if not game:
        game=Game(
            game_id=game_id,
            title=game_name,
            description=""
        )
        db.session.add(game)
        db.session.flush()
    
    new_fav = Favorite(
        user_id=current_user.user_id,
        game_id=game_id,
        game_name=game_name,
        game_image=game_image or None
    )
    db.session.add(new_fav)
    db.session.commit()
    return new_fav
    
def get_user_favorites(user_id:int):
    return Favorite.query.filter_by(user_id=user_id).all()

def del_fav(favorite_id:int):
    deleted= Favorite.query.filter_by(favorite_id=favorite_id).first()
    if deleted:
        db.session.delete(deleted)
        db.session.commit()
    return deleted
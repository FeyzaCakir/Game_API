from flask import Blueprint, render_template,jsonify
from flask_login import login_required
from .services import get_games,get_details

games_bp = Blueprint("games", __name__, template_folder="templates")

@games_bp.route("/games")
def list_games():
    data = get_games()

    games = [
        {
            "id": g["id"],
            "name": g["name"],
            "released": g.get("released"),
            "background_image": g.get("background_image")
        }
        for g in data.get("results", [])
    ]

    return render_template("games.html", games=games)

@games_bp.route("/games/<int:id>")
@login_required
def details(id):
    game=get_details(id)
    return render_template("game_detail.html",game=game)
   

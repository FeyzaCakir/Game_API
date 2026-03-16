from flask import Blueprint,request,redirect,url_for,flash,render_template,jsonify
from .services import add_favorite,get_user_favorites,del_fav
from flask import request,g
from flask_login import current_user,login_required

favorites_bp= Blueprint("favorites_bp",__name__,template_folder="templates")

@favorites_bp.route("/favorites",methods=["GET"])

def list_favorites():
    favorites = get_user_favorites(current_user.user_id)
    return render_template("favorites.html",favorites=favorites)


@favorites_bp.route("/favorites/add", methods=["POST"])
@login_required
def add():
    game_id = int(request.form.get("game_id"))
    game_name = request.form.get("game_name")
    game_image = request.form.get("game_image")

    favorite = add_favorite(
        game_id=game_id,
        game_name=game_name,
        game_image=game_image
    )
    if not favorite:
        flash("Bu oyun zaten favorilerinde.", "warning")
    else:
        flash("Oyun favorilere eklendi.", "success")

    return redirect(url_for("games.list_games"))


@favorites_bp.route("/favorites/delete",methods=["POST"])
@login_required
def delete():
    favorite_id=request.form["favorite_id"]
    deleted=del_fav(int(favorite_id))
    if deleted:
        flash("Favori başarıyla silindi")
    else:
        flash("Favori bulunamadı")
    return redirect("/favorites")


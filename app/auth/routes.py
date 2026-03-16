from flask import Blueprint,request,redirect,url_for,flash,render_template,current_app,jsonify
from flask_login import login_user,logout_user, login_required,current_user
from app.models.user import User
from app.extensions import db
from datetime import datetime,timedelta

auth_bp= Blueprint("auth_bp",__name__,template_folder="templates")

@auth_bp.route("/whoami")
def whoami():
    return f"Hello {current_user.username}"


@auth_bp.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        username=request.form.get("username")
        email=request.form.get("email")
        password= request.form.get("password")
        
        existing_user=User.query.filter_by(email=email).first()
        if existing_user:
            flash("Bu email zaten mevcut","error")
            return redirect(url_for("auth_bp.register"))
        else:
            new_user=User(username=username,email=email)
            new_user.set_password(password)
            
            db.session.add(new_user)
            db.session.commit()
        
            flash("Register is right.","success")
            return redirect(url_for("auth_bp.login")) #endpoint adı: blueprintname_functionname
    return render_template("register.html")

@auth_bp.route("/",methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form.get("email")
        password=request.form.get("password")
        
        user=User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Login is succesfull.","success")
            return redirect(url_for("games.list_games"))
        
        elif not user :
            flash("Böyle bir kullanıcı yok","error")
            return redirect(url_for("auth_bp.login"))
        elif not user.check_password(password):
            flash("Şifre yanlış","error") 
            return redirect(url_for("auth_bp.login"))  
        
    return render_template("login.html")
  

    
    
@auth_bp.route("/logout")
@login_required #çıkabilmek için giriş yapmış olman gerekir
def logout():
    logout_user()
    flash("Logout is succesfull","success")
    return redirect(url_for("auth_bp.login"))   



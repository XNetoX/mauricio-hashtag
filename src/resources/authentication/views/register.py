from flask import render_template, request, session, redirect, url_for

from config import REGISTER_TOKEN
from src.resources.authentication.services import user_service


def register():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["senha"]
        password_confirmation = request.form["confirmacao_de_senha"]
        token = request.form["token"]

        if token != REGISTER_TOKEN:
            return render_template("register.html", error_message="Token inválido!")

        if password != password_confirmation:
            return render_template(
                "register.html", error_message="Senhas diferentes, tente novamente."
            )

        user_service.create_user(email, password)
        session["email"] = email
        return redirect(url_for("home.home"))

    return render_template("register.html")

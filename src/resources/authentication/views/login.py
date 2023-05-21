from flask import redirect, render_template, request, session, url_for, flash

from src.resources.authentication.services import user_service


def login():
    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        if not user_service.check_if_user_exists(email):
            error_message="Usuário não cadastrado."
            return render_template(
                "login.html",error_message=error_message
            )

        if user_service.check_user_credentials(email, password):
            session["email"] = email
            return redirect(url_for("home.home"))
        else:
            error_message = "Credenciais inválidas. Tente novamente."
            return render_template(
                "login.html", error_message=error_message
            )

    return render_template("login.html")

from flask import redirect, render_template, request, session

from src.resources.authentication.services import user_service


def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if not user_service.check_if_user_exists(email):
            return render_template(
                "login.html", error_message="Usuário não cadastrado."
            )

        if user_service.check_user_credentials(email, password):
            session["email"] = email
            return redirect("/")
        else:
            return render_template(
                "login.html", error_message="Credenciais inválidas. Tente novamente."
            )

    return render_template("login.html")

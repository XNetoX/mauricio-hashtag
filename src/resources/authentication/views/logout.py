from flask import redirect, session, url_for



def logout():
    session.pop("email", None)
    return redirect(url_for("authentication.login"))
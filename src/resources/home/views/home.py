from flask import redirect, render_template, session, request, url_for
from src.resources.webhooks.services import webhook_services


def home():
    if "email" not in session:
        return redirect(url_for("authentication.login"))

    if request.method == "POST":
        email = request.form["email"]
        webhooks = webhook_services.get_webhooks_by_email(email)
        return render_template("home.html", webhooks=webhooks)
    else:
        webhooks = webhook_services.get_all_webhooks()
        return render_template("home.html", webhooks=webhooks)

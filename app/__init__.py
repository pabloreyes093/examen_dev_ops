from flask import Flask, render_template

def create_app():
    app = Flask(__name__, template_folder="templates")
    @app.route("/")
    def index():
        # Datos de ejemplo (puedes reemplazar por fetch a API si quieres)
        standings = [
            {"pos": 1, "team": "Barcelona SC", "pts": 45},
            {"pos": 2, "team": "Emelec", "pts": 40},
            {"pos": 3, "team": "Independiente del Valle", "pts": 36},
            {"pos": 4, "team": "Aucas", "pts": 34},
        ]
        return render_template("index.html", standings=standings)
    return app

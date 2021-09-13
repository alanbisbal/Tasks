from flask import Flask, jsonify ,render_template




def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    
    @app.route("/")
    def home():
        return render_template("home.html")
    return app
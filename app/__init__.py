from flask import Flask, render_template, request, session, flash
from flask_bcrypt import Bcrypt

#Importe de Blurprints
from app.routes.index_routes import bp_index

def application():
    app = Flask(__name__)

    #Configuración
    app.secret_key = "M&_S3cr3t_K3&"
    Bcrypt(app)

    #Registro de Blueprint
    app.register_blueprint(bp_index)

    #Ruta Metodo para verificar las URL y Redireccionar al Login
    @app.before_request
    def verificar_peticion():
        ruta = request.path
        if not 'name' in session and ruta != "/" and ruta != "/login_access" and not ruta.startswith("/static"):
            flash("Debe Iniciar Sesión","warning")
            return render_template(('login.html'))
    
    return app
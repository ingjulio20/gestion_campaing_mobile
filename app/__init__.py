from flask import Flask, render_template, request, session, flash
from flask_bcrypt import Bcrypt

#Importe de Blurprints
from app.routes.index_routes import bp_index
from app.routes.deptos_routes import bp_deptos
from app.routes.registros_routes import bp_registros

def application():
    app = Flask(__name__)

    #Configuración
    app.secret_key = "M&_S3cr3t_K3&"
    Bcrypt(app)

    #Registro de Blueprint
    app.register_blueprint(bp_index)
    app.register_blueprint(bp_deptos)
    app.register_blueprint(bp_registros)

    #Ruta Metodo para verificar las URL y Redireccionar al Login
    @app.before_request
    def verificar_peticion():
        ruta = request.path
        if not 'name' in session and ruta != "/" and ruta != "/login_access" and not ruta.startswith("/static"):
            flash("Debe Iniciar Sesión","warning")
            return render_template(('login.html'))
    
    return app
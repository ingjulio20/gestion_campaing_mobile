from flask import Flask, render_template, request, redirect, url_for
from flask_bcrypt import Bcrypt

def application():
    app = Flask(__name__)

    app.secret_key = "M&_S3cr3t_K3&"
    bcrypt = Bcrypt(app)

    return application    
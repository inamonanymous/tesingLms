from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from .routes.firstlane import Firstlane

app = Flask(__name__)
app.secret_key = "981254678"

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "password"
app.config['MYSQL_DB'] = "testinglms"

db = MySQL(app)
fl = Firstlane()

app.register_blueprint(fl.index_view)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin

app = Flask(__name__)

app.config['SECRET_KEY'] = 'socsecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

# ------------------
# DATABASE MODELS
# ------------------

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(200))
    severity = db.Column(db.String(50))
    status = db.Column(db.String(50))
    time = db.Column(db.String(50))

# ------------------
# LOGIN LOADER
# ------------------

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ------------------
# ROUTES
# ------------------

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username,password=password).first()

        if user:
            login_user(user)
            return redirect(url_for("dashboard"))

    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():

    incidents = Incident.query.all()

    return render_template("dashboard.html",incidents=incidents)


@app.route("/api/incidents")
def api_incidents():

    incidents = Incident.query.all()

    data=[]

    for i in incidents:

        data.append({
            "id":i.id,
            "type":i.type,
            "severity":i.severity,
            "status":i.status,
            "time":i.time
        })

    return jsonify(data)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask
from dotenv import load_dotenv
import os
from extensions import db, login_manager, bcrypt

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aegis.db'

db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)

from models.user import User
from routes.auth import auth

app.register_blueprint(auth)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return "<h1>The AEGIS Protocol is Running 🚀</h1>"

if __name__ == "__main__":
    app.run(debug=True)

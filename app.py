from flask import Flask, render_template, redirect, request, session, url_for
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

Session(app)
db = SQLAlchemy(app)

# User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    org_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    org_type = db.Column(db.String(50))
    password = db.Column(db.String(200), nullable=False)

@app.route("/")
def landing():
    return render_template("landing.html")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("org_name")
        user_email = request.form.get("user_email")
        type_org = request.form.get("org_type")
        pwd = request.form.get("password")

        # Check if user already exists
        existing_user = User.query.filter_by(email=user_email).first()
        if existing_user:
            return "Error: This email is already registered!"

        # Hash password
        hashed_pwd = generate_password_hash(pwd)

        # Create and save new user
        new_user = User(
            org_name=name,
            email=user_email,
            org_type=type_org,
            password=hashed_pwd
        )

        db.session.add(new_user)
        db.session.commit()
        
        return f"""
        <h1>Success!</h1>
        <p>{name} has been added to the database.</p>
        <a href="/users">View all users</a>
        """

    return render_template("sign-up.html")    

@app.route("/users")
def view_users():
    all_users = User.query.all()
    if not all_users:
        return "<h1>No users found.</h1><a href='/'>Go back</a>"
    
    user_rows = ""
    for u in all_users:
        user_rows += f"<li>ID: {u.id} | <b>{u.org_name}</b> ({u.email})</li>"
    
    return f"""
    <h1>Registered Users</h1>
    <ul>{user_rows}</ul>
    <a href="/">Add another user</a>
    """

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

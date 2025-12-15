from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///wanderlust.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# -------------------------
# Database Models
# -------------------------
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    date = db.Column(db.String(20))
    destination = db.Column(db.String(50))
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    destination = db.Column(db.String(50))
    persons = db.Column(db.Integer)
    travel_date = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    review = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    rating = db.Column(db.Integer)
    feedback = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# -------------------------
# Routes
# -------------------------
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/contact", methods=["POST"])
def contact():
    db.session.add(Contact(**request.form))
    db.session.commit()
    flash("Contact submitted successfully!")
    return redirect("/")

@app.route("/register", methods=["POST"])
def register():
    db.session.add(Registration(**request.form))
    db.session.commit()
    flash("Registration submitted successfully!")
    return redirect("/")

@app.route("/booking", methods=["POST"])
def booking():
    db.session.add(Booking(**request.form))
    db.session.commit()
    flash("Booking submitted successfully!")
    return redirect("/")

@app.route("/review", methods=["POST"])
def review():
    db.session.add(Review(**request.form))
    db.session.commit()
    flash("Review submitted successfully!")
    return redirect("/")

@app.route("/feedback", methods=["POST"])
def feedback():
    db.session.add(Feedback(**request.form))
    db.session.commit()
    flash("Feedback submitted successfully!")
    return redirect("/")

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method=="POST":
        if request.form["username"]==ADMIN_USERNAME and request.form["password"]==ADMIN_PASSWORD:
            session["admin"]=True
            return redirect("/dashboard")
        flash("Invalid Credentials")
        return redirect("/admin")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect("/admin")
    return render_template(
        "dashboard.html",
        contacts=Contact.query.all(),
        registrations=Registration.query.all(),
        bookings=Booking.query.all(),
        reviews=Review.query.all(),
        feedbacks=Feedback.query.all()
    )

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# Clear all entries
@app.route("/clear/<table>", methods=["POST"])
def clear(table):
    if not session.get("admin"):
        return redirect("/admin")
    tables = {
        "contacts": Contact,
        "registrations": Registration,
        "bookings": Booking,
        "reviews": Review,
        "feedbacks": Feedback
    }
    if table in tables:
        tables[table].query.delete()
        db.session.commit()
    return redirect("/dashboard")

# Run app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

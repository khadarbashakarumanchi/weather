#WTF Forms 

from flask import Flask, render_template
from flask_wtf import FlaskForm  # Import FlaskForm instead of Form
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "goodmorning"  # Use = for assignment

class ContactForm(FlaskForm):  # Use FlaskForm
    name = StringField("What is your name?")
    submit = SubmitField("Submit")

@app.route("/", methods=["GET", "POST"])
def index():
    contact = ContactForm()
    name = None  # Use None instead of False for uninitialized variables

    if contact.validate_on_submit():
        name = contact.name.data
        contact.name.data = ""  # Reset the form field if needed

    return render_template("index.html", contact=contact, name=name)

if __name__ == "__main__":
    app.run(debug=True)

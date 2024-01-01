from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(),Email(message="invalid email", granular_message=True, check_deliverability=False, allow_smtputf8=True, allow_empty_local=True)])
    password = PasswordField(label='Password',validators=[DataRequired(),Length(min=8, max=128, message="Min should be 8 char")])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "gururaj"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login",methods = ["get","post"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "gururajhr0305@gmail.com" and login_form.password.data == "12345678":
            return render_template("success.html")

        return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
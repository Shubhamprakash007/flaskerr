from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that no one supposed to know"

# create a form class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators = [DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    first_name = "John"
    stuff = "this is <strong>Bold</strong> text"
    favorite_pizza = ["Pepperoni","Cheese","Mushroom",41]

    return render_template("index.html",
     first_name = first_name,
     stuff=stuff,
     favorite_pizza = favorite_pizza)

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

# create custom error page
# invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# internal server error thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 40


# create name page
@app.route('/name', methods = ['GET','POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('name.html',
        name = name,
        form = form)

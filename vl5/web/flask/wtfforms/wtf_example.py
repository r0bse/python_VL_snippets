import random
import string
import json
import requests as requests

from flask import Flask, render_template, request, redirect, flash, url_for
from flask_wtf import FlaskForm
from wtforms import Form, StringField, BooleanField, validators, SelectField


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators =[validators.Length(min=4, max=25)])
    email = StringField("Email", validators =[validators.email()])
    rules_accepted = BooleanField("I accept the site rules", validators =[validators.InputRequired()])


class SelectForm(FlaskForm):
    select_field = SelectField('Label')

app = Flask(__name__) # muss vor den Annotierungen stehen!
baseUrl = "https://warnung.bund.de/api31/appdata/covid/covidrules/DE/{0}.json"


@app.route("/")
def add_user():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash("Successfully created a login request")
        return redirect('select-example')

    return render_template("registrationform.html", form = form)


@app.route("/select-example", methods=["POST"])
def select_example():
    form = SelectForm()

    with(open("static/regionKeys.json", 'r')) as file:
        unsorted = json.load(file)["daten"]
        choices = []
        for _ in sorted(unsorted, key=lambda unsorted: unsorted[1]):
            choices.append([ _[0], _[1]])
        form.select_field.choices = choices

    if form.validate_on_submit():
        return redirect(url_for('get_covid_ticker'))

    return render_template("select-example.html", form = form)



@app.route("/result", methods=["POST"])
def get_covid_ticker() -> 'html':

    selected_region_id =  request.form["select_field"]
    # Die Letzten 7 Stellen müssen dabei mit "0000000" ersetzt werden, weil die Daten nur auf Kreisebene bereitgestellt werden.
    replacementStr = '0000000'
    shortened_id = selected_region_id[:-len(replacementStr)] + replacementStr
    url = baseUrl.format(shortened_id)
    response = requests.get(url)
    json = response.json()
    headline = json["level"]["headline"]
    incicdence = json["level"]["range"]
    return render_template("result.html",
                           title=headline,
                           ticker=incicdence)

if __name__ == "__main__":

    app.config["SECRET_KEY"] = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(28))
    app.run(debug = True)


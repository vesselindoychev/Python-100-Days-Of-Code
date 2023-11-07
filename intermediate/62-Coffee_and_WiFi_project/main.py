from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, SelectField
from wtforms import validators
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap5 = Bootstrap4(app)


class CafeForm(FlaskForm):
    coffees = []
    wifi = []
    sockets = []
    for i in range(1, 6):
        coffees.append(('☕' * i, '☕' * i))
        wifi.append(('💪' * i, '💪' * i))
        sockets.append(('🔌' * i, '🔌' * i))
    coffees.append(('✘', '✘'))
    sockets.append(('✘', '✘'))
    wifi.append(('✘', '✘'))
    cafe = StringField('Cafe name', validators=[validators.DataRequired()])
    location = URLField(label='Cafe Location on Google Maps (URL)', validators=[validators.DataRequired(), validators.URL()])
    opening_time = StringField(label='Opening Time e.g. 8AM', validators=[validators.DataRequired()])
    closing_time = StringField(label='Closing Time e.g. 5:30PM', validators=[validators.DataRequired()])
    coffee_rating = SelectField(label='Coffee Rating', choices=[pair for pair in coffees])
    wifi_rating = SelectField(label='Wifi Strength Rating', choices=[pair for pair in wifi])
    power_socket_rating = SelectField(label='Power Socket Availability', choices=[pair for pair in sockets])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', mode='a', encoding='utf-8') as file:
            file.write(f"\n{form.cafe.data},{form.location.data},{form.opening_time.data},{form.closing_time.data},"
                       f"{form.coffee_rating.data},{form.wifi_rating.data},{form.power_socket_rating.data}")
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            print(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)

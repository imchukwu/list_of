from flask import Flask, jsonify, request, flash, url_for, redirect, render_template
from forms import AddSchoolForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
app.config['SECRET_KEY'] = '6956ef6ac895fac965e941548ced2b8e'

db = SQLAlchemy(app)

class schools(db.Model):
   id = db.Column('school_id', db.Integer, primary_key = True)
   name = db.Column(db.String(200))
   state = db.Column(db.String(20))  
   school_type = db.Column(db.String(20))
   description = db.Column(db.String(1000))

def __init__(self, name, state, school_type, description):
   self.name = name
   self.state = state
   self.school_type = school_type
   self.description = description

@app.route('/')
def index():
	return render_template('index.html', schools = schools.query.all())

@app.route("/add_school", methods=['GET', 'POST'])
def add_school():
    form = AddSchoolForm(state='def', school_type='def')
    if form.validate_on_submit():
        flash(f'School with name {form.name.data} added!', 'success')
        return redirect(url_for('index'))
    return render_template('add_school.html', title='Add School', form=form)


if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)

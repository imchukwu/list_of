import logging
from flask import Flask, jsonify, request, flash, url_for, redirect, render_template
from forms import AddSchoolForm
from flask_sqlalchemy import SQLAlchemy

#Logger Configuration
LOG_FORMAT = "%(levelname)s %(asctime)s - %(messages)s"
logging.basicConfig(filename = "C:\\Users\\imchu\\Documents\\Projects\\list_of\\log_data.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

logger = logging.getLogger()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///schools.sqlite3'
app.config['SECRET_KEY'] = 'secret key'

db = SQLAlchemy(app)

class schools(db.Model):
   id = db.Column('school_id', db.Integer, primary_key = True)
   name = db.Column(db.String(200))
   state = db.Column(db.String(20))  
   school_type = db.Column(db.String(20))
   description = db.Column(db.String(1000))

def __init__(self, name, state, school_type, description):
  """ Initialization method with 4 argument """
  self.name = name
  self.state = state
  self.school_type = school_type
  self.description = description

@app.route('/')
def index():
  """ Application Index Page which displays the list of schools"""
  logger.info("Displaying Index page of the application")
  logger.debug("Fetch list of schools")
  return render_template('index.html', schools = schools.query.all())

@app.route("/add_school", methods=['GET', 'POST'])
def add_school():
  """ Page to POST school information to the Web service"""
  
  logger.info("Displaying Add school page for suplying school information")
  logger.debug("Supply a schools with information")
  form = AddSchoolForm(state='def', school_type='def')
  if form.validate_on_submit():

    logger.debug("School successfully added to database")
    flash(f'School with name {form.name.data} added!', 'success')
    return redirect(url_for('index'))
  
  logger.debug("School not successfully addes to database")
  return render_template('add_school.html', title='Add School', form=form)


if __name__ == "__main__":
	db.create_all()
	app.run(debug=True)

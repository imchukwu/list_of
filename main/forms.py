from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class AddSchoolForm(FlaskForm):
    name = StringField('Name',
                           validators=[DataRequired(), Length(min=2, max=100)])

    school_type = SelectField('School Type', choices=[('def', 'Select School Type'), ('pri', 'Primary'), ('sec', 'Secondary'), ('ter', 'Tertiary')],
                        validators=[DataRequired()])

    state = SelectField('State', choices=[('def', 'Select State'), ('s1', 'Abia'), ('s2', 'Abuja'), ('s3', 'Adamawa'), ('s4', 'Akwa Ibom'), ('s5', 'Anambra'),
        ('s6', 'Bayelsa'), ('s7', 'Bauchi'), ('s8', 'Benue'), ('s9', 'Bornu'), ('s10', 'Cross River'), ('s11', 'Delta'), ('s12', 'Ebonyi'),
        ('s13', 'Edo'), ('s14', 'Ekiti'), ('s15', 'Enugu'), ('s16', 'Gombe'), ('s17', 'Imo'), ('s18', 'Jigawa'), ('s19', 'Kaduna'),
        ('s20', 'Kano'), ('s21', 'Katsina'), ('s22', 'Kebbi'), ('s23', 'Kogi'), ('s24', 'Kwara'), ('s25', 'Lagos'), ('s26', 'Nasarawa'),
        ('s27', 'Niger'), ('s28', 'Ogun'), ('s29', 'Ondo'), ('s30', 'Osun'), ('s31', 'Oyo'), ('s32', 'Plateau'), ('s33', 'Rivers'),
        ('s34', 'Sokoto'), ('s35', 'Taraba'), ('s36', 'Yobe'), ('s37', 'Zamfara')], validators=[DataRequired()])
    
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=4, max=1000)])
    
    submit = SubmitField('Add School')

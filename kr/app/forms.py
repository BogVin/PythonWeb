from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired, ValidationError, Regexp


class CreateProductForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()])
    name = StringField('Name', validators=[Length(min=3, max=25,
                                              message='This field length must be between 3 and 25 characters'),
                                              DataRequired('This field is required')])
    instock = BooleanField('I avalibel')
    number = StringField('Number', validators=[DataRequired()])
    cost = StringField('Cost', validators=[DataRequired()])
    description = StringField('Description')
    category =  SelectField(u'Category', coerce=str)
    submit = SubmitField('Add')


class UpdateProductForm(FlaskForm):
    code = StringField('Code', validators=[DataRequired()])
    name = StringField('Name', validators=[Length(min=3, max=25,
                                              message='This field length must be between 3 and 25 characters'),
                                              DataRequired('This field is required')])
    instock = BooleanField('I avalibel')
    number = StringField('Number', validators=[DataRequired()])
    cost = StringField('Cost', validators=[DataRequired()])
    description = StringField('Description')
    category =  SelectField(u'Category', coerce=str)
    submit = SubmitField('Update')



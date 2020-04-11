from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(3, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(3, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(3, 15),
                                                   Regexp('^[A-Za-z][A-Za-z_]*$', 0, 'Username must have only letters, numbers or undersocores')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='password must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_emial(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username already in use.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('OldPassword', validators=[DataRequired(), Length(3, 64)])
    new_password = PasswordField('NewPassword', validators=[DataRequired(), Length(3, 64), EqualTo('new_password2', message='newPassword must match.')])
    new_password2 = PasswordField('Confirm your NewPassword',validators=[DataRequired()])
    submit = SubmitField('Update Password')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Length(3, 64), Email()])
    submit = SubmitField('Reset Password')


class ResetPasswordForm(FlaskForm):
    new_password = PasswordField('NewPassword', validators=[DataRequired(), Length(3, 64), EqualTo('new_password2', message='password must match.')])
    new_password2 = PasswordField('Confirm Your Password')
    submit = SubmitField('Reset Password')




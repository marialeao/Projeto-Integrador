from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, IntegerField, BooleanField, SubmitField, RadioField,DecimalField,FloatField,TextAreaField
from wtforms_alchemy.fields import QuerySelectField
from wtforms.fields.html5 import DateField,TimeField
from wtforms.validators import Length, EqualTo, DataRequired,Email,NumberRange

class CadastroUsuarioForm(FlaskForm):
    nome = StringField("Nome completo",[DataRequired()])
    email = StringField("Email",[DataRequired(),Length(max=256),Email()])
    senha = PasswordField("Senha",validators=[DataRequired()])
    cadastrar = SubmitField("Cadastrar")

class LoginUsuarioForm(FlaskForm):
    email = StringField("Email",[DataRequired(),Length(max=256),Email()])
    senha = PasswordField("Senha", validators=[DataRequired(),Length(min=4,max=16)])
    login = SubmitField("Logar")
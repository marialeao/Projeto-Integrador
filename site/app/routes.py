from app import app,db,login
from flask import render_template,redirect, request, Flask
from app.forms import CadastroUsuarioForm
from app.forms import LoginUsuarioForm
from app.models import Usuario
from flask_login import login_user,logout_user
from flask_login import login_required
from app.config import Config


# @index.user_loader
# def load_user(nome_usuario):
#     return Usuario.query.get(str(nome_usuario))

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/')
def index():
    return render_template('home.html',title='Home')
@app.route('/index')
def indexa():
    return render_template('home.html',title='Home')

@app.route('/login', methods=['get','post'])
def cadastrar_usuario():
    form = CadastroUsuarioForm()
    if request.method == "POST":
        usuario = Usuario(email=form.email.data,
                          nome=form.nome.data,
                          isAdmin=False)
        usuario.set_senha(form.senha.data)
        try:
            db.session.add(usuario)
            db.session.commit()
            return redirect('/home')           
        except:
            return "Houve um erro no cadastro"    
    else: 
        return render_template("login.html",title="Cadastrar Usuario",form=form)

@app.route('/login',methods=['get','post'])
def logar_usuario():
    form = LoginUsuarioForm()
    erro = None
    if request.method == "POST":
        user = Usuario.query.filter_by(nome_usuario=form.nome_usuario.data).first()
        if user is not None:
            if user.check_password(form.senha.data):
                login_user(user)
                return redirect("/")
            else:
                erro = "Senha inválida"
        else:
            erro = "Usuário inválido"
    return render_template("login.html", title="Login", form=form, erros = erro) 


@app.route('/logout')
@login_required
def logout_usuario():
    logout_user()
    return redirect('/')
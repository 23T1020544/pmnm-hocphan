import re
from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, EqualTo, ValidationError

app = Flask(__name__)
app.secret_key = 'super_secret_key'

USERS = {
    "admin": "admin123",
    "an": "an123456"
}

class RegisterForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[
        DataRequired(message="Lỗi ở tên"),
        Length(min=4, max=20, message="Lỗi độ dài")
    ])
    email = StringField('Email', validators=[
        DataRequired(message="Lỗi ở email"),
        Regexp(r'^[^@]+@[^@]+\.[^@]+$', message="Email không đúng định dạng")
    ])
    password = PasswordField('Mật khẩu', validators=[
        DataRequired(message="Lỗi ở mật khẩu"),
        Length(min=8, message="Mật khẩu tối thiểu 8 ký tự")
    ])
    confirm_password = PasswordField('Nhập lại mật khẩu', validators=[
        DataRequired(message="Lỗi ở mật khẩu"),
        EqualTo('password', message="Mật khẩu nhập lại không khớp")
    ])
    agree = BooleanField('Đồng ý điều khoản', validators=[
        DataRequired(message="Bạn phải đồng ý với điều khoản")
    ])
    submit = SubmitField('Đăng ký')

    def validate_username(self, field):
        pattern = r'^[a-z0-9_]+$'
        if not re.match(pattern, field.data):
            raise ValidationError("Lỗi chỉ chữ thường")
        if field.data in USERS:
            raise ValidationError("Tên đăng nhập đã được sử dụng")


@app.before_request
def check_remember_me():
    if 'user' not in session and request.cookies.get('remember_user'):
        session['user'] = request.cookies.get('remember_user')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('home'))

    username_input = ''
    if request.method == 'POST':
        username_input = request.form.get('username', '')
        password = request.form.get('password', '')
        remember = request.form.get('remember')

        username = username_input.strip()

        if username in USERS and USERS[username] == password:
            session['user'] = username
            flash(f"Đăng nhập thành công. Xin chào {username}!")
            
            response = make_response(redirect(url_for('home')))
            if remember:
                response.set_cookie('remember_user', username, max_age=7*24*3600)
            return response
        else:
            flash("Sai tên đăng nhập hoặc mật khẩu.")
            return render_template('login.html', username=username_input)

    return render_template('login.html', username=username_input)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        USERS[form.username.data] = form.password.data
        flash("Đăng ký thành công")
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/profile')
def profile():
    if 'user' not in session:
        flash("Vui lòng đăng nhập..")
        return redirect(url_for('login'))
    return render_template('profile.html')

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    flash("Bạn đã đăng xuất.")
    response = make_response(redirect(url_for('login')))
    response.set_cookie('remember_user', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask,request,render_template,flash,redirect,url_for,session
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.secret_key='your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class user(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),unique=True,nullable=False)
    password=db.Column(db.String(200),nullable=True)
    email=db.Column(db.String(120),unique=True,nullable=False)

@app.route('/')
def index():
    if "user" not in session:
        return redirect(url_for('login'))

    return render_template('dashboard.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':

        username=request.form['username']
        password=request.form['password']

        user_data=user.query.filter_by(username=username).first()
    
        if user_data  and check_password_hash(user_data.password,password):
            session['user']=username
            flash("login successful!")
            return redirect(url_for('index'))
        else:
            flash("invalid username or password")
    
    return render_template('login.html')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form['username']
        password=request.form['password']
        confirm=request.form.get('confirm')
        email=request.form['email']

        existing_user=user.query.filter_by(username=username).first()

        if existing_user:
            flash("User already exits!")
        elif password != confirm:
            flash("Password doesn't match!")
        else:
            hashed_password=generate_password_hash(password)
            new_user=user(username=username,password=hashed_password,email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.")
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop("user",None)
    flash("logged out successfully")
    return redirect(url_for('login'))

if __name__=='__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



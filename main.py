from flask import Flask, render_template, request, redirect, flash, session
from passlib.hash import pbkdf2_sha256
from flask_mail import  Mail
# from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os


app = Flask(__name__)

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = "ptrever781@gmail.com",
    MAIL_PASSWORD = "Trever@gta"
)
mail = Mail(app)
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.secret_key=os.urandom(24)        #generated secret key for a session with random func of os module

conn=mysql.connector.connect(host="localhost", user="root", password="", database="capstone")
cursor=conn.cursor()


# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/capstone'
# db = SQLAlchemy(app)

# class Signup(db.Model):
#     # userid name email phone password
#     userid = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80),  nullable=False)
#     email = db.Column(db.String(20), unique=True, nullable=False)
#     phone = db.Column(db.String(20),  nullable=False)
#     password = db.Column(db.String(30), nullable=False)


param=""
@app.route('/')
def index():
    if 'user_id' in session:
        print(param)
        return render_template("index.html", user=param)
    else:
        return render_template("index.html")
    # if 'user_id' in session:    # user_id will be a key in session when user has logged in
    #     return render_template("index.html")
    # else:
    #     return redirect('/login')


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/trainers')
def trainers():
    return render_template("trainers.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/notes')
def notes():
    return render_template("Notes.html")

@app.route('/blogindex')
def blogindex():
    return render_template("blogindex.html")
@app.route('/blogcontact')
def blogcontact():
    return render_template("blogcontact.html")
@app.route('/blogpost')
def blogpost():
    return render_template("blogpost.html")
@app.route('/blogabout')
def blogabout():
    return render_template("blogabout.html")

# ************************************  Content Pages routes   **************************************************

# ************ AWS ****************
@app.route('/awshome')
def awshome():
    return render_template("awsTutorial.html")

# ************* C++ ****************
@app.route('/c++home')
def chome():
    return render_template("C++Tutorial.html")

# ************* Java ****************
@app.route('/javahome')
def javahome():
    return render_template("javaTutorial.html")

# ************* Python ****************
@app.route('/pythonhome')
def pythonhome():
    return render_template("pythonTutorial.html")

# ************* Flask ****************
@app.route('/flaskhome')
def flaskhome():
    return render_template("FlaskTutorial.html")


# ************* Angular7 ****************
@app.route('/angular7')
def angular():
    return render_template("Angular7Tutorial.html")

# ************* Block-Chain ****************
@app.route('/blockchain')
def blockchain():
    return render_template("BlockChainTutorial.html")

# ************* GIT ****************
@app.route('/git')
def git():
    return render_template("GitTutorial.html")

# ************* React JS ****************
@app.route('/reactjs')
def reactjs():
    return render_template("ReactJSTutorial.html")



    

# *************** Below routes are for Authentication Purposes:------------

@app.route('/login')
def login():
    if 'user_id' in session:
        return  redirect('/')
    else:
        return  render_template("login.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")



@app.route('/login-validation', methods=['POST'])
def login_validation():
    email=request.form.get('your_email')
    password=request.form.get('your_pass')
    # print(password)P
    # print(type(password))
    
    if len(email)==0 or len(password)==0:
        flash("Enter all the details.", 'error')
        return redirect('/login')
    else:
        cursor.execute("""SELECT * FROM `signup` WHERE `email` LIKE '{}' """.format(email))
        users=cursor.fetchall()
        # print(type(users))
        # print(users)
        if(len(users)>0):
            hash_from_db=users[0][4]
            # print(hash_from_db)
            if pbkdf2_sha256.verify(password, hash_from_db):
                session['user_id']=users[0][0]    #session is set
                flash("Login Successful. !!", 'success')
                global param
                param+=str(users[0][1])
                return redirect('/')
                # return render_template("index.html", users=users)
            else:
                flash("Invalid Credentials. Try Again !!!", 'error')
                return redirect('/login')
        else:
            flash("Invalid Credentials. Try Again !!!", 'error')
            return redirect('/login')
        # print(users)
        # return "hey bro"
        # return "Your email is {} and password is {}".format(email, password)



@app.route('/signup_user', methods=['POST', 'GET'])
def signup_user():
    # name, email, phone, pass, repass
    if(request.method=='POST'):
        # ADD entry to database.
        f_name=request.form.get('name')
        f_email=request.form.get('email')
        f_phone=request.form.get('phone')
        f_password=request.form.get('pass')
        f_re_password=request.form.get('re_pass')
        
        if len(f_name)==0 or len(f_email)==0 or len(f_phone)==0 or len(f_password)==0 or len(f_re_password)==0:
            flash("Please fill all the details.", 'error')
            return redirect('/signup')
        else:
            cursor.execute("""SELECT * FROM `signup` WHERE `email` LIKE '{}' """.format(f_email))
            users=cursor.fetchall()
            if len(users) >0:
                flash("This email is already Registered.", 'error')
                return redirect('/signup')
            else:
                if f_password != f_re_password:
                    flash("Passwords do not match.", 'error')
                    return redirect('/signup')
                elif len(f_phone) != 10 or f_phone.isdigit()==False:
                    flash(" Phone number is Invalid. ", 'error')
                    return redirect('/signup')
                else:
                    hash_pass=pbkdf2_sha256.hash(f_password)  #making hash of password for storing in database
                    cursor.execute("""INSERT INTO `signup` (`userid`, `name`, `email`, `phone`, `password`) VALUES(NULL, '{}', '{}', '{}', '{}') """.format(f_name,     f_email, f_phone, hash_pass))
                    conn.commit()
                    mail.send_message("New User Signed Up. Flask Mail",
                                        sender = f_email,
                                        recipients = ["ptrever781@gmail.com"],
                                        body = "Details of the user :- " + "\n" + "Name : "+ f_name+ "\n"+ "Email : "+f_email+"\n"+"Phone no. : "+f_phone+"\n" + "Password_hash= "+ hash_pass,
                                    )

                    flash('You are Successfully Registered.', 'success')
                    return redirect('/login')
            # return "User Successfully Registered"
        # return "Your name is {} , email is {}, password is {}, and phone is {}".format(f_name, f_email, f_password, f_phone)  



@app.route('/contact_validation', methods=['POST', 'GET'])
def contact_validation():
    # name, email, phone, pass, repass
    if(request.method=='POST'):
        u_name=request.form.get('name')
        u_email=request.form.get('email')
        u_subject=request.form.get('subject')
        u_message=request.form.get('message')
        
        if len(u_name)==0 or len(u_email)==0 or len(u_subject)==0 or len(u_message)==0:
            flash("Please fill all the details.", 'error')
            return redirect('/contact')
        else:
            # print(u_name)
            # print(u_email)
            cursor.execute("""SELECT * FROM `contacts` WHERE `Email` LIKE '{}' """.format(u_email))
            users=cursor.fetchall()
            # print(users)
            if len(users) >0:
                flash("  Email already present in contact list.", 'error')
                return redirect('/contact')
            else:
                cursor.execute("""INSERT INTO `contacts` (`id`, `Name`, `Email`, `Subject`, `Message`) VALUES(NULL, '{}', '{}', '{}', '{}') """.format(u_name,  u_email, u_subject, u_message))
                conn.commit()
                mail.send_message("New user filled the contact form. His contact details mail.",
                                        sender = u_email,
                                        recipients = ["ptrever781@gmail.com"],
                                        body = "Details of the user :- " + "\n" + "Name : "+ u_name+ "\n"+ "Email : "+u_email+"\n"+"Subject : "+u_subject+"\n"  + "Message : "+ u_message,
                                    )
                flash('Your message has been sent. Thank you!', 'success')
                return redirect('/')





@app.route('/logout')
def logout():
    session.pop('user_id')
    global param
    param=""
    flash("You have been Logged Out. !!!", 'success')
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)





# Domain name : - flexhubspot.com
# FLEX- Focoused Learning Experience 
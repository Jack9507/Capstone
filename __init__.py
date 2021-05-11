from flask import Flask, render_template, request, redirect, flash, session
from passlib.hash import pbkdf2_sha256
from flask_mail import  Mail
from datetime import datetime
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

conn=mysql.connector.connect(host="localhost", user="root", password="", database="capstone", auth_plugin='mysql_native_password')
cursor=conn.cursor()




param=""
emailg=""
passg=""
user_id=""
@app.route('/')
def index():
    if 'user_id' in session:
        # print(param)
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

@app.route('/blogindex', methods=['GET'])
def blogindex():
     cursor.execute("""SELECT * FROM `blogpost` """)
     users=cursor.fetchall()
    #  print(users[0][1])
     return render_template("blogindex.html", posts=users)

@app.route('/blogcontact')
def blogcontact():
    return render_template("blogcontact.html")

@app.route('/bcvalidation',  methods=['GET', 'POST'])
def bcvalidation():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        msg=request.form.get('msg')
        
        date=datetime.now()
        cursor.execute("""INSERT INTO `blogcontact` (`sno`, `name`, `phone`, `msg`, `date`, `email`) VALUES(NULL, '{}', '{}', '{}', '{}', '{}') """.format(name, phone, msg, date, email))
        conn.commit()
        
        flash('Your message has been sent. Thank you!', 'success')
        return redirect('/blogcontact')


@app.route('/blogdashboard')
def blogdashboard():
     cursor.execute("""SELECT * FROM `blogpost` """)
     users=cursor.fetchall()
     #  print(users[0][1])
     return render_template("blogdashboard.html", posts=users)


@app.route('/blogedit/<string:sno>', methods=['GET', 'POST'])
def blogedit(sno):
    if 'user_id' in session:
        if(request.method=='POST'):
            title=request.form.get('title')
            tagline=request.form.get('tagline')
            slug=request.form.get('slug')
            content=request.form.get('content')
            date=datetime.now()
            
            if sno=='0':
                # Adding new post
                cursor.execute("""INSERT INTO `blogpost` (`sno`, `title`, `tagline`, `slug`, `content`, `date`) VALUES(NULL, '{}', '{}', '{}', '{}', '{}') """.format(title, tagline, slug, content, date))
                conn.commit()
                flash('Add/Edit completed successfully.', 'success')
                return redirect('/blogdashboard') 
            else:
                # Edit the existing post
                cursor.execute("""SELECT * FROM `blogpost` WHERE `sno` LIKE '{}' """.format(sno))
                post=cursor.fetchall()
                cursor.execute("""UPDATE `blogpost` 
                                      SET `title`='{}',
                                          `tagline`= '{}',
                                          `slug`='{}',
                                          `content`='{}',
                                          `date`='{}'
                                      WHERE `sno`='{}' """.format(title, tagline, slug, content, date, sno))
                conn.commit()
                flash('Post Updated Successfully.', 'success')
                return redirect('/blogdashboard')

    
    if 'user_id' not in session:
        flash('You need to login first.', 'error') 
    if sno=='0':
        post=[('','','','','')] 
    else:
        cursor.execute("""SELECT * FROM `blogpost` WHERE `sno` LIKE '{}' """.format(sno))
        post=cursor.fetchall()          
    return render_template("blogedit.html", sno=sno, title=post[0][1], tagline=post[0][2], slug=post[0][3], content=post[0][4])
            

@app.route('/blogdelete/<string:sno>', methods=['GET', 'POST'])
def blogdelete(sno):
    if 'user_id' in session:
        cursor.execute("""DELETE FROM `blogpost` WHERE `sno` LIKE '{}' """.format(sno))
        flash('Post deleted successfully.', 'success') 
        return redirect('/blogdashboard')

    if 'user_id' not in session:
        flash('You need to login first.', 'error') 
    
    return redirect('/blogdashboard')




@app.route('/post/<string:post_slug>', methods=['GET', 'POST'])
def post_route(post_slug):
    cursor.execute("""SELECT * FROM `blogpost` WHERE `slug` LIKE '{}' """.format(post_slug))
    users=cursor.fetchall()
    # print(users)
    return render_template('blogpost.html',  post=users)

@app.route('/blogabout')
def blogabout():
    return render_template("blogabout.html")

@app.route('/tos')
def tos():
    return render_template("termsofservices.html")
@app.route('/privacypolicy')
def privacypolicy():
    return render_template("privacypolicy.html")



@app.route('/updateprofile')
def updateprofile():
    return render_template("updateprofile.html")

@app.route('/update_validation', methods=['GET', 'POST'])
def update_validation():
    if(request.method=='POST'):
        f2_name=request.form.get('name')
        f2_email=request.form.get('email')
        f2_designation=request.form.get('designation')
        f2_phone=request.form.get('phone')
        f2_password=request.form.get('pass')
        f2_re_password=request.form.get('re_pass')

        if len(f2_name)==0 or len(f2_email)==0 or len(f2_designation)==0 or len(f2_phone)==0 or len(f2_password)==0 or len(f2_re_password)==0:
            flash("Please fill all the details.", 'error')
            return redirect('/updateprofile')
        else:
                if f2_password != f2_re_password:
                    flash("Passwords do not match.", 'error')
                    return redirect('/updateprofile')
                elif len(f2_phone) != 10 or f2_phone.isdigit()==False:
                    flash(" Phone number is Invalid. ", 'error')
                    return redirect('/updateprofile')
                else:
                    hash_pass=pbkdf2_sha256.hash(f2_password)  #making hash of password for storing in database
                    cursor.execute("""UPDATE `signup` 
                                      SET `name`='{}',
                                          `email`= '{}',
                                          `designation`='{}',
                                          `phone`='{}',
                                          `password`='{}'
                                      WHERE `userid`='{}' """.format(f2_name, f2_email, f2_designation, f2_phone, hash_pass, user_id))
                    conn.commit()
                    flash('Profile Updated Successfully.', 'success')
                    return redirect('/updateprofile')


@app.route('/myprofile')
def myprofile():
    if 'user_id' in session:
        cursor.execute("""SELECT * FROM `signup` WHERE `email` LIKE '{}' """.format(emailg))
        users=cursor.fetchall()
        # print(users)
    if 'user_id' not in session:
        users=[('','','','','')]
    return render_template("myprofile.html", id=users[0][0], name=users[0][1], email=users[0][2], designation=users[0][3], phone=users[0][4], password=passg)




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
            hash_from_db=users[0][5]
            # print(hash_from_db)
            if pbkdf2_sha256.verify(password, hash_from_db):
                session['user_id']=users[0][0]    #session is set
                flash("Login Successful. !!", 'success')
                global param
                param+=str(users[0][1])
                global emailg
                emailg+=email
                global passg
                passg += password
                global user_id
                user_id += str(users[0][0])
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
        f_designation=request.form.get('designation')
        f_phone=request.form.get('phone')
        f_password=request.form.get('pass')
        f_re_password=request.form.get('re_pass')
        
        if len(f_name)==0 or len(f_email)==0 or len(f_designation)==0 or len(f_phone)==0 or len(f_password)==0 or len(f_re_password)==0:
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
                    cursor.execute("""INSERT INTO `signup` (`userid`, `name`, `email`, `designation`, `phone`, `password`) VALUES(NULL, '{}', '{}', '{}', '{}', '{}') """.format(f_name, f_email, f_designation, f_phone, hash_pass))
                    conn.commit()
                    mail.send_message("New User Signed Up. Flask Mail",
                                        sender = f_email,
                                        recipients = ["ptrever781@gmail.com"],
                                        body = "Details of the user :- " + "\n" + "Name : "+ f_name+ "\n"+ "Email : "+f_email + "\n" + "Designation : "+f_designation +"\n"+ "Phone no. : "+f_phone+"\n" + "Password_hash= "+ hash_pass,
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
    global emailg
    emailg=""
    global passg
    passg=""
    global user_id
    user_id=""
    flash("You have been Logged Out. !!!", 'success')
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)





# ENd of COde

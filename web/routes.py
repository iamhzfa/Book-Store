from web import app
from flask import render_template, url_for, session, redirect, flash, request
# from web.models import Item, Users
from web.forms import RegisterForm, LoginForm, sellingForm
from web import mydb
from functools import wraps
from werkzeug.utils import secure_filename
import os
import random
from werkzeug.utils import secure_filename
# import smtplib

# from flask_mail import Mail

# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = 'your@gmail.com'
# app.config['MAIL_PASSWORD'] = 'Your password'
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# mail = Mail(app)

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, *kwargs)
        else:
            return redirect(url_for('sign_in'))
    return wrap

def not_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return redirect(url_for('home'))
        else:
            return f(*args, *kwargs)
    return wrap


# @app.route('/demo')
# def demo_page():
#     items = Item.query.all()
#     return render_template('demo.html', items=items)


@app.route('/')
@app.route('/Home')
def home():
    return render_template('index.html')

@app.route('/About')
def about():
    return render_template('about.html')

@app.route('/Universities')
def University_page():
    return render_template('Universities.html')


@app.route('/Schools')
def School_page():
    return render_template('Schools.html')


@app.route('/Competitions')
def Competition_page():
    return render_template('Competitions.html')

@app.route('/Contact-Us')
def contact_us():
    return render_template('ContactUs.html')
    
@app.route('/Schools/<string:Department>')
def class12(Department):
    
    if Department == 'Science':
        db = mydb.cursor()
        db.execute(f'select * from school_books where sub_name = "physics" limit 3 ;')
        physicsData = db.fetchall()
        db.execute(f'select * from school_books where sub_name = "chemistry" limit 3 ;')
        chemistryData = db.fetchall()
        db.execute(f'select * from school_books where sub_name = "biology" limit 3 ;')
        biologyData = db.fetchall()
        db.execute(f'select *from school_books ORDER BY sub_name = "Math" DESC LIMIT 3 ;')#fetch data in reverse order by using ORDER BY table_name DESC
        mathData = db.fetchall()
        db.close()
        return render_template('Schools/Science.html', physicsData = physicsData, chemistryData = chemistryData, biologyData = biologyData, mathData = mathData)
    elif Department == 'Commerce':
        db = mydb.cursor()
        db.execute(f'select * from school_books where sub_name = "accounts" limit 3 ;')
        accountsData = db.fetchall()
        db.execute(f'select * from school_books where sub_name = "BST" limit 3 ;')
        bstData = db.fetchall()
        db.execute(f'select * from school_books where sub_name = "economics" limit 3 ;')
        economicsData = db.fetchall()
        db.execute(f'select *from school_books ORDER BY sub_name = "IP" DESC LIMIT 3 ;')#fetch data in reverse order by using ORDER BY table_name DESC
        ipData = db.fetchall()
        db.close()
        return render_template('Schools/Commerce.html', accountsData = accountsData, bstData = bstData, economicsData = economicsData, ipData = ipData)
    elif Department == 'Arts':
        db = mydb.cursor()
        db.execute(f'select * from school_books where sub_name = "history" limit 3 ;')
        historyData = db.fetchall()
        db.execute(f'select * from school_books where sub_name = "geography" limit 3 ;')
        geographyData = db.fetchall()
        db.execute(f'select * from school_books where sub_name = "PS" limit 3 ;')
        psData = db.fetchall()
        db.execute(f'select * from school_books where sub_name = "GS" limit 3 ;')#fetch data in reverse order by using ORDER BY table_name DESC
        gsData = db.fetchall()
        db.close()
        return render_template('Schools/Arts.html', historyData = historyData, geographyData = geographyData, psData = psData, gsData = gsData)
    else:
        return "<p> Page Not Found </p>"

    
@app.route('/Schools/Science/<string:sub_name>')
def scienceDepartment(sub_name):

    db = mydb.cursor()
    db.execute(f'select * from school_books where sub_name = "{ sub_name }"; ')
    data = db.fetchall()

    if sub_name == 'Physics':
        return render_template('Schools/Science/Physics.html', data=data)
    elif sub_name == 'Chemistry':
        return render_template('Schools/Science/Chemistry.html', data=data)
    elif sub_name == 'Math':
        return render_template('Schools/Science/Math.html', data=data)
    elif sub_name == 'Biology':
        return render_template('Schools/Science/Biology.html', data=data)
    else:
        return "Page not found"


@app.route('/Schools/Commerce/<string:sub_name>')
def commerceDepartment(sub_name):

    db = mydb.cursor()
    db.execute(f'select * from school_books where sub_name = "{ sub_name }"; ')
    data = db.fetchall()

    if sub_name == 'Accounts':
        return render_template('Schools/Commerce/Accounts.html', data=data)
    elif sub_name == 'Business Study' or sub_name == 'B S T' or sub_name == 'BST':
        return render_template('Schools/Commerce/businessStudy.html', data=data)
    elif sub_name == 'Economics':
        return render_template('Schools/Commerce/Economics.html', data=data)
    elif sub_name == 'Information Practice' or sub_name == 'I P' or sub_name == 'IP':
        return render_template('Schools/Commerce/infoPractice.html', data=data)
    else:
        return "Page not found"


@app.route('/Schools/Arts/<string:sub_name>')
def artsDepartment(sub_name):

    db = mydb.cursor()
    db.execute(f'select * from school_books where sub_name = "{ sub_name }"; ')
    data = db.fetchall()

    if sub_name == 'History':
        return render_template('Schools/Arts/History.html', data=data)
    elif sub_name == 'Geography':
        return render_template('Schools/Arts/Geography.html', data=data)
    elif sub_name == 'Political Science' or sub_name == 'P S' or sub_name == 'PS':
        return render_template('Schools/Arts/politicalScience.html', data=data)
    elif sub_name == 'General Study' or sub_name == 'G S' or sub_name == 'GS':
        return render_template('Schools/Arts/generalStudies.html', data=data)
    else:
        return "Page not found"


@app.route('/Sell-Book', methods=['POST','GET'])
def Sale_page():
    form = sellingForm()
    # formLog = LoginForm()
    if 'uid' in session:
        if form.validate_on_submit():

            uId = session['uid']
            uName = session['uname']   

            ## set directory where we want to save image
            imgSaveDir = os.path.join(os.path.dirname(app.instance_path), 'web\static\img')

            bookImg = form.bookImage.data
            imgName = secure_filename(bookImg.filename)

            # generating random number to make unique name
            n = random.randint(1000,1000000) 
            RandNumber = str(n)
            finalImgName = RandNumber+imgName
            # we have used \\\ three slash becuase 1 to avoid f strings escape and one to avoid database query escape
            # we have not used that url because we have faced issue to show pic by that url, so we will save name ans urlimg in
            #  database
            image = f"'\\\static\\\img\\\sellerImg\\\'{finalImgName}'"
            bookImg.save(os.path.join(imgSaveDir, 'sellerImg',finalImgName ))
       

            # db = mydb.cursor()
            # db.execute(f'select * from users where  uid = "{uId}";')
            # result = db.fetchone()
            # db.close()
            # data = result
            # uName = data[2]

            if(form.streamName.data == 'School'):
                streamName = 'school_books'
            elif(form.streamName.data == 'Universities'):
                streamName = 'Universities'
            elif(form.streamName.data == 'Competition'):
                streamName = 'Competition'
            db = mydb.cursor()   
            db.execute(f'insert into {streamName}(book_name, sub_name, class_name, mfg_year, selling_amount, publication_name, user_id, seller_name, quantity, image) values("{form.bookName.data}","{form.subjectName.data}", {form.className.data}, {form.mfgYear.data}, {form.sellingAmount.data}, "{form.publicationName.data}",{uId}, "{uName}", {form.quantity.data}, "{finalImgName}");')   
            mydb.commit()
            db.close()
            flash('Book added Successfully!','success')

            return redirect(url_for('School_page'))
        else:
            flash('Make sure you have enter correct details, like photo and Subject','danger')
            return render_template('sellBook.html', form=form)
    else:
        flash("Please Sign in first for selling books",'danger')
        return redirect(url_for('sign_in'))

@app.route('/Sign-in', methods=['POST', 'GET'])
@not_logged_in
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password_hash = form.password.data

        db = mydb.cursor()

        db.execute(f'select * from users where username = "{username}";')
        result = db.fetchone()
        db.close()

        if result:
            data = result
            password = data[4]
            uid = data[0]
            uname = data[2]

            if password == password_hash:
                session['logged_in'] = True
                session['uid'] = uid
                session['uname'] = uname
                flash('LogIn Successfully!','success')

                return redirect(url_for('home'))
            else:
                flash("Password is Incorrect !!", 'danger')
                return render_template('SignIn.html', form=form)
        else:
            flash("Username Not Found !!", 'danger')
            return render_template('SignIn.html', form=form)

    return render_template('SignIn.html', form=form)

@app.route('/Register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            db = mydb.cursor()
            db.execute(f'insert into users(name, username, email, password) values("{form.name.data}", "{form.username.data}","{form.email.data}","{form.password.data}");')
            mydb.commit()
            db.close()
            return redirect(url_for('sign_in'))
        except:
            flash("Username or Email is Exist already, Try with another one", 'danger')

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'{err_msg}', 'danger')

    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    if 'uid' in session:
        session.clear()
        flash('Logged Out Successfully!','success')
        return redirect(url_for('home'))
    return redirect(url_for('sign_in'))


    
            # name = form.name.data
            # email = form.email.data

            # message = f"Hi, {name} You are register to our website"
            # server = smtplib.SMTP("smtp.gmail.com", 587)
            # server.starttls()
            # server.login()
            # server.sendmail("huzefamd5@gmail.com", email, message)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/seller-history')
def history():
    uName = session['uname']               
    db = mydb.cursor()
    db.execute(f'select * from school_books where seller_name = "{ uName }"; ')
    data = db.fetchall()

    return render_template('history.html', data=data)

@app.route('/<string:book_id_name>')
def product(book_id_name):
    x = book_id_name.split('__')
    if len(x) > 1:
        book_id = x[0]
        book_name = x[1]
        db = mydb.cursor()
        db.execute(f'select * from school_books where book_id = "{book_id}";')
        result = db.fetchall()
        return render_template('product.html', data=result)
    
    return render_template('product.html')

@app.route('/result', methods=["GET","POST"])
def result():
    if request.method == 'POST':
        book = request.form['book']
        # search by author or book
        db = mydb.cursor()
        db.execute(f'select * from school_books where book_name like "%{book}%" or publication_name like "%{book}%";')
        schoolResult = db.fetchall()
        db.close()
        return render_template('result.html', schoolResult=schoolResult)
    return redirect(url_for('home'))
from flask import Flask, request, render_template, redirect
# import cgi

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
    return render_template('signup_form.html')


@app.route('/sign-up')
def display_signup_from():
    return render_template('signup_form.html')


@app.route('/sign-up', methods=['POST'])
def sign_up():

    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email'] 

    username_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''
    error_char_count = 'must be between 3 and 20 characters'
    error_spaces = 'must contain no spaces'
    
    if  username_error.isspace():
        username_error = 'invalid character'
        password = ''
        verify_password = ''
    elif len(username) < 3 or len(username) > 20: # len('')
        username_error = 'Must be between 3 and 20 characters'
        password = ''
        verify_password = ''

    if  password_error.isspace():
        password_error = 'invalid character no spaces'
        password = ''
        verify_password = ''
    elif len(password) < 3 or len(password) > 20:
        password_error = 'Must be between 3 and 20 characters'
        password = ''

    if verify_password != password:
        verify_password_error = 'passwords do not match'
        password_error = 'passwords do not match'
        password = ''
        verify_password = ''        

    if email: 
        if not len(email) > 2 and len(email) < 21:
           email_error = 'Email' + error_char_count
           password = ''
           verify_password = ''
           
        elif not email.count('@') >= 1:
           email_error = 'Email must contain the @ symbol'
           password = ''
           verify_password = ''
           
        elif not email.count('@') <= 1:
           email_error = 'Email must contain only one @ symbol'
           password = ''
           verify_password = ''
          
        elif not email.count('.') >= 1:
           email_error = 'Email must contain . (period)'
           password = ''
           verify_password = ''
           
        elif not email.count('.') <= 1:
           email_error = 'Email must contain only one . (period)'
           password = ''
           verify_password = ''
           
        else: 
            if ' ' in email:
               email_error = 'Email ' + error_spaces
               password = ''
               verify_password = ''

    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup_form.html', username=username, password=password, verify_password=verify_password, email=email, username_error=username_error, password_error=password_error, verify_password_error=verify_password_error, email_error=email_error)


@app.route('/welcome')
def valid_signup():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


app.run()


               
               

        
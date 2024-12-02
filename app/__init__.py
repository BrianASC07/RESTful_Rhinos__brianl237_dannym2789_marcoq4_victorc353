from flask import Flask, render_template, url_for, session, request, redirect
import os


app = Flask(__name__)

app.secret_key = os.urandom(32)
##########################################
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST': 
        type = request.form.get("type")
        if (type == "loginbutton"):
            return redirect(url_for('login'))
        elif (type == "signupbutton"):
            return redirect(url_for('signup'))
        elif (type == "logoutbutton"):
            session.pop('username')
            return redirect(url_for('home'))
        elif (type == "profilebutton"):
            return redirect(url_for('profile'))
    
    #IF LOGGED IN 
    if 'username' in session:
        return render_template('home.html', loggedin=True)
    return render_template('home.html', loggedin=False)
##########################################
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        type = request.form.get("type")
        #LOGIN BUTTON
        if (type == "loginenter"):
            #DB STUFF HERE
            if (True): 
                session['username'] = ""
                return redirect(url_for('home'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))
        
    #IF LOGGED IN 
    if 'username' in session:
        redirect(url_for('home'))
    return render_template('login.html')
##########################################
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    #IF LOGGED IN 
    if 'username' in session:
        redirect(url_for('home'))
    if request.method == 'POST':
        type = request.form.get("type")
        #SIGN UP BUTTON
        if (type == "signupenter"):
            #DB STUFF HERE
            if (True): 
                session['username'] = ""
                return redirect(url_for('home'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))
    return render_template('signup.html')
##########################################
@app.route("/profile", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST': 
        type = request.form.get("type")
        if (type == "prefsbutton"):
            return redirect(url_for('prefs'))
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))
    return render_template('profile.html')
##########################################
@app.route("/preferences", methods=['GET', 'POST'])
def prefs():
    if request.method == 'POST': 
        type = request.form.get("type")
        #RETURN BACK HOME BUTTON
        if (type == "returnhome"):
            return redirect(url_for('home'))
    return render_template('prefs.html')
##########################################
if __name__ == "__main__":
    app.debug = True
    app.run()
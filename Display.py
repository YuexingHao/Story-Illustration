from flask import Flask, render_template, flash, request, session, url_for
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField
from flask_bootstrap import Bootstrap

# App config.
DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
 

@app.route("/submit")
def submit():
    
    
    f = open('url.txt','r')
    if f.mode=='r':
        x=f.read()
        print(x)
        flash('Here is your picture links below: ' + x)
        
        
    return render_template('submit.html')
    

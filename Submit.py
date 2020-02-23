from flask import Flask, render_template, flash, request, session, url_for
from wtforms import Form, TextField, TextAreaField, StringField, SubmitField
from flask_bootstrap import Bootstrap

# App config.
DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'SuperSecretKey'
 
class NameForm(Form):
    name = TextField('Please insert your stories here. (At most five sentences!):')
 
    
@app.route("/text", methods = ['GET', 'POST'])
def textupload():
    form = NameForm(request.form)
    print (form.errors)
 
    if request.method == 'GET':
        
        file = open('url.txt','r')
        if file.mode=='r':
        x=file.read()
        print(x)
        return('Here is your picture links below: ' + x)
         
        flash('Here is your story below: ' + name)

    return render_template('submit.html', form=form)

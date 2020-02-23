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
 
    
@app.route('/home')
def Story():
    return render_template('Story.html')    

@app.route("/text", methods = ['GET', 'POST'])
def textupload():
    form = NameForm(request.form)
    print (form.errors)
 
    if request.method == 'POST':
        name=request.form['name']
        print (name)
        
        thefile = open('story.txt', 'w')
        n = thefile.write(name)
        thefile.close()
         
        flash('Here is your story below: ' + name)

    return render_template('textupload.html', form=form)


    
@app.route("/image")
def image():
    return render_template('imageupload.html')

@app.route("/submit")
def submit():
    
    
    f = open('url.txt','r')
    if f.mode=='r':
        x=f.read()
        print(x)
        return('Here is your picture links below:  ' + x)
        
        
    '''return render_template('submit.html')'''
    
    
@app.route("/feedback")
def feedback():
    return render_template('feedback.html')
    
'''
def index():
    return redirect(url_for('.submit'))

@app.route("/submit")
def submit():
    return render_template('submit.html')

if __name__== '__main__':
   app.run(debug=True)

def placeholder_display(name):
    
    return render_template('submit.html', form=form) 
    
    'We are working on it! Please visit later.. - Here is your story: ' + name

    output_string = placeholder_display(name)
'''



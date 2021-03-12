
from flask import render_template
from . import main

   

# your views go here i.e for home,about
@main.route("/")
@main.route('/home')
def homepage():
    return render_template('home.html',title=home)




if __name__=='__main__':
    app.run(debug=True)


from flask import render_template
from . import main

   

# your views go here i.e for home,about
@main.route("/")
@main.route('/home')
def homepage():
    return render_template('home.html',title=home)




<<<<<<< HEAD
if __name__=='__main__':
    app.run(debug=True)
=======
@main.route("/about")
def about():
    return render_template("about.html")

>>>>>>> ba86ec7ade79a936b81e04ee8b80a97cf8f97770

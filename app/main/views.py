
from flask import render_template
from . import main

   

# your views go here i.e for home,about
@main.route("/")
<<<<<<< HEAD
def index():
    return render_template('menu.html')
    
=======
@main.route('/home')
def homepage():
    return render_template('home.html',title=home)

>>>>>>> c6210a6f03e451f1b89fc05be33219256516393a



<<<<<<< HEAD
if __name__=='__main__':
    app.run(debug=True)
=======
@main.route("/about")
def about():
<<<<<<< HEAD
    pass

@main.route("/footer")
def footer():
    pass
    return render_templates('footer.html')
=======
    return render_template("about.html")

>>>>>>> ba86ec7ade79a936b81e04ee8b80a97cf8f97770
>>>>>>> c6210a6f03e451f1b89fc05be33219256516393a

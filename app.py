"""What We've done so far"""
"""
1. Created a virtual environment with venv "python -m venv venv
    - This create a venv folder containing a copy of python and pip for just this project
    -Note: pip is python's package installer (for external libraries)
2. Actived the virtual environment with "./venv/Scripts/activate"
    - This should put (venv) at the front of the command line
3. Installed flask with "pip install flask"

4. Created templates in a templates folder to return thml pages
5. Rendered the templates with render_templates()
6. Created a requirements.txt file that will let you or others easily install packages the app needs
    -Created with: pip freeze > requirements.txt
    -Can be run with pip install -r requirements.txt
7. Added a .gitignore to make sure we don't commit our venv stuff
8. Created static folder to be used to server other local resources (css/js/images)
    -used url_for() to load static asserts in html pages.
"""

#import the Flask class from the flask module
from flask import Flask, render_templates # render_templates loads HTML 
import datetime

#Create an instance of the Flask app
app=Flask(__name__)

#Define the route for a home page
@app.route("/")
def home():
    #Return a single string that is valid HTML
    #return "<h1>Welcome to my Flask App!</h>"
    return render_templates("home.html")

@app.route("/time")
def time():
    #get the current time on the server
    now= datetime.datetime.now()
    #return f"<h2>Current Server Time: {now}</h2>"

    return render_templates("time.html", current_time=now)

if __name__ == "__main__":
    app.run(debug=True) # debug = True enables automatic reload on changes and better error messages
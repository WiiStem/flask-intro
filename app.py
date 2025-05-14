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
# # render_templates loads HTML 
from flask import Flask,render_template, request
import datetime
import requests


#Create an instance of the Flask app
app=Flask(__name__)

#Define the route for a home page
@app.route("/")
def home():
    #Return a single string that is valid HTML
    #return "<h1>Welcome to my Flask App!</h>"
    return render_template("home.html")

@app.route("/time")
def time():
    #get the current time on the server
    now= datetime.datetime.now()
    #return f"<h2>Current Server Time: {now}</h2>"

    return render_template("time.html", current_time=now)

@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        ssn = request.form.get('snn')
        return render_template("greeting.html", name=name, ssn=ssn)

    return render_template("form.html")

@app.route("/catfact")
def catfact():
    response = requests.get("https://catfact.ninja/fact")
    if response.status_code == 200: # we successfully got a response
        data = response.json()
        fact = data["fact"]
    else:
        fact = "Could not fetch a cat fact right now. Try again later."

    picresp = requests.get("https://cataas.com/cat?json=true")
    if picresp.status_code == 200: # we successfully got a response
        picdata = picresp.json()
        pic = picdata["url"]
    else:
        pic = "/images/404.png"

    return render_template("catfact.html", cat_fact=fact, cat_img=pic)
    
    


@app.route("/math")
def math():
    return render_template("math.html")

@app.route("/math_result", methods=['POST'])
def solve():
    num = request.form.get('num')
    num_2 = request.form.get('num_2')
    operation=request.form.get('operation')
    answer = eval(f"{num} {operation} {num_2}")
    return render_template("math_result.html",num=num, operation=operation, num_2=num_2, answer=answer)

if __name__ == "__main__":
    app.run(debug=True) # debug = True enables automatic reload on changes and better error messages
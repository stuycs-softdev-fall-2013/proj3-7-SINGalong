from flask import Flask
from flask import render_template, session, request, redirect, url_for

app = Flask(__name__)
app.secret_key = "SINGalong"
_loggedin = False

@app.route('/',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("Login.html")
    if request.method == "POST":
        #checking login stuff
        return redirect(url_for("home"));


@app.route("/home", methods = ["POST","GET"])
def home():
    if request.method == "GET":
        return render_template('Home.html')
    if request.method == "POST":
        
    
    
	
	
@app.route('/AboutUs')
def AboutUs():
    return render_template('AboutUs.html')

if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)

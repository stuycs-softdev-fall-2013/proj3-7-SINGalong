
from flask import Flask
from flask import render_template, session, request, redirect, url_for
import members

app = Flask(__name__)
app.secret_key = "SINGalong"
_loggedin = False
_link = ""

@app.route('/',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("Login.html")
    if request.method == "POST":
        #checking login stuff
        return redirect(url_for("/AboutUs"));
		
@app.route('/Home', methods = ["POST", "GET"])
def Home():
    if request.method == "GET":
        return render_template('Home.html')

@app.route('/AboutUs', methods = ["POST", "GET"])
def AboutUs():
    if request.method == "GET":
        return render_template('AboutUs.html')

@app.route('/Contact', methods = ["POST", "GET"])
def Contact():
	if request.method == "GET":
		return render_template('Contact.html')

@app.route('/Crews', methods = ["POST", "GET"])
def Rules():
	if request.method == "GET":
		return render_template('Crews.html')

@app.route('/Calendar', methods = ["POST", "GET"])
def Calendar():
	if request.method == "GET":
		return render_template('Calendar.html')

@app.route('/Belly', methods = ["POST", "GET"])
def Belly():
	if request.method == "GET":
		return render_template('belly.html')		

@app.route('/Boyshiphop', methods = ["POST", "GET"])
def BoysHH():
	if request.method == "GET":
		return render_template('boyshiphop.html')

@app.route('/Contemporary', methods = ["POST", "GET"])
def Contemp():
	if request.method == "GET":
		return render_template('contemp.html')

@app.route('/Girlshiphop', methods = ["POST", "GET"])
def Girlshiphop():
	if request.method == "GET":
		return render_template('girlshiphop.html')		

@app.route('/Step', methods = ["POST", "GET"])
def Step():
	if request.method == "GET":
		return render_template('step.html')
		
@app.route('/Latin', methods = ["POST", "GET"])
def Latin():
	if request.method == "GET":
		return render_template('latin.html')

@app.route('/Rave', methods = ["POST", "GET"])
def Rave():
	if request.method == "GET":
		return render_template('rave.html')

@app.route('/Props', methods = ["POST", "GET"])
def Props():
	if request.method == "GET":
		return render_template('props.html')

@app.route('/Cast', methods = ["POST", "GET"])
def Cast():
	if request.method == "GET":
		return render_template('cast.html')

@app.route('/Costumes', methods = ["POST", "GET"])
def Costumes():
	if request.method == "GET":
		return render_template('costumes.html')
        if request.method == "POST":
            if request.form['btn']:
                global _link
                _link = request.form['btn']
                return redirect(url_for("members"))


@app.route('/Band', methods = ["POST", "GET"])
def Band():
	if request.method == "GET":
		return render_template('band.html')

@app.route('/Art', methods = ["POST", "GET"])
def Art():
	if request.method == "GET":
		return render_template('art.html')

@app.route('/Tech', methods = ["POST", "GET"])
def Tech():
	if request.method == "GET":
		return render_template('tech.html')

@app.route('/SoundandLights', methods = ["POST", "GET"])
def SoundLights():
	if request.method == "GET":
		return render_template('soundlights.html')

@app.route('/Chorus', methods = ["POST", "GET"])
def Chorus():
	if request.method == "GET":
		return render_template('chorus.html')


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)

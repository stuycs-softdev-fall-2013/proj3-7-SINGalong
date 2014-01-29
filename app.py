
from flask import Flask
from flask import render_template, session, request, redirect, url_for
from pymongo import MongoClient
from members import addMember, getMembers
from director import addDirector
from news import addPost
from videos import getURLs, addURL

app = Flask(__name__)
app.secret_key = "SINGalong"

client = MongoClient()
db = client['members']
members = db['members']

member = ""
director = ""
crew = ""
post = ""

@app.route('/',methods=["POST","GET"])
def login():
    if request.method == "GET":
        return render_template("Login.html")
    if request.method == "POST":
        return redirect(url_for("/Home"));
		
@app.route('/Home', methods = ["POST", "GET"])
def Home():
    if request.method == "GET":
        return render_template('Home.html')
    if request.method == "POST":
        if "addnewpost" in request.form:
            post = str(request.form['newpost'])
            addPost(post)
            return render_template('Home.html', posts = post)

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
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('belly.html', member = getMembers("Belly"), director = getDirectors("Belly"))		

@app.route('/Boyshiphop', methods = ["POST", "GET"])
def BoysHH():
	if request.method == "GET":
		return render_template('boyshiphop.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('boyshiphop.html', member = getMembers("BoysHH"), director = getDirectors("BoysHH"))		


@app.route('/Contemporary', methods = ["POST", "GET"])
def Contemp():
	if request.method == "GET":
		return render_template('contemp.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            elif "ad" in request.form: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            elif "av" in request.form:
                url = request.form['vid']
                addURL(url)
            else:
                return render_template('contemp.html')
            return render_template('contemp.html', member = getMembers("Contemp"), director = getDirectors("Contemp"), vid = getURLs("Contemp"))		


@app.route('/Girlshiphop', methods = ["POST", "GET"])
def Girlshiphop():
	if request.method == "GET":
		return render_template('girlshiphop.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('girlshiphop.html', member = getMembers("Girlshiphop"), director = getDirectors("Girlshiphop"))		

@app.route('/Step', methods = ["POST", "GET"])
def Step():
	if request.method == "GET":
		return render_template('step.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('step.html', member = getMembers("Step"), director = getDirectors("Step"))		

		
@app.route('/Latin', methods = ["POST", "GET"])
def Latin():
	if request.method == "GET":
		return render_template('latin.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('latin.html', member = getMembers("Latin"), director = getDirectors("Latin"))		

@app.route('/Rave', methods = ["POST", "GET"])
def Rave():
	if request.method == "GET":
		return render_template('rave.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('rave.html', member = getMembers("Rave"), director = getDirectors("Rave"))		


@app.route('/Props', methods = ["POST", "GET"])
def Props():
	if request.method == "GET":
		return render_template('props.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('props.html', member = getMembers("Props"), director = getDirectors("Props"))		


@app.route('/Cast', methods = ["POST", "GET"])
def Cast():
	if request.method == "GET":
		return render_template('cast.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('cast.html', member = getMembers("Cast"), director = getDirectors("Cast"))		


@app.route('/Costumes', methods = ["POST", "GET"])
def Costumes():
	if request.method == "GET":
		return render_template('costumes.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member, "Costumes")
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('costumes.html', member = getMembers("Costumes"), director = getDirectors("Costumes"))


@app.route('/Band', methods = ["POST", "GET"])
def Band():
	if request.method == "GET":
		return render_template('band.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('band.html', member = getMembers("Band"), director = getDirectors("Band"))		


@app.route('/Art', methods = ["POST", "GET"])
def Art():
	if request.method == "GET":
		return render_template('art.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('art.html', member = getMembers("Art"), director = getDirectors("Art"))		


@app.route('/Tech', methods = ["POST", "GET"])
def Tech():
	if request.method == "GET":
		return render_template('tech.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('tech.html', member = getMembers("Tech"), director = getDirectors("Tech"))		


@app.route('/SoundandLights', methods = ["POST", "GET"])
def SoundLights():
	if request.method == "GET":
		return render_template('soundlights.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('soundlights.html', member = getMembers("SoundLights"), director = getDirectors("SoundLights"))		


@app.route('/Chorus', methods = ["POST", "GET"])
def Chorus():
	if request.method == "GET":
		return render_template('chorus.html')
        if request.method == "POST":
            if "am" in request.form:
                member = str(request.form["member"])
                print member
                addMember(member)
            else: 
                director = str(request.form["director"])
                print director 
                addDirector(director)
            return render_template('chorus.html', member = getMembers("Chorus"), director = getDirectors("Chorus"))		


if __name__=="__main__":
    app.debug=True
    app.run(host='0.0.0.0',port=7004)

from flask import Flask, render_template
app = Flask("__name__")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/caska")
def SobreCaska():
    return render_template("caska.html")

@app.route("/guts")
def SobreGuts():
    return render_template("guts.html")

@app.route("/griffth")
def SobreGriffth():
    return render_template("griffth.html")
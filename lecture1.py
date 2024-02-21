from flask import Flask , redirect , url_for

app = Flask(__name__) 

@app.route("/") 

def home():
    return "<h1> welcome hello world  </h1>"  

@app.route("/courses") 
def courses():
    return "welcome to home"

@app.route("/<name>")
def name(name):
    return f"Hello{name}" 

@app.route("/admin")
def admin():
    return redirect("/")

if __name__ == "__main__": 
    app.run(debug = True)
    
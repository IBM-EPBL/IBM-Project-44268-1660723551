from flask import Flask,render_template
app=Flask(__name__)
@app.route("/index")
def indexpage():
 return render_template('index.html')
@app.route("/signin")
def signinpage():
  return render_template('signin.html')
@app.route("/signup")
def signuppage():
 return render_template('signup.html')
if __name__=="__main__":
 app.run(debug=True)

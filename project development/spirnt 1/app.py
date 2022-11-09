from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route("/loginpage")
def loginpage():
  return render_template('loginpage.html')

@app.route("/about")
def about():
  return render_template('about.html')

@app.route("/content")
def content():
  return render_template('content.html')
  
if __name__=="__main__":
  app.run(debug=True)
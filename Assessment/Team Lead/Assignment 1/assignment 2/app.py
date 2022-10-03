from cgitb import reset
from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

app = Flask(__name__)
app.secret_key = 'fasdgfdgdfg'


@app.route('/')
def home():
   return render_template('home.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route('/signinp')
def signin():
   return render_template('signin.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         name = request.form['name']
         email = request.form['email']
         password = request.form['password']
        
         
         with sql.connect("signup_database.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,email,password) VALUES (?,?,?,?)",(name,email,password) )
            con.commit()
            msg = "Record successfully added!"
      except:
         con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("list.html",msg = msg)
         con.close()

@app.route('/list')
def list():
   con = sql.connect("signup_database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from signup")
   
   signup = cur.fetchall();
   return render_template("list.html", signup = signup)

if __name__ == '__main__':
   app.run(debug = True)

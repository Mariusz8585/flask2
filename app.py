from flask import Flask, render_template, request
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/mainpage/me")
def hello():
     return render_template("mainpage.html")

@app.route("/mypage/contact", methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("mypage.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")























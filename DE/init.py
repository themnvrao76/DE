from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import requests
from pprint import pprint

mylist=[]
data=requests.get(f"https://www.googleapis.com/books/v1/volumes?q=elonmusk&key=AIzaSyB_j2rH8EflxsWIqnak3Jq4qZfbSooypNo")
new=data.json()
for i in range(10):
    mylist.append([{'title':new['items'][i]['volumeInfo']['title'],'img':new['items'][i]['volumeInfo']['imageLinks']["thumbnail"]}])

newlist=mylist

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/books'

db = SQLAlchemy(app)
class Contect(db.Model):
    SNO = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), nullable=False)
    PH_NO = db.Column(db.String(12), nullable=False)
    MSG = db.Column(db.String(120), nullable=False)
   
    Gmail = db.Column(db.String(20), nullable=False)

class Books(db.Model):
    SNO = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(21), nullable=False)
    img_file = db.Column(db.String(80), nullable=False)
    Title = db.Column(db.String(21), nullable=False)
    Author = db.Column(db.String(120), nullable=False)
    Price = db.Column(db.Integer, nullable=True)
@app.route("/home",methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        v=request.form.get("mysearch")
        print(v)
        mylist.clear()
        try:
            data=requests.get(f"https://www.googleapis.com/books/v1/volumes?q={v}&key=AIzaSyB_j2rH8EflxsWIqnak3Jq4qZfbSooypNo")
            new=data.json()
            for i in range(10):
                mylist.append([{'title':new['items'][i]['volumeInfo']['title'],'img':new['items'][i]['volumeInfo']['imageLinks']["thumbnail"]}])
            return render_template("index.html",data=mylist)
            
        except Exception as e:
            print(e)
            return render_template('error.html')
    else:
        return render_template("index.html",data=newlist)


            
            

    

@app.route("/")
def new():
    return render_template("welcome.html")



@app.route("/about")

def about():
    return render_template("about.html")

@app.route("/login")

def login():
    return render_template("login.html")

@app.route("/contect",methods=['GET','POST'])

def contect():
    if (request.method=='POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contect(Name=name, PH_NO = phone, MSG = message, Gmail = email )
        db.session.add(entry)
        db.session.commit()
    return render_template("contect.html")


@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Books.query.filter_by(slug=post_slug).first()
    print(post)
    return render_template('post.html', post=post)


app.run(debug=True)
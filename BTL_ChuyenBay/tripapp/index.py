from flask import Flask, render_template, request
import os
from tripapp import app
from tripapp.admin import *
app = Flask(__name__)

@app.route("/")
def home():
    users = [{
        "name": "Nguyen Van A",
        "email": "a@gmail.com"
    }, {
        "name": "Tran Van B",
        "email": "b@gmail.com"
    }, {
        "name": "Le Van C",
        "email": "c@gmail.com"
    }]
#Tim Kiem tu khoa:
    key = request.args.get("keyword")
    if key:
        users = [u for u in users if u ['name'].lower().find(key.lower()) >= 0]

    return render_template('index.html', users=users)

#Dang nhap:
@app.route("/login", methods=['post'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == '123':
        return 'thanh cong'
    return 'loi'
#Dua hinh anh vao
@app.route('/upload', methods = ['post'])
def up():
    i = request.files['avatar']
    i.save(os.path.join('', app.root_path , 'static/uploadimages/' , i.filename))

    return 'Upload thành công.'
#Path params
@app.route("/hello/<name>")
def hello(name):
    return render_template('index.html', message = "Xin chao %s!!!" % name)

def hello2():
    fname = request.args.get('first_name', 'A')
    lname = request.args.get('last_name', 'B')

    return render_template('index.html', message = 'Chao mung %s %s!!!' % (fname, lname))

if __name__ == "__main__":
    app.run(debug=True)

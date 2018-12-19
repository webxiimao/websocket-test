#-*- coding=utf8 -*-
'''
write by xii
'''
from flask import render_template,url_for,Blueprint,session,redirect,request


main = Blueprint('main',__name__)


@main.route('/')
def enter():
    return redirect(url_for('main.login'))#重定向到login页面



@main.route('/index')
def index():
    return render_template('index.html', title='聊天实验室')



@main.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        session['nickname'] = request.form['nickname']
        return redirect(url_for('main.index'))
    return render_template('login.html',title='chatroom login')
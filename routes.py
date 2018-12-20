#-*- coding=utf8 -*-
'''
write by xii
'''
from flask import render_template,url_for,Blueprint,session,redirect,request
from config import Config


main = Blueprint('main',__name__)


@main.route('/')
def enter():
    return redirect(url_for('main.login'))#重定向到login页面



@main.route('/index')
def index():
    if 'nickname' in session:
        #只有存在session的情况下才能进入聊天室
        return render_template('index.html', title='聊天实验室' ,rooms=Config.PUBLIC_ROOMS)
    return redirect(url_for('main.login'))



@main.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        nickname = request.form['nickname']
        if nickname:
            session['nickname'] = nickname
            return redirect(url_for('main.index'))
        else:
            return render_template('login.html',title='chatroom login',error="昵称不能为空")
    return render_template('login.html',title='chatroom login')
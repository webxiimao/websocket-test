#-*- coding=utf8 -*-
'''
write by xii
'''
from flask_socketio import SocketIO,emit,namespace
from flask import session,request

socketio = SocketIO()


@socketio.on('connect')
def handle_connect():
    socketio.emit('client_connect',{'data':session['nickname']})


@socketio.on('msg submit')
def handle_request_msg(msg):
    socketio.emit('get_res',{'data':{'msg':msg['data'],'name':session['nickname']}})


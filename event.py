#-*- coding=utf8 -*-
'''
write by xii
'''
from flask_socketio import SocketIO,emit,namespace,join_room,leave_room
from flask import session,request

socketio = SocketIO()


# @socketio.on('connect')
# def handle_connect():
#     socketio.emit('client_connect',{'data':session['nickname']})
#

@socketio.on('join room')
def handle_room_join(data):
    room = data['room']
    join_room(room)
    session['room'] = room
    d = {
        'data':session['nickname']
    }
    socketio.emit('client_connect', d ,room=room)


@socketio.on('leave room')
def handle_room_leave(data):
    print('leave room')
    room = session['room']
    leave_room(room)
    d = {
        'data': session['nickname']
    }
    socketio.emit('leave_room',d,room=room)


@socketio.on('msg submit')
def handle_request_msg(msg):
    d = {
        'data':{
            'msg':msg['data'],
            'name':session['nickname']
        }
    }
    socketio.emit('get_res',d, room=session['room'])




#coding=utf-8
import itchat
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

KEY = '225ee83379c7461eb212e7169eb1ff00'

def get_response(msg):
	apiUrl = 'http://www.tuling123.com/openapi/api'
	data = {
		'key' : KEY,
		'info' : msg,
		'userid' : 'ezio',
	}
	try:
		r = requests.post(apiUrl, data = data).json()
		return r.get('text')
	except:
		return
@itchat.msg_register(itchat.content.TEXT,isGroupChat = False)
def tuling_reply(msg):
	print(msg['Text'])
	print(msg['FromUserName'])
	print itchat.search_friends(userName=msg['FromUserName'])   #详细信
	print itchat.search_friends(userName=msg['FromUserName'])['NickName']   #获取昵称
	name = itchat.search_friends(userName=msg['FromUserName'])['NickName']
	if name == '碳化' :
		defaultReply = '碳小化: Not working now!'
		reply = '碳小化: ' + get_response(msg['Text'])
		print(reply)
		return reply or defaultReply
	else :
		return
itchat.auto_login(hotReload=True)
itchat.run()

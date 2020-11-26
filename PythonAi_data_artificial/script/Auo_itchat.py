# Python自动化发送微信消息
# 自动化办公体系 搭建
import  itchat
itchat.auto_login(enableCmdQR=False,hotReload=True)
to_name=itchat.search_friends(name='@----刈-carzy')
itchat.send_msg('ceshi',toUserName=to_name)
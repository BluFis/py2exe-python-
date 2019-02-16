# -*- coding: utf-8 -*-
from urllib import urlencode
import sitecustomize

print unicode('url编码工具 python2.7\n','utf-8')
url=raw_input(unicode('请输入url:\n','utf-8').encode('gbk'))
def get_param_count():
    index = raw_input(unicode('请输入参数的个数：\n','utf-8').encode('gbk'))
    if(int(index)<=0):
        print unicode('非法个数，请重新输入！\n','utf-8')
        get_param_count()
    return int(index)
index = get_param_count()
para_dic={}
k=1
while (k<=index):
    key=raw_input(unicode('请输入第%d个参数名：\n' %(k),'utf-8').encode('gbk'))
    value = raw_input(unicode('请输入第%d个参数值：\n' % (k),'utf-8').encode('gbk'))
    if(key==''):
        print unicode('参数错误，请重新输入\n','utf-8')
        continue
    para_dic[key]=value
    k=k+1

url_data = urlencode(para_dic)
if(url_data==''):
    print unicode('url编码结果为:%s\n' %(url),'utf-8')
else:
    if (url[:-1] != '?'):
        url = url + '?'
    print unicode('url编码结果为:%s\n' % (url+url_data),'utf-8')

# -*- coding: utf-8 -*-
from urllib import urlencode
import sitecustomize

print ('url编码工具 python2.7\n')
url=raw_input('请输入url:\n')
def get_param_count():
    index = raw_input('请输入参数的个数：\n')
    if(int(index)<=0):
        print ('非法个数，请重新输入！\n')
        get_param_count()
    return int(index)
index = get_param_count()
para_dic={}
k=1
while (k<=index):
    key=raw_input('请输入第%d个参数名：\n' %(k))
    value = raw_input('请输入第%d个参数值：\n' % (k))
    if(key==''):
        print ('参数错误，请重新输入\n')
        continue
    para_dic[key]=value
    k=k+1

url_data = urlencode(para_dic)
if(url_data==''):
    print ('url编码结果为:%s\n' %(url))
else:
    if (url[:-1] != '?'):
        url = url + '?'
    print ('url编码结果为:%s\n' % (url+url_data))

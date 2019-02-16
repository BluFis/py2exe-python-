# -*- coding: utf-8 -*-
import Tkinter as tk
from urllib import urlencode


class paramEntry(tk.Entry):
    def __init__(self,parent,tag):
        tk.Entry.__init__(self,parent)
        self.tag = tag


class paramFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.row_num=0
        self.param_dic={}

    def insert_row(self):
        param_label1_1 = tk.Label(self, text='请输入参数名：')
        param_label1_1.grid(column=0, row=self.row_num)
        param_text1_1 = paramEntry(self,'key'+str(self.row_num))
        param_text1_1.grid(column=1, row=self.row_num)
        param_label1_2 = tk.Label(self, text='请输入参数值：')
        param_label1_2.grid(column=2, row=self.row_num)
        param_text1_2 = paramEntry(self,'value'+str(self.row_num))
        param_text1_2.grid(column=3, row=self.row_num)
        self.param_dic['key'+str(self.row_num)]=param_text1_1
        self.param_dic['value' + str(self.row_num)] = param_text1_2

class mainView(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.url_label = tk.Label(self, text='请输入url:').grid(column=0, row=0,padx=5,pady=5)
        self.url_text = tk.Entry(self,width=55)
        self.url_text.grid(column=1, row=0, columnspan=2,pady=5)
        self.url_add_btn = tk.Button(self, text='+', width=2,height=1,command=self.insert_row).grid(column=4, row=0)
        self.param_Frame = paramFrame(self)
        self.param_Frame.grid(column=0, row=1, columnspan=5,padx=5,pady=5)
        self.param_Frame.insert_row()
        self.active_btn = tk.Button(self, text='url编码', command=self.active_url).grid(column=0, row=2,padx=5,pady=5)
        self.active_text = tk.StringVar()
        self.active_Entry = tk.Entry(self, textvariable=self.active_text,justify=tk.LEFT,width=56)
        self.active_Entry.grid(column=1, row=2,columnspan=4)

    def insert_row(self):
        self.param_Frame.row_num=self.param_Frame.row_num+1
        self.param_Frame.insert_row()

    def active_url(self):
        key,value='',''
        url_param=dict()
        for index in range(0,int(len(self.param_Frame.param_dic)/2)):
            key = self.param_Frame.param_dic['key'+str(index)].get()
            if key == '':
                break
            value = self.param_Frame.param_dic['value'+str(index)].get()
            url_param[key]=value
        url_data = urlencode(url_param)
        url = self.url_text.get()
        if(url_data==''):
            self.active_text.set(url)
        else:
            if (url[:-1] != '?'):
                url = url + '?'
            self.active_text.set(url+url_data)


Tk=tk.Tk()
Tk.title('url编码工具python2.7版本')
Tk.resizable(width=False,height=False)
mv = mainView(Tk)
mv.pack()
Tk.mainloop()

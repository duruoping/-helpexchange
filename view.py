import tkinter as tk
from tkinter import ttk
from db import db
import json
import tkinter.messagebox
from tkinter import *

class InputFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root
        self.name = tk.StringVar()
        self.informationelse = tk.StringVar()
        self.address = tk.StringVar()
        self.phonenumber = tk.StringVar()
        self.status = tk.StringVar()
        self.create_page()

    def input(self):
        with open("materials.json","r",encoding = "utf-8") as fin:
            li = json.load(fin)
        
        if len(li) == 0:
            idx = str(0)
        else:
            idx = str(max([int(i) for i in list(li.keys())])+1)

        li[idx] = {"物品名称": self.info1.get(), "物品说明": self.info2.get(), "所在地址": self.info3.get(), "联系方式": self.info4.get()}
        
        with open("materials.json","w",encoding = "utf-8") as fin:
            json.dump(li,fin, ensure_ascii=False)

        tkinter.messagebox.showinfo('提示','已存储')
        self.info1.delete(0,"end")
        self.info2.delete(0,"end")
        self.info3.delete(0,"end")
        self.info4.delete(0,"end")


    def create_page(self):
        # stick 控件对象方向 tk.W 西方位
        # pady padding y 上下的宽度
        # row 行 表格布局
        tk.Label(self).grid(row=0, stick=tk.W, pady=10)
        tk.Label(self, text='物品名称: ').grid(row=1, stick=tk.W, pady=10)
        # text variable 绑定控件里面的数据内容
        self.info1 = tk.Entry(self, textvariable=self.name)
        self.info1.grid(row=1, column=1, stick=tk.E)
        tk.Label(self, text='物品说明: ').grid(row=2, stick=tk.W, pady=10)
        self.info2 = tk.Entry(self, textvariable=self.informationelse)
        self.info2.grid(row=2, column=1, stick=tk.E)
        tk.Label(self, text='所在地址: ').grid(row=3, stick=tk.W, pady=10)
        self.info3 = tk.Entry(self, textvariable=self.address)
        self.info3.grid(row=3, column=1, stick=tk.E)
        tk.Label(self, text='联系方式: ').grid(row=4, stick=tk.W, pady=10)
        self.info4 = tk.Entry(self, textvariable=self.phonenumber)
        self.info4.grid(row=4, column=1, stick=tk.E)

        tk.Button(self, text='录入', command=self.input).grid(row=5, column=1, stick=tk.E, pady=10)
        tk.Label(self, textvariable=self.status).grid(row=6, column=1, stick=tk.E, pady=10)



class QueryFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root
        self.itemName = tk.StringVar()

        tk.Label(self, text='查询界面').pack()
        self.table_frame = tk.Frame(self)
        self.table_frame.pack()
        self.row = 1
        self.listBox = None
        self.VScroll = None
        self.HScroll = None


        self.create_page()

    def create_page(self):
        tk.Button(self, text='刷新数据', command=self.show_data_frame).pack(anchor=tk.E, pady=5)
        # self.show_data_frame()

    def show_data_frame(self):
        with open("materials.json","r",encoding = "utf-8") as fin:
            li = json.load(fin)
        if self.listBox:
            self.listBox.destroy()
        if self.VScroll:
            self.VScroll.destroy()
        if self.HScroll:
            self.HScroll.destroy()
        data = [[k]+[li[k][k1] for k1 in li[k]] for k in li]
        self.listBox = ttk.Treeview(self.root, height=15, columns=["id","name","illustration","address","phone"], show='headings')  # 创建表格
        self.VScroll = ttk.Scrollbar(self.root, orient='vertical', command=self.listBox.yview)  # 创建滚动条
        self.HScroll = ttk.Scrollbar(self.root, orient='horizontal', command=self.listBox.xview)  # 创建滚动条
        self.listBox.configure(yscrollcommand=self.VScroll.set)  # 滚动条与表格控件关联
        self.VScroll.pack(side = "right", fill = "y")  # 滚动条放置位置
        self.HScroll.pack(side = "bottom", fill = "x")  # 滚动条放置位置
        self.listBox.heading('id', text="编号", anchor="w")
        self.listBox.heading('name', text="物品名称", anchor="w")
        self.listBox.heading('illustration', text="物品说明", anchor="w")
        self.listBox.heading('address',text="所在地址",anchor="w")
        self.listBox.heading('phone', text="联系方式", anchor="w")
        for itm in data:
            self.listBox.insert("",-1,values=itm)
        self.listBox.pack(expand=1, fill="both")


class DeleteFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root
        tk.Label(self, text='删除数据').pack()
        self.delete_frame = tk.Frame(self)
        self.delete_frame.pack()
        self.status = tk.StringVar()
        self.v1 = tk.StringVar()
        self.create_page()

    def create_page(self):
        tk.Label(self.delete_frame, text='根据名字删除信息').pack(anchor=tk.W, padx=20)
        self.e1 = tk.Entry(self.delete_frame, textvariable=self.v1)
        self.e1.pack(side=tk.LEFT, padx=20, pady=5)

        tk.Button(self.delete_frame, text='删除', command=self._delete).pack()
        tk.Label(self, textvariable=self.status).pack()

    def _delete(self):
        with open("materials.json","r",encoding = "utf-8") as fin:
            li = json.load(fin)
        item = self.e1.get()
        ks = [k for k in li if li[k]["物品名称"] == item]
        for k in ks:
            del li[k]
        with open("materials.json","w",encoding = "utf-8") as fin:
            json.dump(li,fin, ensure_ascii=False)
        
        


class ChangeFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master  # 定义内部变量root

        tk.Label(self, text='修改界面').pack()
        self.change_frame = tk.Frame(self)
        self.change_frame.pack()
        self.status = tk.StringVar()
        self.name = tk.StringVar()
        self.informationelse = tk.StringVar()
        self.address = tk.StringVar()
        self.phonenumber = tk.StringVar()
        self.k = None
        self.create_page()

    def create_page(self):
        tk.Label(self.change_frame).grid(row=0, stick=tk.W, pady=1)
        tk.Label(self.change_frame, text='物品名称: ').grid(row=1, stick=tk.W, pady=10)
        self.info1 = tk.Entry(self.change_frame, textvariable=self.name)
        self.info1.grid(row=1, column=1, stick=tk.E)
        tk.Label(self.change_frame, text='物品说明: ').grid(row=2, stick=tk.W, pady=10)
        self.info2 = tk.Entry(self.change_frame, textvariable=self.informationelse)
        self.info2.grid(row=2, column=1, stick=tk.E)
        tk.Label(self.change_frame, text='所在地址: ').grid(row=3, stick=tk.W, pady=10)
        self.info3 = tk.Entry(self.change_frame, textvariable=self.address)
        self.info3.grid(row=3, column=1, stick=tk.E)
        tk.Label(self.change_frame, text='联系方式: ').grid(row=4, stick=tk.W, pady=10)
        self.info4 = tk.Entry(self.change_frame, textvariable=self.phonenumber)
        self.info4.grid(row=4, column=1, stick=tk.E)
        tk.Button(self.change_frame, text='查询', command=self._search).grid(row=6, column=0, stick=tk.W, pady=10)
        tk.Button(self.change_frame, text='修改', command=self._change).grid(row=6, column=1, stick=tk.E, pady=10)
        tk.Label(self.change_frame, textvariable=self.status).grid(row=7, column=1, stick=tk.E, pady=10)

    def _search(self):
        with open("materials.json","r",encoding = "utf-8") as fin:
            li = json.load(fin)
        if self.info1.get() in [li[key]["物品名称"] for key in li]:
            k = [key for key in li if li[key]["物品名称"] == self.info1.get()][0]

            self.info2.insert(0,li[k]["物品说明"])
            self.info3.insert(0,li[k]["所在地址"])
            self.info4.insert(0,li[k]["联系方式"])
            
            self.k = k


    def _change(self):
        with open("materials.json","r",encoding = "utf-8") as fin:
            li = json.load(fin)
        idx = self.k

        if idx:
            li[idx] = {"物品名称": self.info1.get(), "物品说明": self.info2.get(), "所在地址": self.info3.get(), "联系方式": self.info4.get()}
        
            with open("materials.json","w",encoding = "utf-8") as fin:
                json.dump(li,fin, ensure_ascii=False)

            tkinter.messagebox.showinfo('提示','已修改')
            self.info1.delete(0,"end")
            self.info2.delete(0,"end")
            self.info3.delete(0,"end")
            self.info4.delete(0,"end")


class AboutFrame(tk.Frame):  # 继承Frame类
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.create_page()

    def create_page(self):
        tk.Label(self, text='关于作品：软件工程大作业').pack(anchor=tk.W)
        tk.Label(self, text='关于作者：贾祎萍').pack(anchor=tk.W)
      
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('%dx%d' % (600, 400))
    q = InputFrame(root)
    q.pack()
    root.mainloop()

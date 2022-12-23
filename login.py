
import tkinter as tk
import tkinter.messagebox
from main import MainPage
import json

# 标准开发代码
class LoginPage:
    """登录界面"""

    def __init__(self, master):
        # 将画板绑定到实例对象
        self.root = master
        # self.page 画纸
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.root.geometry("%dx%d" % (300, 180))

        # tkinter 提供的可变变量
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        # 创建一个lab
        # 网格布局
        tk.Label(self.page).grid(row=0, column=0)
        # textvariable 这个参数是把 tkinter 里面的字符串变量与 空间绑定起来
        tk.Label(self.page, text="账户").grid(row=1, column=0, stick=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=tk.W, pady=10)
        tk.Label(self.page, text="密码").grid(row=2, column=0, stick=tk.E, pady=10)
        tk.Entry(self.page, textvariable=self.password).grid(row=2, column=1, stick=tk.W, pady=10)
        # command 接受一个函数 执行登录的逻辑
        tk.Button(self.page, text="登录", command=self.login_check).grid(row=3, column=0, stick=tk.W, pady=10)
        tk.Button(self.page, text="退出").grid(row=3, column=1, stick=tk.E, pady=10)

    def login_check(self):
        """检验登录"""
        # 拿到账号与密码
        name = self.username.get()
        pwd = self.password.get()
        # 不去查询数据库
        with open("user.json","r",encoding = "utf-8") as fin:
            user = json.load(fin)
        if [name,pwd] in user:
            print('恭喜登录成功')
            # 摧毁当前页面绘制的内容
            self.page.destroy()
            # 页面的切换
            MainPage(self.root)
        else:
            tkinter.messagebox.showinfo(title='错误', message='账户或者密码错误')
    
    # def register(self):


if __name__ == '__main__':
    # 创建一个对象 窗口对象
    root = tk.Tk()
    LoginPage(root)
    # 显示界面
    root.mainloop()


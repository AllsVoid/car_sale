import wx
import wx.grid
from mydb import Sql_operation
from EOperation import EOperation
from CarOperation import CarOperation
from COperation import COperation
from CarOperation import InquireOp
from SOperation import SOperation
from CustomManer import CustomManer
#创建系统登录界面
class UserLogin(wx.Frame):
    '''
	登录界面
	'''

    #初始化登录界面
    def __init__(self, *args, **kw):
        # ensure the parent's __init__ is called
        super(UserLogin, self).__init__(*args, **kw)
        #设置窗口屏幕居中
        self.Center()
        #创建窗口
        self.pnl = wx.Panel(self)
        #调用登录界面函数
        self.LoginInterface()

    def LoginInterface(self):
        #创建垂直方向box布局管理器
        vbox = wx.BoxSizer(wx.VERTICAL)
        #################################################################################
        #创建logo静态文本，设置字体属性
        logo = wx.StaticText(self.pnl, label="轿车信息管理系统")
        font = logo.GetFont()
        font.PointSize += 30
        font = font.Bold()
        logo.SetFont(font)
        #添加logo静态文本到vbox布局管理器
        vbox.Add(logo,
                 proportion=0,
                 flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,
                 border=180)
        #################################################################################
        #创建静态框
        sb_username = wx.StaticBox(self.pnl, label="用户名")
        sb_password = wx.StaticBox(self.pnl, label="密  码")
        #创建水平方向box布局管理器
        hbox_username = wx.StaticBoxSizer(sb_username, wx.HORIZONTAL)
        hbox_password = wx.StaticBoxSizer(sb_password, wx.HORIZONTAL)
        #创建用户名、密码输入框
        self.user_name = wx.TextCtrl(self.pnl, size=(210, 25))
        self.user_password = wx.TextCtrl(self.pnl,
                                         size=(210, 25),
                                         style=wx.TE_PASSWORD)
        self.showinfo=wx.TextCtrl(self.pnl,style=wx.TE_MULTILINE | wx.HSCROLL,size=(150,150))
        #添加用户名和密码输入框到hbox布局管理器
        hbox_username.Add(self.user_name, 0, wx.EXPAND | wx.BOTTOM, 5)
        hbox_password.Add(self.user_password, 0, wx.EXPAND | wx.BOTTOM, 5)
        #将水平box添加到垂直box
        vbox.Add(hbox_username, proportion=0, flag=wx.CENTER)
        vbox.Add(hbox_password, proportion=0, flag=wx.CENTER)
        #################################################################################
        #创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        #创建登录按钮、绑定事件处理
        login_button = wx.Button(self.pnl, label="登录", size=(80, 25))
        login_button.Bind(wx.EVT_BUTTON, self.LoginButton)
        #添加登录按钮到hbox布局管理器
        hbox.Add(login_button, 0, flag=wx.EXPAND | wx.TOP, border=5)
        #将水平box添加到垂直box
        vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        vbox.Add(self.showinfo, proportion=0, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)
        #################################################################################
        #设置面板的布局管理器vbox
        self.pnl.SetSizer(vbox)

    def LoginButton(self, event):
        #连接cara_sale数据库
        op = Sql_operation("car_sale")
        #获取users表中的用户名和密码信息，返回为二维元组
        np = op.FindAll("user")
        #匹配标记
        login_sign = 0
        #匹配用户名和密码
        for i in np:
            if (i[1] == self.user_name.GetValue()) and (
                    i[2] == self.user_password.GetValue()):
                login_sign = 1
                if i[1]=='custom':
                    login_sign=2
                print(login_sign)
                print(i[1])
                print(i[2])
                break
        if login_sign == 0:
            self.showinfo.AppendText("用户名或密码错误！")
        elif login_sign == 1:
            print("登录成功！")
            operation = Maner(None, title="信息管理", size=(1024, 668))
            operation.Show()
            self.Close(True)
        elif login_sign==2:
            print("登陆成功")
            operation=CustomManer(None,title="客户界面",size=(1024,668))
            operation.Show()
            self.Close(True)
class Maner(wx.Frame):
    def __init__(self, *args, **kw):
        super(Maner, self).__init__(*args, **kw)
        self.Center()
        self.pnl = wx.Panel(self)
        self.ManerBoard()

    def ManerBoard(self):
        #创建垂直方向box布局管理器
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        #添加文本logo
        logo = wx.StaticText(self.pnl, label="信息管理界面")
        font = logo.GetFont()
        font.PointSize += 30
        font = font.Bold()
        logo.SetFont(font)
        #将logo添加进self.vbox
        self.vbox.Add(logo,
                      proportion=0,
                      flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,
                      border=5)
        stext=wx.StaticBox(self.pnl,label="选择操作",size=(800,600))
        vbox_center=wx.StaticBoxSizer(stext,wx.VERTICAL)
        CButton = wx.Button(self.pnl, id=5, label="用户管理", size=(150, 40))
        CButton.Bind(wx.EVT_BUTTON, self.Click)
        EButton = wx.Button(self.pnl, id=6, label="员工管理", size=(150, 40))
        EButton.Bind(wx.EVT_BUTTON, self.Click)
        CarButton = wx.Button(self.pnl, id=7, label="车辆管理", size=(150, 40))
        CarButton.Bind(wx.EVT_BUTTON, self.Click)
        SaleButton = wx.Button(self.pnl, id=8, label="销售信息管理", size=(150, 40))
        SaleButton.Bind(wx.EVT_BUTTON,self.Click)
        #self.Bind(wx.wxEVT_BUTTON, self.Click, id=5, id2=7)
        vbox_center.Add(CButton, proportion=0, flag=wx.CENTER | wx.BOTTOM,border=40)
        vbox_center.Add(EButton, proportion=0, flag=wx.CENTER | wx.BOTTOM,border=40)
        vbox_center.Add(CarButton, proportion=0, flag=wx.CENTER | wx.BOTTOM,border=40)
        vbox_center.Add(SaleButton, proportion=0, flag=wx.CENTER | wx.BOTTOM,border=40)
        hbox=wx.BoxSizer()
        hbox.Add(vbox_center,proportion=0,flag=wx.EXPAND | wx.BOTTOM,border=5)
        self.vbox.Add(hbox,proportion=0,flag=wx.CENTER)
        self.pnl.SetSizer(self.vbox)

    def Click(self, event):
        Bid = event.GetId()
        if Bid == 5:
            User = COperation(None, title="客户管理界面", size=(1024, 668))
            User.Show()
            self.Close(True)
        if Bid == 6:
            Employ=EOperation(None,title="员工管理界面",size=(1024,668))
            Employ.Show()
            self.Close(True)
        if Bid == 7:
            Car=CarOperation(None,title="车辆管理界面",size=(1024,668))
            Car.Show()
            self.Close(True)
        if Bid == 8:
            Sale=SOperation(None,title="销售信息管理界面",size=(1024,668))
            Sale.Show()
            self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    login = UserLogin(None, title="轿车营销管理系统", size=(1024, 668))
    login.Show()
    app.MainLoop()
"""
if __name__ == '__main__':
    app = wx.App()
    Userm = Maner(None, title="信息管理", size=(1024, 668))
    Userm.Show()
    app.MainLoop()
"""
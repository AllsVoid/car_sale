import wx
import wx.grid
from mydb import Sql_operation


class CustomManer(wx.Frame):
    def __init__(self, *args, **kw):
        super(CustomManer, self).__init__(*args, **kw)
        self.Center
        self.pnl = wx.Panel(self)
        self.CustomUI()

    def CustomUI(self):
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        #################################################################################
        #创建logo静态文本，设置字体属性
        #"""
        logo = wx.StaticText(self.pnl, label="XX销售公司欢迎您！")
        font = logo.GetFont()
        font.PointSize += 20
        font = font.Bold()
        logo.SetFont(font)
        self.vbox.Add(logo,
                      proportion=0,
                      flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,
                      border=5)
        #"""
        #################################################################################
        #创建左侧的静态框
        text_frame = wx.StaticBox(self.pnl, label="选择操作")
        #创建垂直方向box布局管理器
        vbox_button = wx.StaticBoxSizer(text_frame, wx.VERTICAL)
        #创建操作按钮、绑定事件处理
        check_button = wx.Button(self.pnl,
                                 id=10,
                                 label="查看车辆信息",
                                 size=(150, 50))
        quit_button = wx.Button(self.pnl, id=11, label="退出系统", size=(150, 50))
        self.Bind(wx.EVT_BUTTON, self.ClickButton, id=10, id2=11)
        #添加操作按钮到vbox布局管理器
        vbox_button.Add(check_button, 0, wx.EXPAND | wx.BOTTOM, 40)
        vbox_button.Add(quit_button, 0, wx.EXPAND | wx.BOTTOM, 200)
        #创建右侧静态框
        right_showop = wx.StaticBox(self.pnl, label="显示/操作窗口", size=(800, 500))
        #创建垂直方向box布局管理器
        self.vbox_showop = wx.StaticBoxSizer(right_showop, wx.VERTICAL)
        #创建水平方向box布局管理器
        hbox = wx.BoxSizer()
        hbox.Add(vbox_button, 0, wx.EXPAND | wx.BOTTOM, 5)
        hbox.Add(self.vbox_showop, 0, wx.EXPAND | wx.BOTTOM, 5)
        #将hbox添加到垂直box
        self.vbox.Add(hbox, proportion=0, flag=wx.CENTER)
        #################################################################################
        self.pnl.SetSizer(self.vbox)

    def ClickButton(self, event):
        Bid = event.GetId()
        if Bid == 10:
            print("查询操作！")
            inquire_button = ViewOp(None, title="车辆管理系统", size=(1024, 720))
            inquire_button.Show()
            self.Close(True)
        elif Bid == 11:
            self.Close(True)


class ViewOp(CustomManer):
    def __init__(self, *args, **kw):
        super(ViewOp, self).__init__(*args, **kw)
        self.cgrid = self.CreateGrid()
        self.cgrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,
                        self.OnLabelleftClick)
        #添加到vbox_showop布局管理器
        self.vbox_showop.Add(self.cgrid, 0,
                             wx.CENTER | wx.TOP | wx.FIXED_MINSIZE, 30)

    def ClickButton(self, event):
        Bid = event.GetId()
        if Bid == 10:
            print("查询操作！")
            inquire_button = ViewOp(None, title="车辆管理系统", size=(1024, 720))
            inquire_button.Show()
            self.Close(True)
        elif Bid == 11:
            self.Close(True)

    def CreateGrid(self):
        #连接car_sale数据库
        op = Sql_operation("car_sale")
        #获取car表中的学生信息，返回为二维元组
        np = op.FindAll("car")
        column_names = ("车辆编号", "型号", "颜色", "生产厂商", "出厂日期", "价格")
        cgrid = wx.grid.Grid(self.pnl)
        #CreateGrid(行数，列数)
        cgrid.CreateGrid(len(np), len(np[0]) - 1)
        for row in range(len(np)):
            #表格横向为对应表中的属性，纵向为首个属性的数据
            cgrid.SetRowLabelValue(row, str(np[row][0]))
            for col in range(1, len(np[row])):
                cgrid.SetColLabelValue(col - 1, column_names[col])
                cgrid.SetCellValue(row, col - 1, str(np[row][col]))
        cgrid.AutoSize()
        return cgrid

    def OnLabelleftClick(self, event):
        #连接car_sale数据库
        op = Sql_operation("car_sale")
        np = op.FindAll("car")
        print("RowIdx: {0}".format(event.GetRow()))
        print("ColIdx: {0}".format(event.GetRow()))
        print(np[event.GetRow()])
        event.Skip()

"""
if __name__ == '__main__':
    app = wx.App()
    login = CustomManer(None, title="车辆信息查看界面", size=(1024, 720))
    login.Show()
    app.MainLoop()
"""
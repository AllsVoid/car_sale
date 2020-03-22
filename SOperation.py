import wx
import wx.grid
from mydb import Sql_operation
class SOperation(wx.Frame):
	'''
	操作界面
	'''
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(SOperation,self).__init__(*args, **kw)
		#设置窗口屏幕居中
		self.Center()
		#创建窗口
		self.pnl = wx.Panel(self)
		#调用操作界面函数
		self.OperationInterface()

	def OperationInterface(self):
		#创建垂直方向box布局管理器
		self.vbox = wx.BoxSizer(wx.VERTICAL)
		#################################################################################
		#创建logo静态文本，设置字体属性
		logo = wx.StaticText(self.pnl,label="销售信息管理")
		font = logo.GetFont()
		font.PointSize += 30
		font = font.Bold()
		logo.SetFont(font)
		#添加logo静态文本到vbox布局管理中
		self.vbox.Add(logo,proportion=0,flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTER,border=5)
		#################################################################################
		#创建左侧的静态框
		text_frame = wx.StaticBox(self.pnl,label="选择操作")
		#创建垂直方向box布局管理器
		vbox_button = wx.StaticBoxSizer(text_frame,wx.VERTICAL)
		#创建操作按钮、绑定事件处理
		check_button = wx.Button(self.pnl,id=10,label="查看销售信息",size=(150,50))
		add_button = wx.Button(self.pnl,id=11,label="添加销售信息",size=(150,50))
		xls_button = wx.Button(self.pnl,id=12,label="导出数据",size=(150,50))
		update_button = wx.Button(self.pnl,id=14,label="修改销售信息",size=(150,50))
		quit_button = wx.Button(self.pnl,id=13,label="退出系统",size=(150,50))
		self.Bind(wx.EVT_BUTTON,self.ClickButton,id=10,id2=14)
		#添加操作按钮到vbox布局管理器
		vbox_button.Add(check_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(add_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(xls_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(update_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(quit_button,0,wx.EXPAND | wx.BOTTOM,200)
		#创建右侧静态框
		sb_show_operation = wx.StaticBox(self.pnl,label="显示/操作窗口",size=(800,450))
		#创建垂直方向box布局管理器
		self.vbox_showop = wx.StaticBoxSizer(sb_show_operation,wx.VERTICAL)
		#创建水平方向box布局管理器
		hbox = wx.BoxSizer()
		hbox.Add(vbox_button,0,wx.EXPAND | wx.BOTTOM,5)
		hbox.Add(self.vbox_showop,0,wx.EXPAND | wx.BOTTOM,5)
		#将hbox添加到垂直box
		self.vbox.Add(hbox,proportion=0,flag=wx.CENTER)
		#################################################################################
		self.pnl.SetSizer(self.vbox)
    #通过对应的按钮进行事件的跳转
	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="销售管理系统",size=(1024,720))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			print("添加操作！")
			add_button = AddOp(None,title="销售管理系统",size=(1024,720))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			print("导出数据")
			xls_button = ExcelOp(None,title="销售管理系统",size=(1024,720))
			xls_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="销售管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)

#继承SOperation类，实现初始化操作界面
"""
进行数据库的查询操作
"""
class InquireOp(SOperation):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(InquireOp,self).__init__(*args, **kw)
		#创建销售信息网格
		self.cgrid = self.CreateGrid()
		self.cgrid.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK,self.OnLabelleftClick)
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(self.cgrid,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,30)
    #此处的ClickButton用于事件之间的跳转
	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			pass
		elif Bid == 11:
			print("添加操作！")
			add_button = AddOp(None,title="销售管理系统",size=(1024,720))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			print("导出数据")
			xls_button = ExcelOp(None,title="销售管理系统",size=(1024,720))
			xls_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="销售管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)
    #创建用于显示数据的表格
	def CreateGrid(self):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		#获取car表中的学生信息，返回为二维元组
		np = op.FindAll("sale")
		column_types = ("销售编号","车辆编号","销售车型","车辆颜色","销售日期","销售数量","销售员","买家")
		cgrid = wx.grid.Grid(self.pnl)
		#CreateGrid(行数，列数)
		cgrid.CreateGrid(len(np),len(np[0])-1)
		for row in range(len(np)):
            #表格横向为对应表中的属性，纵向为首个属性的数据
			#row[0]要显示的为第一列
			cgrid.SetRowLabelValue(row,str(np[row][0]))
			for col in range(1,len(np[row])):
				cgrid.SetColLabelValue(col-1,column_types[col])
				cgrid.SetCellValue(row,col-1,str(np[row][col]))
		cgrid.AutoSize()
		return cgrid

	def OnLabelleftClick(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		np = op.FindAll("sale")
		print("RowIdx: {0}".format(event.GetRow()))
		print("ColIdx: {0}".format(event.GetRow()))
		print(np[event.GetRow()])
		event.Skip()

#继承SOperation类，实现初始化操作界面
"""
数据库插入操作
"""
class AddOp(SOperation):
	def __init__(self,*args,**kw):
		super(AddOp,self).__init__(*args, **kw)
		#创建表中属性文本框
		self.sale_no=wx.TextCtrl(self.pnl,size=(210,25))
		self.sale_car = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_type = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_color = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_date = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_num = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_man=wx.TextCtrl(self.pnl,size=(210,25))
		self.add_affirm = wx.Button(self.pnl,label="添加",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.add_affirm.Bind(wx.EVT_BUTTON,self.AddAffirm)

        #创建静态框
		text_no=wx.StaticBox(self.pnl,label="销售编号")
		text_car = wx.StaticBox(self.pnl,label="车辆编号")
		text_type = wx.StaticBox(self.pnl,label="销售车型")
		text_color = wx.StaticBox(self.pnl,label="车辆颜色")
		text_date = wx.StaticBox(self.pnl,label="销售日期")
		text_num = wx.StaticBox(self.pnl,label="销售数量")
		text_man=wx.StaticBox(self.pnl,label="销售员")
		#创建水平方向box布局管理器
		hbox_no=wx.StaticBoxSizer(text_no,wx.HORIZONTAL)
		hbox_car = wx.StaticBoxSizer(text_car,wx.HORIZONTAL)
		hbox_type = wx.StaticBoxSizer(text_type,wx.HORIZONTAL)
		hbox_color = wx.StaticBoxSizer(text_color,wx.HORIZONTAL)
		hbox_date = wx.StaticBoxSizer(text_date,wx.HORIZONTAL)
		hbox_num = wx.StaticBoxSizer(text_num,wx.HORIZONTAL)
		hbox_man=wx.StaticBoxSizer(text_man,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hbox_no.Add(self.sale_no,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_car.Add(self.sale_car,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_type.Add(self.sale_type,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_color.Add(self.sale_color,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_date.Add(self.sale_date,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_num.Add(self.sale_num,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_man.Add(self.sale_man,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_no,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_car,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_type,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_color,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_date,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_num,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_man,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.add_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="销售管理系统",size=(1024,720))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			pass
		elif Bid == 12:
			print("导出数据")
			xls_button = ExcelOp(None,title="销售管理系统",size=(1024,720))
			xls_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="销售管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)
	def AddAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		sale_car = self.sale_car.GetValue()
		print(sale_car)
		sale_type = self.sale_type.GetValue()
		print(sale_type)
		sale_color = self.sale_color.GetValue()
		print(sale_color)
		sale_date = self.sale_date.GetValue()
		print(sale_date)
		sale_num = self.sale_num.GetValue()
		print(sale_num)
		sale_man=self.sale_man.GetValue()
		print(sale_man)
		np = op.SInsert(sale_car,sale_type,sale_color,sale_date,sale_num,sale_man)
class UpdateOp(SOperation):
	def __init__(self,*args,**kw):
		super(UpdateOp,self).__init__(*args, **kw)
		#创建表中属性文本框
		self.sale_no = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_car = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_type = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_color = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_date = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_num = wx.TextCtrl(self.pnl,size = (210,25))
		self.sale_man=wx.TextCtrl(self.pnl,size=(210,25))
		self.update_affirm = wx.Button(self.pnl,label="修改",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.update_affirm.Bind(wx.EVT_BUTTON,self.UpdateAffirm)

        #创建静态框
		text_no = wx.StaticBox(self.pnl,label="销售编号")
		text_car = wx.StaticBox(self.pnl,label="车辆编号")
		text_type = wx.StaticBox(self.pnl,label="销售车型")
		text_color = wx.StaticBox(self.pnl,label="车辆颜色")
		text_date = wx.StaticBox(self.pnl,label="销售日期")
		text_num = wx.StaticBox(self.pnl,label="销售数量")
		text_man=wx.StaticBox(self.pnl,label="销售员")
		#创建水平方向box布局管理器
		hbox_no = wx.StaticBoxSizer(text_car,wx.HORIZONTAL)
		hbox_car = wx.StaticBoxSizer(text_car,wx.HORIZONTAL)
		hbox_type = wx.StaticBoxSizer(text_type,wx.HORIZONTAL)
		hbox_color = wx.StaticBoxSizer(text_color,wx.HORIZONTAL)
		hbox_date = wx.StaticBoxSizer(text_date,wx.HORIZONTAL)
		hbox_num = wx.StaticBoxSizer(text_num,wx.HORIZONTAL)
		hbox_man=wx.StaticBoxSizer(text_man,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hbox_no.Add(self.sale_car,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_car.Add(self.sale_car,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_type.Add(self.sale_type,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_color.Add(self.sale_color,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_date.Add(self.sale_date,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_num.Add(self.sale_num,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_man.Add(self.sale_man,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_no,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_car,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_type,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_color,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_date,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_num,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_man,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.update_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="销售管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			print("添加操作！")
			update_buttom=UpdateOp(None,title="销售管理系统",size=(1024,668))
			update_buttom.Show()
			self.Close(True)
		elif Bid == 12:
			print("导出数据")
			xls_button = ExcelOp(None,title="销售管理系统",size=(1024,668))
			xls_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			pass
	def UpdateAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		sale_car = self.sale_car.GetValue()
		print(sale_car)
		sale_type = self.sale_type.GetValue()
		print(sale_type)
		sale_color = self.sale_color.GetValue()
		print(sale_color)
		sale_date = self.sale_date.GetValue()
		print(sale_date)
		sale_num = self.sale_num.GetValue()
		print(sale_num)
		sale_man=self.sale_man.GetValue()
		print(sale_man)
		np = op.SUpdate(sale_car,sale_type,sale_color,sale_date,sale_num,sale_man)
#继承InquireOp类，实现初始化操作界面
class ExcelOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(ExcelOp,self).__init__(*args, **kw)
		#创建删除销售输入框、删除按钮
		self.excel_affrim = wx.Button(self.pnl,label="导出",pos=(625,400),size=(80,25))
		#为删除按钮组件绑定事件处理
		self.excel_affrim.Bind(wx.EVT_BUTTON,self.ExcelAffrim)
		#################################################################################
		#创建静态框
		text_xls = wx.StaticBox(self.pnl,label="导出销售数据")
		#创建水平方向box布局管理器
		hbox_xls = wx.StaticBoxSizer(text_xls,wx.HORIZONTAL)
		#添加到hbox_type布局管理器
		hbox_xls.Add(self.excel_affrim,0,wx.EXPAND | wx.BOTTOM,5)
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_xls,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.excel_affrim,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="销售管理系统",size=(1024,720))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			print("添加操作！")
			add_button = AddOp(None,title="销售管理系统",size=(1024,720))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			pass
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="销售管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)
	def ExcelAffrim(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")

		print("导出销售数据")
		np = op.SExcel()

		xls_button = ExcelOp(None,title="销售管理系统",size=(1024,720))
		xls_button.Show()
		self.Close(True)

if __name__ == '__main__':
	app = wx.App()
	login = SOperation(None,title="CSDN学生信息管理系统",size=(1024,668))
	login.Show()
	app.MainLoop()

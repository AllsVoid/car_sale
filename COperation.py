import wx
import wx.grid
from mydb import Sql_operation
#跳转至管理界面
class COperation(wx.Frame):
	'''
	操作界面
	'''
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(COperation,self).__init__(*args, **kw)
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
		logo = wx.StaticText(self.pnl,label="信息管理")
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
		check_button = wx.Button(self.pnl,id=10,label="查看客户信息",size=(150,50))
		add_button = wx.Button(self.pnl,id=11,label="添加客户信息",size=(150,50))
		delete_button = wx.Button(self.pnl,id=12,label="删除客户信息",size=(150,50))
		update_button = wx.Button(self.pnl,id=14,label="修改客户信息",size=(150,50))
		quit_button = wx.Button(self.pnl,id=13,label="退出系统",size=(150,50))
		self.Bind(wx.EVT_BUTTON,self.ClickButton,id=10,id2=14)
		#添加操作按钮到vbox布局管理器
		vbox_button.Add(check_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(add_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(delete_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(update_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(quit_button,0,wx.EXPAND | wx.BOTTOM,200)
		#创建右侧静态框
		sb_show_operation = wx.StaticBox(self.pnl,label="显示/操作窗口",size=(800,500))
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
			inquire_button = InquireOp(None,title="用户管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			print("添加操作！")
			add_button = AddOp(None,title="用户管理系统",size=(1024,668))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="用户管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_buttom=UpdateOp(None,title="用户管理系统",size=(1024,668))
			update_buttom.Show()
			self.Close(True)

#继承COperation类，实现初始化操作界面
"""
进行数据库的查询操作
"""
class InquireOp(COperation):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(InquireOp,self).__init__(*args, **kw)
		#创建学生信息网格
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
			add_button = AddOp(None,title="用户管理系统",size=(1024,668))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="用户管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="用户管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)
    #创建用于显示数据的表格
	def CreateGrid(self):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		#获取custom表中的学生信息，返回为二维元组
		np = op.FindAll("custom")
		column_names = ("客户姓名","年龄","性别","联系方式","业务记录")
		cgrid = wx.grid.Grid(self.pnl)
		cgrid.CreateGrid(len(np),len(np[0]))
		for row in range(len(np)):
            #表格横向为对应表中的属性，纵向为首个属性的数据
			cgrid.SetRowLabelValue(row,str(np[row][0]))
			for col in range(1,len(np[row])):
				cgrid.SetColLabelValue(col-1,column_names[col])
				cgrid.SetCellValue(row,col-1,str(np[row][col]))
		cgrid.AutoSize()
		return cgrid

	def OnLabelleftClick(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		np = op.FindAll("custom")
		print("RowIdx: {0}".format(event.GetRow()))
		print("ColIdx: {0}".format(event.GetRow()))
		print(np[event.GetRow()])
		event.Skip()

#继承COperation类，实现初始化操作界面
"""
数据库插入操作
"""
class AddOp(COperation):
	def __init__(self,*args,**kw):
		super(AddOp,self).__init__(*args, **kw)
		#创建表中属性文本框
		self.cname = wx.TextCtrl(self.pnl,size = (210,25))
		self.cage = wx.TextCtrl(self.pnl,size = (210,25))
		self.csex = wx.TextCtrl(self.pnl,size = (210,25))
		self.ctel = wx.TextCtrl(self.pnl,size = (210,25))
		self.Brecord = wx.TextCtrl(self.pnl,size = (210,25))
		self.add_affirm = wx.Button(self.pnl,label="添加",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.add_affirm.Bind(wx.EVT_BUTTON,self.AddAffirm)

        #创建静态框
		text_name = wx.StaticBox(self.pnl,label="客户姓名")
		text_age = wx.StaticBox(self.pnl,label="年  龄")
		text_sex = wx.StaticBox(self.pnl,label="性  别")
		text_tel = wx.StaticBox(self.pnl,label="联系方式")
		text_record = wx.StaticBox(self.pnl,label="业务记录")
		#创建水平方向box布局管理器
		hbox_name = wx.StaticBoxSizer(text_name,wx.HORIZONTAL)
		hbox_age = wx.StaticBoxSizer(text_age,wx.HORIZONTAL)
		hbox_sex = wx.StaticBoxSizer(text_sex,wx.HORIZONTAL)
		hbox_tel = wx.StaticBoxSizer(text_tel,wx.HORIZONTAL)
		hbox_record = wx.StaticBoxSizer(text_record,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hbox_name.Add(self.cname,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_age.Add(self.cage,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_sex.Add(self.csex,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_tel.Add(self.ctel,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_record.Add(self.Brecord,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_age,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_sex,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_tel,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_record,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.add_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="用户管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			pass
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="用户管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_buttom=UpdateOp(None,title="用户管理系统",size=(1024,668))
			update_buttom.Show()
			self.Close(True)

	def AddAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		#向stu_information表添加学生信息
		cname = self.cname.GetValue()
		print(cname)
		cage = self.cage.GetValue()
		print(cage)
		csex = self.csex.GetValue()
		print(csex)
		ctel = self.ctel.GetValue()
		print(ctel)
		Brecord = self.Brecord.GetValue()
		print(Brecord)
		np = op.CInsert(cname,cage,csex,ctel,Brecord)

class UpdateOp(COperation):
	def __init__(self,*args,**kw):
		super(UpdateOp,self).__init__(*args, **kw)
		#创建表中属性文本框
		self.cname = wx.TextCtrl(self.pnl,size = (210,25))
		self.cage = wx.TextCtrl(self.pnl,size = (210,25))
		self.csex = wx.TextCtrl(self.pnl,size = (210,25))
		self.ctel = wx.TextCtrl(self.pnl,size = (210,25))
		self.Brecord = wx.TextCtrl(self.pnl,size = (210,25))
		self.update_affirm = wx.Button(self.pnl,label="修改",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.update_affirm.Bind(wx.EVT_BUTTON,self.UpdateAffirm)

        #创建静态框
		text_name = wx.StaticBox(self.pnl,label="客户姓名")
		text_age = wx.StaticBox(self.pnl,label="年  龄")
		text_sex = wx.StaticBox(self.pnl,label="性  别")
		text_tel = wx.StaticBox(self.pnl,label="联系方式")
		text_record = wx.StaticBox(self.pnl,label="业务记录")
		#创建水平方向box布局管理器
		hbox_name = wx.StaticBoxSizer(text_name,wx.HORIZONTAL)
		hbox_age = wx.StaticBoxSizer(text_age,wx.HORIZONTAL)
		hbox_sex = wx.StaticBoxSizer(text_sex,wx.HORIZONTAL)
		hbox_tel = wx.StaticBoxSizer(text_tel,wx.HORIZONTAL)
		hbox_record = wx.StaticBoxSizer(text_record,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hbox_name.Add(self.cname,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_age.Add(self.cage,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_sex.Add(self.csex,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_tel.Add(self.ctel,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_record.Add(self.Brecord,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_age,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_sex,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_tel,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_record,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.update_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="用户管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			pass
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="用户管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_buttom=UpdateOp(None,title="用户管理系统",size=(1024,668))
			update_buttom.Show()
			self.Close(True)
	def UpdateAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		#向stu_information表添加学生信息
		cname = self.cname.GetValue()
		print(cname)
		cage = self.cage.GetValue()
		print(cage)
		csex = self.csex.GetValue()
		print(csex)
		ctel = self.ctel.GetValue()
		print(ctel)
		Brecord = self.Brecord.GetValue()
		print(Brecord)
		np = op.CUpdate(cname,cage,csex,ctel,Brecord)

#继承InquireOp类，实现初始化操作界面
class DelOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(DelOp,self).__init__(*args, **kw)
		#创建删除学员信息输入框、删除按钮
		self.del_id = wx.TextCtrl(self.pnl,pos = (407,78),size = (210,25))
		self.del_affirm = wx.Button(self.pnl,label="删除",pos=(625,78),size=(80,25))
		#为删除按钮组件绑定事件处理
		self.del_affirm.Bind(wx.EVT_BUTTON,self.DelAffirm)
		#################################################################################
		#创建静态框
		text_del = wx.StaticBox(self.pnl,label="请选择需要删除的用户姓名")
		#创建水平方向box布局管理器
		hbox_del = wx.StaticBoxSizer(text_del,wx.HORIZONTAL)
		#添加到hbox_name布局管理器
		hbox_del.Add(self.del_id,0,wx.EXPAND | wx.BOTTOM,5)
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_del,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.del_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)


	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="用户管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			print("添加操作！")
			add_button = AddOp(None,title="用户管理系统",size=(1024,668))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			pass
		elif Bid == 13:
			self.Close(True)

	def DelAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		#向stu_information表添加学生信息
		del_id = self.del_id.GetValue()
		print(del_id)
		np = op.CDel(str(del_id))

		del_button = DelOp(None,title="用户管理系统",size=(1024,668))
		del_button.Show()
		self.Close(True)
"""
if __name__ == '__main__':
	app = wx.App()
	login = COperation(None,title="用户管理系统",size=(1024,668))
	login.Show()
	app.MainLoop()
"""
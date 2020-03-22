import wx
import wx.grid
from mydb import Sql_operation
class EOperation(wx.Frame):
	'''
	操作界面
	'''
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(EOperation,self).__init__(*args, **kw)
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
		logo = wx.StaticText(self.pnl,label="员工信息管理")
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
		check_button = wx.Button(self.pnl,id=10,label="查看员工信息",size=(150,50))
		add_button = wx.Button(self.pnl,id=11,label="添加员工信息",size=(150,50))
		delete_button = wx.Button(self.pnl,id=12,label="删除员工信息",size=(150,50))
		update_button = wx.Button(self.pnl,id=14,label="修改员工信息",size=(150,50))
		quit_button = wx.Button(self.pnl,id=13,label="退出系统",size=(150,50))
		self.Bind(wx.EVT_BUTTON,self.ClickButton,id=10,id2=14)
		#添加操作按钮到vbox布局管理器
		vbox_button.Add(check_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(add_button,0,wx.EXPAND | wx.BOTTOM,40)
		vbox_button.Add(delete_button,0,wx.EXPAND | wx.BOTTOM,40)
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
			inquire_button = InquireOp(None,title="员工管理系统",size=(1024,720))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			print("添加操作！")
			add_button = AddOp(None,title="员工管理系统",size=(1024,720))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="员工管理系统",size=(1024,720))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="员工管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)

#继承EOperation类，实现初始化操作界面
"""
进行数据库的查询操作
"""
class InquireOp(EOperation):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(InquireOp,self).__init__(*args, **kw)
		#创建员工信息网格
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
			add_button = AddOp(None,title="员工管理系统",size=(1024,720))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="员工管理系统",size=(1024,720))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="员工管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)
    #创建用于显示数据的表格
	def CreateGrid(self):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		#获取car表中的学生信息，返回为二维元组
		np = op.FindAll("employ")
		column_names = ("员工编号","员工姓名","年龄","性别","籍贯","学历")
		cgrid = wx.grid.Grid(self.pnl)
		#CreateGrid(行数，列数)
		cgrid.CreateGrid(len(np),len(np[0])-1)
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
		np = op.FindAll("employ")
		print("RowIdx: {0}".format(event.GetRow()))
		print("ColIdx: {0}".format(event.GetRow()))
		print(np[event.GetRow()])
		event.Skip()

#继承EOperation类，实现初始化操作界面
"""
数据库插入操作
"""
class AddOp(EOperation):
	def __init__(self,*args,**kw):
		super(AddOp,self).__init__(*args, **kw)
		#创建表中属性文本框
		self.eno = wx.TextCtrl(self.pnl,size = (210,25))
		self.ename = wx.TextCtrl(self.pnl,size = (210,25))
		self.eage = wx.TextCtrl(self.pnl,size = (210,25))
		self.esex = wx.TextCtrl(self.pnl,size = (210,25))
		self.ehome = wx.TextCtrl(self.pnl,size = (210,25))
		self.edu=wx.TextCtrl(self.pnl,size=(210,25))
		self.add_affirm = wx.Button(self.pnl,label="添加",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.add_affirm.Bind(wx.EVT_BUTTON,self.AddAffirm)

        #创建静态框
		text_no = wx.StaticBox(self.pnl,label="员工编号")
		text_name = wx.StaticBox(self.pnl,label="员工姓名")
		text_age = wx.StaticBox(self.pnl,label="年  龄")
		text_sex = wx.StaticBox(self.pnl,label="性  别")
		text_home = wx.StaticBox(self.pnl,label="籍  贯")
		text_edu=wx.StaticBox(self.pnl,label="学  历")
		#创建水平方向box布局管理器
		hbox_no = wx.StaticBoxSizer(text_no,wx.HORIZONTAL)
		hbox_name = wx.StaticBoxSizer(text_name,wx.HORIZONTAL)
		hbox_age = wx.StaticBoxSizer(text_age,wx.HORIZONTAL)
		hbox_sex = wx.StaticBoxSizer(text_sex,wx.HORIZONTAL)
		hbox_home = wx.StaticBoxSizer(text_home,wx.HORIZONTAL)
		hbox_edu=wx.StaticBoxSizer(text_edu,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hbox_no.Add(self.eno,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_name.Add(self.ename,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_age.Add(self.eage,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_sex.Add(self.esex,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_home.Add(self.ehome,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_edu.Add(self.edu,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_no,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_age,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_sex,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_home,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_edu,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.add_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)

	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="员工管理系统",size=(1024,720))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			pass
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="员工管理系统",size=(1024,720))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="员工管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)
	def AddAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		eno = self.eno.GetValue()
		print(eno)
		ename = self.ename.GetValue()
		print(ename)
		eage = self.eage.GetValue()
		print(eage)
		esex = self.esex.GetValue()
		print(esex)
		ehome = self.ehome.GetValue()
		print(ehome)
		edu=self.edu.GetValue()
		print(edu)
		np = op.EInsert(eno,ename,eage,esex,ehome,edu)
class UpdateOp(EOperation):
	def __init__(self,*args,**kw):
		super(UpdateOp,self).__init__(*args, **kw)
		#创建表中属性文本框
		self.eno = wx.TextCtrl(self.pnl,size = (210,25))
		self.ename = wx.TextCtrl(self.pnl,size = (210,25))
		self.eage = wx.TextCtrl(self.pnl,size = (210,25))
		self.esex = wx.TextCtrl(self.pnl,size = (210,25))
		self.ehome = wx.TextCtrl(self.pnl,size = (210,25))
		self.edu=wx.TextCtrl(self.pnl,size=(210,25))
		self.update_affirm = wx.Button(self.pnl,label="修改",size=(80,25))
		#为添加按钮组件绑定事件处理
		self.update_affirm.Bind(wx.EVT_BUTTON,self.UpdateAffirm)

        #创建静态框
		text_no = wx.StaticBox(self.pnl,label="员工编号")
		text_name = wx.StaticBox(self.pnl,label="员工姓名")
		text_age = wx.StaticBox(self.pnl,label="年  龄")
		text_sex = wx.StaticBox(self.pnl,label="性  别")
		text_home = wx.StaticBox(self.pnl,label="籍  贯")
		text_edu=wx.StaticBox(self.pnl,label="学  历")
		#创建水平方向box布局管理器
		hbox_no = wx.StaticBoxSizer(text_no,wx.HORIZONTAL)
		hbox_name = wx.StaticBoxSizer(text_name,wx.HORIZONTAL)
		hbox_age = wx.StaticBoxSizer(text_age,wx.HORIZONTAL)
		hbox_sex = wx.StaticBoxSizer(text_sex,wx.HORIZONTAL)
		hbox_home = wx.StaticBoxSizer(text_home,wx.HORIZONTAL)
		hbox_edu=wx.StaticBoxSizer(text_edu,wx.HORIZONTAL)
		#添加到hsbox布局管理器
		hbox_no.Add(self.eno,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_name.Add(self.ename,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_age.Add(self.eage,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_sex.Add(self.esex,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_home.Add(self.ehome,0,wx.EXPAND | wx.BOTTOM,5)
		hbox_edu.Add(self.edu,0,wx.EXPAND | wx.BOTTOM,5)
		#################################################################################
		#添加到vbox_showop布局管理器
		self.vbox_showop.Add(hbox_no,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_name,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_age,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_sex,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_home,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(hbox_edu,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
		self.vbox_showop.Add(self.update_affirm,0,wx.CENTER | wx.TOP | wx.FIXED_MINSIZE,5)
	def ClickButton(self,event):
		Bid = event.GetId()
		if Bid == 10:
			print("查询操作！")
			inquire_button = InquireOp(None,title="员工管理系统",size=(1024,668))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			pass
		elif Bid == 12:
			print("删除操作！")
			del_button = DelOp(None,title="员工管理系统",size=(1024,668))
			del_button.Show()
			self.Close(True)
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_buttom=UpdateOp(None,title="员工管理系统",size=(1024,668))
			update_buttom.Show()
			self.Close(True)
	def UpdateAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		eno = self.eno.GetValue()
		print(eno)
		ename = self.ename.GetValue()
		print(ename)
		eage = self.eage.GetValue()
		print(eage)
		esex = self.esex.GetValue()
		print(esex)
		ehome = self.ehome.GetValue()
		print(ehome)
		edu=self.edu.GetValue()
		print(edu)
		np = op.EUpdate(eno,ename,eage,esex,ehome,edu)
#继承InquireOp类，实现初始化操作界面
class DelOp(InquireOp):
	def __init__(self,*args,**kw):
		# ensure the parent's __init__ is called
		super(DelOp,self).__init__(*args, **kw)
		#创建删除员工输入框、删除按钮
		self.del_id = wx.TextCtrl(self.pnl,pos = (407,400),size = (210,25))
		self.del_affirm = wx.Button(self.pnl,label="删除",pos=(625,400),size=(80,25))
		#为删除按钮组件绑定事件处理
		self.del_affirm.Bind(wx.EVT_BUTTON,self.DelAffirm)
		#################################################################################
		#创建静态框
		text_del = wx.StaticBox(self.pnl,label="请选择需要删除的员工编号")
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
			inquire_button = InquireOp(None,title="员工管理系统",size=(1024,720))
			inquire_button.Show()
			self.Close(True)
		elif Bid == 11:
			print("添加操作！")
			add_button = AddOp(None,title="员工管理系统",size=(1024,720))
			add_button.Show()
			self.Close(True)
		elif Bid == 12:
			pass
		elif Bid == 13:
			self.Close(True)
		elif Bid == 14:
			print("修改操作！")
			update_button=UpdateOp(None,title="员工管理系统",size=(1024,668))
			update_button.Show()
			self.Close(True)
	def DelAffirm(self,event):
		#连接car_sale数据库
		op = Sql_operation("car_sale")
		del_id = self.del_id.GetValue()
		print(del_id)
		np = op.EDel(int(del_id))

		del_button = DelOp(None,title="员工管理系统",size=(1024,720))
		del_button.Show()
		self.Close(True)
"""
if __name__ == '__main__':
	app = wx.App()
	login = EOperation(None,title="CSDN学生信息管理系统",size=(1024,668))
	login.Show()
	app.MainLoop()
"""
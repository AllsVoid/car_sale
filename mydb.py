import pymysql
import sys
import xlwt
#创建数据库操作类
class Sql_operation(object):
	'''
	数据库操作
	'''
	#用构造函数实现数据库连接，并引入mydb参数，实现调用不同的数据库
	def __init__(self,mydb):
		#实例变量
		self.mydb = mydb
		#打开数据库连接
		self.db = pymysql.connect(host = "localhost",user = "root",password = "kybb82157108",db = "car_sale",charset = "utf8")
		#创建游标对象
		self.cursor = self.db.cursor()

	#定义查看数据表信息函数，并引入table_field、table_name参数，实现查看不同数据表的建表语句
	def FindAll(self,table_name):
		#实例变量
		self.table_name = table_name
		#定义SQL语句
		sql = "select * from %s"%(self.table_name)
		try:
			#执行数据库操作
			self.cursor.execute(sql)
			#处理结果
			data = self.cursor.fetchall()
			return data
		except Exception as err:
			print("SQL执行错误，原因：",err)

	#定义添加表数据函数
	def CInsert(self,cname,cage,csex,ctel,Brecord):
		#实例变量
		self.cname = cname
		self.cage = cage
		self.csex = csex
		self.ctel = ctel
		self.Brecord = Brecord
		#定义SQL语句
		sql = "insert into custom(cname,cage,csex,ctel,Brecord) values('%s','%s','%s','%s','%s')"%(self.cname,self.cage,self.csex,self.ctel,self.Brecord)
		try:
			#执行数据库操作
			self.cursor.execute(sql)
			#事务提交
			self.db.commit()
		except Exception as err:
			#事务回滚
			self.db.rollback()
			print("SQL执行错误，原因：",err)
	def CarInsert(self,car_no, car_type, car_color, car_maner, car_date,car_price):
		self.car_no=car_no
		self.car_type=car_type
		self.car_color=car_color
		self.car_maner=car_maner
		self.car_date=car_date
		self.car_price=car_price
		sql="insert into car(car_no,car_type,car_color,car_maner,car_date,car_price) values('%s','%s','%s','%s','%s','%s')"%(self.car_no,self.car_type,self.car_color,
		self.car_maner,self.car_date,self.car_price)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as err:
			self.db.rollback()
			print("执行错误，原因:",err)
	def EInsert(self,eno, ename, eage, esex, ehome, edu):
		self.eno=eno
		self.ename=ename
		self.eage=eage
		self.esex=esex
		self.ehome=ehome
		self.edu=edu
		sql = "insert into employ values('%s','%s','%s','%s','%s','%s')"%(self.eno, self.ename, self.eage,
		self.esex, self.ehome, self.edu)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as err:
			self.db.rollback()
			print("执行错误，原因:",err)

	def SInsert(self,sale_car,sale_type,sale_color,sale_date,sale_num,sale_man):
		self.sale_car=sale_car
		self.sale_type=sale_type
		self.sale_color=sale_color
		self.sale_date=sale_date
		self.sale_num=sale_num
		self.sale_man=sale_man
		sql="insert into sale values('%s','%s','%s','%s','%s','%s')"%(self.sale_car, self.type, self.sale_color,
		self.sale_date,self.sale_num,self.sale_man)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as err:
			self.db.rollback()
			print("执行错误，原因:",err)


	#定义删除表数据函数
	def CDel(self,cname):
		#实例变量
		self.cname = cname
		#定义SQL语句
		sql = "delete from custom where cname='%s'"%(self.cname)
		try:
			#执行数据库操作
			self.cursor.execute(sql)
			#事务提交
			self.db.commit()
		except Exception as err:
			#事务回滚
			self.db.rollback()
			print("SQL执行错误，原因：",err)
	def CarDel(self,car_no):
		self.car_no=car_no
		sql="delete from car where car_no=%d"%(self.car_no)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as err:
			self.db.rollback()
			print("执行错误，原因:",err)
	def EDel(self,eno):
		self.eno=eno
		sql="delete from employ where eno=%d"%(self.eno)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as err:
			self.cursor.rollback()
			print("执行错误，原因:",err)

	def CUpdate(self,cname,cage,csex,ctel,Brecord):
		#实例变量
		self.cname = cname
		self.cage = cage
		self.csex = csex
		self.ctel = ctel
		self.Brecord = Brecord
		#定义SQL语句
		sql = "update custom set cname='%s',cage='%s',csex='%s',ctel='%s',Brecord='%s' where cname='%s'"%(self.cname,
		self.cage,self.csex,self.ctel,self.Brecord,self.cname)
		try:
			#执行数据库操作
			self.cursor.execute(sql)
			#事务提交
			self.db.commit()
		except Exception as err:
			#事务回滚
			self.db.rollback()
			print("SQL执行错误，原因：",err)
	def CarUpdate(self,car_no, car_type, car_color, car_maner, car_date,car_price):
		#实例变量
		self.car_no=car_no
		self.car_type=car_type
		self.car_color=car_color
		self.car_maner=car_maner
		self.car_date=car_date
		self.car_price=car_price
		#定义SQL语句
		sql = "update car set car_no='%s',car_type='%s',car_color='%s',car_maner='%s',car_date='%s',car_price='%f' where car_no=%s"%(self.car_no,
		self.car_type,self.car_color,self.car_maner,self.car_date,self.car_price,self.car_no)
		try:
			#执行数据库操作
			self.cursor.execute(sql)
			#事务提交
			self.db.commit()
		except Exception as err:
			#事务回滚
			self.db.rollback()
			print("SQL执行错误，原因：",err)
	def EUpdate(self,eno, ename, eage, esex, ehome, edu):
		self.eno=eno
		self.ename=ename
		self.eage=eage
		self.esex=esex
		self.ehome=ehome
		self.edu=edu
		sql = "update employ set eno='%s',ename='%s',eage='%s',esex='%s',ehome='%s',edu='%s' where eno='%s'"%(self.eno, self.ename, self.eage,
		self.esex, self.ehome, self.edu,self.eno)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as err:
			self.db.rollback()
			print("执行错误，原因:",err)
	def SUpdate(self,sale_no,sale_car,sale_type,sale_color,sale_date,sale_num,sale_man):
		self.sale_no=sale_no
		self.sale_car=sale_car
		self.sale_type=sale_type
		self.sale_color=sale_color
		self.sale_date=sale_date
		self.sale_num=sale_num
		self.sale_man=sale_man
		sql="update sale set sale_no='%d', sale_car='%s',sale_type='%s', sale_color='%s',sale_date='%s',sale_num='%s',sale_man='%s' where sale_no='%d'"%(self.sale_no,self.sale_car,
		self.type, self.sale_color,self.sale_date,self.sale_num,self.sale_man,self.sale_no)
		try:
			self.cursor.execute(sql)
			self.db.commit()
		except Exception as err:
			self.db.rollback()
			print("执行错误，原因:",err)
	def SExcel(self):
		sql="select * from sale"
		self.cursor.execute(sql)
		data=self.cursor.fetchall()
		self.cursor.scroll(0,mode='absolute')
		fields=self.cursor.description
		workbook=xlwt.Workbook()
		sheet=workbook.add_sheet('sheet1', cell_overwrite_ok=True)

		for field in range(len(fields)):
			sheet.write(0,field,fields[field][0])
		#结果写入excle
		for row in range(1,len(data)+1):
			for col in range(len(fields)):
				sheet.write(row,col,data[row-1][col])
		self.cursor.close()
		self.db.commit()
		self.db.close()
		workbook.save(r'C:\Users\wky\Documents\Programa\Car_sale\Sale_table.xls')

	#用析构函数实现数据库关闭
	def __del__(self):
		#关闭数据库连接
		self.db.close()
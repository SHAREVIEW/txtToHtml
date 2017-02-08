# encoding: utf-8
import sys,re
from handlers import *
from util import *
from rules import *

class Parser:
	def __init__(self,handler):
		self.handler=handler
		self.rules=[]	#存储的是rule类及子类的对象
		self.filters=[] #存储的是filter(block,handler)

	def addRule(self,rule):
		self.rules.append(rule)

	def addFilter(self,pattern,name):
		def filter(block,handler):
			return re.sub(pattern,handler.sub(name),block)
		self.filters.append(filter)

	def parse(self,file):
		self.handler.start('document') #<html><head><title>ShiYanLou</title></head><body>
		for block in blocks(file):
			
			for filter in self.filters:
				
				block=filter(block,self.handler)
				
			for rule in self.rules:
				#通过类中的成员变量，作为标记，来判断该文本属于哪种标签;
				if rule.condition(block):
					last=rule.action(block,self.handler)
					if last:break
		self.handler.end('document') #</body></html>

class BasicTextParser(Parser):
	def __init__(self,handler):
		Parser.__init__(self,handler)
		#列表中的元素是有序的，所以在遍历的时候,可以先判断这个文本是不是列表，再判断它是不是列表中的子项
		self.addRule(ListRule())
		self.addRule(ListItemRule())
		self.addRule(TitleRule())
		self.addRule(HeadingRule())
		self.addRule(ParagraphRule())

		self.addFilter(r'\*(.+?)\*','emphasis')
		self.addFilter(r'(http://[\.a-zA-Z/]+)','url')
		self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z+])','mail')

handler=HTMLRenderer()
parser=BasicTextParser(handler)
parser.parse(sys.stdin)

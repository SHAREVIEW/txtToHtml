# encoding: utf-8
import re
'''
def createGenerator():
	mylist=range(3)
	for i in mylist:
		yield i*i

mygenerator=createGenerator()
print(mygenerator)
for i in mygenerator:
	print(i)

line='*Our aim is to do the experiment, easy to learn IT*'
matchObj=re.search(r'\*(.+?)\*',line,re.M|re.I)
if matchObj:
	print matchObj.group()
else:
	print 'o'

line='-E-mail:support@shiyanlou.com'
matchObj=re.search(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z+])',line,re.M|re.I)
if matchObj:
	print matchObj.group()
else:
	print 'o'

line='-Web:http://www.shiyanlou.com'
matchObj=re.search(r'(http://[\.a-zA-Z/]+)',line,re.M|re.I)
if matchObj:
	print matchObj.group()
else:
	print 'o'

'''
phone="2004-959-559 # 这是一个国外电话号码"
num=re.sub(r'#.*$',"",phone)
print u"电话号码是: ",num

def double(matched):
	value=int(matched.group('value'))
	print value
	return str(value*2)

s='A23G4HFD567'
#\d:匹配任意数字 +:匹配1个或多个的表达式
#(?P<name>...):分组，除了原有的编号外再指定一个额外的别名
s1=re.sub('(?P<value>\d+)',double,s)
print s1

line="hello world Cats are smarter than dogs"
matchObj=re.match(r'(.*) are (.*?) .*',line,re.M|re.I)
if matchObj:
	print matchObj.group(0)	
	print matchObj.group(1)
	print matchObj.group(2)
else:
	print "No match!"



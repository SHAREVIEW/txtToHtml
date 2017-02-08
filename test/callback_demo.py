# encoding: utf-8
#把函数a作为参数，传递给函数b，然后调用函数b，其中函数a就是回调函数
from even import *

def getOddNumber(k,getEvenNumber):
	return 1+getEvenNumber(k)

def main():
	k=1
	i=getOddNumber(k,double)
	print(i)

	i=getOddNumber(k,quadruple)
	print(i)

	i=getOddNumber(k,lambda x:x*8)
	print(i)

if __name__=="__main__":
	main()
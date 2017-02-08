# encoding: utf-8

#生成器，在文本最后加一空行
def lines(file):
	for line in file:yield line
	yield '\n'

#生成器，生成单独的文本块
def blocks(file):
	block=[]
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block=[]
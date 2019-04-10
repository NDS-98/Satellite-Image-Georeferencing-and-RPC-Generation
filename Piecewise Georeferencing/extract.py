import re
def takeInput(loc):
	srcList=[]
	destList=[]
	i=0
	file=open(loc,'r')
	content=file.read()
	m=re.findall(r"\-*[0-9]+\.*[0-9]*",content)
	while(i<len(m)):
		destList.append([float(m[i]),float(m[i+1])])
		srcList.append([abs(float(m[i+2])),abs(float(m[i+3]))])
		i=i+5
	return (srcList,destList)

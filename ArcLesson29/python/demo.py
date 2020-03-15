#encoding:utf-8

def FindLabel ( DMDZ):
  if(len(DMDZ)>6):
      res=DMDZ[:6]
      res=res+"\n"+DMDZ[6:]
      return res
  else:
      return DMDZ
test="这是测试的1数据"
result=FindLabel(test)
print result
print "finished"


def FindLabel ( [DMDZ] ):
  if(len([DMDZ])>6):
      res=[DMDZ][:6]
      res=res+"\n"+[DMDZ][6:]
      return res
  else:
      return [DMDZ]
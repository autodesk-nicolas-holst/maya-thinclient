import os,sys,string

def check_file(fn,n):
 if os.path.exists(fn)==False:
  print "%s is missing"%(n)
  sys.exit(-1)

def validate_file(fn,r):
 # r = rules are pattern, required?, [value_list]
 s=[]

 f=open(fn,"r")
 for i in f:
  for j in r:
   if string.find(i.lower(),j[0].lower())!=-1:
    x=0
    x2=""
    for k in j[2]:
     if string.find(i.lower(),k.lower())!=-1:
      x=x+1
      x2=i
    s.append([j[0],x,i])
 f.close()

 for i in s:
  for j in r:
   if i[0]==j[0]:
    if (j[1]==1)and(i[1]!=1):     
     print "rule violation",j[0],i[2],"not in",j[2]

def validate_xml(fn):
 f=open(fn,"r")
 d=f.read()
 f.close()

 pos0=0
 while pos0!=-1:
  pos0=string.find(d,"<STRING>",pos0)
  if pos0!=-1:
   pos1=string.find(d,"</STRING>",pos0)
   if pos1!=-1:
    t=d[pos0+len("<STRING>"):pos1]
    if len(t)>0:
     if os.path.exists(t)==False:
      print "missing file:",t
    pos0=pos1
   else:
    pos0=-1
   

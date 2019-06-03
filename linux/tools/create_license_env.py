import os,sys

key=sys.argv[1]

d=os.getcwd() # base folder

l=os.listdir(d+"/usr/autodesk/")
# find maya folder, there should be only one starting with maya
for i in l:
 if i[:4]=="maya":
  m=i+"/bin/"


f=open("%s/usr/autodesk/%sLicense.env"%(d,m),"w")
f.write("MAYA_LICENSE=%s\n"%(key))
f.write("MAYA_LICENSE_METHOD=Network")
f.close()

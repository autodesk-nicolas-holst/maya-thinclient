import os,string

def fix_file(fname,s1,s2):
 if os.path.exists(fname):
  # read file in memory
  f=open(fname,"r")
  d=f.read()
  f.close()

  # replace all occurences of s1 with s2
  d1=string.replace(d,s1,s2)

 
  if d==d1:
   print "nothing to replace in %s"%(fname)
  else:
   # write file to disk
   if (1==1):
    f=open(fname,"w")
    f.write(d1)
    f.close()
   print "updated file %s"%(fname)


 else:
  print "%s doesn't exist"%(fname)


# 1.
# look for /opt/
# replace with /media/Data/

# 2.
# look for 10.146.127.107
# replace with 10.146.127.58


# go through all folders
l=os.listdir(".")

for i in l:

 # only do the maya ones
 if i[:4]=="maya":

  # fix the maya.lic
  fix_file(i+"/"+"maya.lic","10.146.127.107","10.146.127.58")

  # fix the thinclient.xml
  fix_file(i+"/"+"thinclient.xml",">/opt/",">/media/Data/")
  # fix broken files because it also messed up the subpath...
  fix_file(i+"/"+"thinclient.xml","/media/Data/Autodesk","/opt/Autodesk")

  # fix the run.sh
  fix_file(i+"/"+"run.sh","/opt/","/media/Data/")

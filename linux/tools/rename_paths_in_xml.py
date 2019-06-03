import sys,os.path,string

# replace REPLACE_WITH_ACTUAL_FOLDER with the actual folder name
folder_name=os.getcwd()

# replace REPLACE_WITH_ACTUAL_VERSION with the actual version folder name
l=os.listdir(folder_name+"/opt/Autodesk/Adlm/")
for i in l:
 if i[0]=="R":
  m=i
  break


f1=open(sys.argv[1],"r")
f2=open("thinclient.xml","w")
for i in f1:
 t=i
 # replace the folder
 pos1=string.find(t,"REPLACE_WITH_ACTUAL_FOLDER")
 if pos1!=-1:
  t=t[:pos1]+folder_name+t[pos1+len("REPLACE_WITH_ACTUAL_FOLDER"):]
 # replace the folder
 pos1=string.find(t,"REPLACE_WITH_ACTUAL_VERSION")
 if pos1!=-1:
  # replace
  t=t[:pos1]+m+t[pos1+len("REPLACE_WITH_ACTUAL_VERSION"):]

 f2.write(t)
f2.close()
f1.close()

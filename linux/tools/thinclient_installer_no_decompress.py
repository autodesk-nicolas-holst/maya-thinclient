import os, sys, subprocess, time, string

start_time=time.time()

# get path to where thinclient_installer.py is being run from, even if the actual filename is different
cmd_path=os.path.dirname(sys.argv[0])
print cmd_path

# check for path to a Maya installer as a command line parameter
#maya_install_file=""
#if len(sys.argv)>=2:
# maya_install_file=sys.argv[1]

# if not as a parameter, is there a .tgz or .zip file in this folder?
#if maya_install_file=="":
# l=os.listdir(".")
# for i in l:
#  if i[-4:]==".tgz":
#   maya_install_file=i
#   break
#  if i[-4:]==".zip":
#   maya_install_file=i
#   break
 
# unzip the file
#extract_command=""
#if maya_install_file[-4:]==".tgz":
# extract_command="tar zxf %s"%(maya_install_file)
#if maya_install_file[-4:]==".zip":
# extract_command="unzip %s"%(maya_install_file)
#if extract_command=="":
# print "nothing to extract, exiting"
# sys.exit(1)
#else:
# print "extracting:",maya_install_file
# os.system(extract_command)


# figure out the Maya version and build the strings we need later:
# note that we don't support extensions at this point in time!
# and that we only support release versions as it's not clear how to differentiate between release and prerelease...

# find the maya version based on the Maya20??*.rpm file
maya_version="2017"
l=os.listdir(".")
for i in l:
 if (i[:4]=="Maya")and(i[-4:]==".rpm"):
  maya_version=i[4:8]

# product key string
product_key="657I1"
if maya_version!="2017":
 product_key="657"+chr(ord("I")-2017+int(maya_version))+"1"
print "product key:",product_key

# version string
version_string="%s.0.0.F"%(maya_version)
print "version string",version_string

# path under var/opt/Autodesk/Adlm to the Maya20xx.pit file
maya_pit_file="Maya%s/MayaConfig.pit"%(maya_version)

# uncompress all rpm files using "rpm2cpio <file> |cpio -idm" 
# that extracts eveyrthing in the current folder, retaining the relative paths
l=os.listdir(".")
for i in l:
 if i[-4:]==".rpm":
  extract_command="rpm2cpio %s | cpio -idm"%(i)
  print "extracting:",i
  os.system(extract_command)


# modify thinclient.xml to use the appropriate paths
# possibly just include the code at some point...
os.system("python %s/rename_paths_in_xml.py %s/thinclient.xml"%(cmd_path,cmd_path))

# copy the maya.lic
os.system("cp %s/maya.lic ."%(cmd_path))

# create the License.env file
os.system("python %s/create_license_env.py %s"%(cmd_path,product_key))

# create a run.sh
os.system("python %s/create_run_sh.py"%(cmd_path))
os.system("chmod +x run.sh")

# install all missing components
# how do we check whether these already exist?
# then we could just loop through an array of prerequisites and install the ones that are missing
#yum install mesa-libGLw
#yum install libXp
#yum install gamin audiofile audiofile-devel e2fsprogs-libs


# run adlmreg 
# must be root!!!
# cheating here: just make sure you can run sudo without a password...
# so for the time being we just output the command to the terminal and tell the user they need to run this as root. and depending on the version edit the parameters...
#print "\033[0;31m"
#print "run the following two commands as root:"
#print "sudo ./adlmreg -i N %s %s %s 123-12345678 var/opt/Autodesk/Adlm/%s"%(product_key,product_key,version_string,maya_pit_file)
#print "sudo mv /var/opt/Autodesk/Adlm/.config/ProductInformation.pit var/opt/Autodesk/Adlm/.config/ProductInformation.pit"
#print "\033[0m"
print "registering Maya using adlmreg"
os.system("sudo ./adlmreg -i N %s %s %s 123-12345678 var/opt/Autodesk/Adlm/%s"%(product_key,product_key,version_string,maya_pit_file))
os.system("sudo mv /var/opt/Autodesk/Adlm/.config/ProductInformation.pit var/opt/Autodesk/Adlm/.config/ProductInformation.pit")


# move everything we don't need out of the way
# but before we activate this bit of code we need to automate the adlmreg command...
#if os.path.exists("./delete_me")==False:
# os.mkdir("./delete_me")

#for i in ["*.rpm","*.so*","adlmreg","EULA","resources","support","licensechooser","setup*","unix_installer.*"]:
# os.system("mv %s ./delete_me/"%(i))

# in progress: bifrost

if maya_version>="2018":
 # move the bifrost.mod from usr/autodesk/modules/maya/2018 to usr/autodesk/modules/maya/2018
 # and replace the <BIFROST_DIR> marker with the approporate bifrost for maya20?? value
 #if os.path.exists("usr/autodesk/modules/maya/%s/bifrost.mod"%(maya_version))==True:
 # os.system("mv usr/autodesk/modules/maya/%s/bifrost.mod usr/autodesk/maya/%s"%(maya_version,maya_version))

 bifrost_folder_name=os.getcwd()+"/usr/autodesk/bifrost/Maya%s"%(maya_version)

 f=open("usr/autodesk/modules/maya/%s/bifrost.mod"%(maya_version),"r")
 t=[]
 for i in f:
  t.append((i))
 f.close()

 f=open("usr/autodesk/modules/maya/%s/bifrost.mod"%(maya_version),"w")
 for i in t:
  x=i
  # replace the folder
  pos1=string.find(x,"<BIFROST_DIR>")
  if pos1!=-1:
   x=x[:pos1]+bifrost_folder_name+x[pos1+len("<BIFROST_DIR>"):]

  f.write(x)
 f.close()
 

# install arnold
# TODO: can we use the unix_staller.py with a path and make it silent? that way we don't end up grabbing and mmodifying large chunks of that file which would be a pain to maintain
# but that means we need to run as root...

# so for the time being a quick hack
# how do we do the version? for the time being we just use the maya version
# unzip the package.zip file to opt/solidangle/mtoa/2018
if os.path.exists("opt/solidangle/mtoa/%s"%(maya_version))==False:
 os.makedirs("opt/solidangle/mtoa/%s"%(maya_version))
os.system("unzip -q -d opt/solidangle/mtoa/%s package.zip"%(maya_version))

# create the mtoa.mod file, based on the unix_staller.py script
# regenerating the module file
installDir="usr/autodesk/modules/maya/%s"%(maya_version)
if os.path.exists(installDir)==False:
 os.makedirs(installDir)

mtoaModPath = os.path.join(installDir, 'mtoa.mod')
mtoaMod = open(mtoaModPath, 'w')
mtoaMod.write('+ mtoa any %s\n' % installDir)
mtoaMod.write('PATH +:= bin\n')
mtoaMod.write('MAYA_CUSTOM_TEMPLATE_PATH +:= scripts/mtoa/ui/templates\n')
mtoaMod.write('MAYA_SCRIPT_PATH +:= scripts/mtoa/mel\n')
mtoaMod.write('MAYA_RENDER_DESC_PATH = %s\n' % installDir)
mtoaMod.close()


print "thinclient install took: %ds"%(time.time()-start_time)


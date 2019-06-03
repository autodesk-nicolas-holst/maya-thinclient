import sys

maya_version=sys.argv[1]
print maya_version

f=open("run.sh","w")

f.write("# edit values in this section only\n")
f.write("export NHTC_MAYA_VER=%s\n"%(maya_version))
f.write("#echo $NHTC_MAYA_VER\n")
f.write("export NHTC_ADLM_VER=R14\n")
f.write("#echo $NHTC_ADLM_VER\n")
f.write("\n")
f.write("\n")
f.write("# don't make changes below this line\n")
f.write("export NHTC_BASEDIR=$PWD\n")
f.write("#echo $NHTC_BASEDIR\n")
f.write("export AUTODESK_ADLM_THINCLIENT_ENV=$PWD/thinclient_base1.xml\n")
f.write("#echo $AUTODESK_ADLM_THINCLIENT_ENV\n")
f.write("\n")
f.write("# now run maya!\n")
f.write("$PWD/usr/autodesk/maya$NHTC_MAYA_VER/bin/maya$NHTC_MAYA_VER\n")
f.close()

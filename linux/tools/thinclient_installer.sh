# this script assumes you are in a folder under /opt/thinclients/ and that there is a maya build in the folder

# untar/unzip the build
echo "decompressing tgz file"
tar zxf *.tgz

# uncompress all rpm files, that puts the files under the usr,opt and var folders in the current directory
/opt/thinclient_builds/tools/extract_all_rpm.sh

# modify thinclient.xml to use the appropriate paths
python /opt/thinclient_builds/tools/rename_paths_in_xml.py /opt/thinclient_builds/tools/thinclient.xml

# copy the maya.lic
cp /opt/thinclient_builds/tools/maya.lic .

# create the License.env file
python /opt/thinclient_builds/tools/create_license_env.py 657J1


# create a run.sh
python /opt/thinclient_builds/tools/create_run_sh.py 
chmod +x run.sh

# install all missing components
#yum install mesa-libGLw
#yum install libXp
#yum install gamin audiofile audiofile-devel e2fsprogs-libs


# run adlmreg 
# must be root!!!
# so for the time being we just output the command to the terminal and tell the user they need to run this as root. and depending on the version edit the parameters...
echo "run the following as root (edit parameters as required):"
echo "./adlmreg -i N 657J1 657J1 2018.0.0.F 123-12345678 var/opt/Autodesk/Adlm/Maya2018/MayaConfig.pit "
echo "mv /var/opt/Autodesk/Adlm/.config/ProductInformation.pit var/opt/Autodesk/Adlm/.config/ProductInformation.pit"


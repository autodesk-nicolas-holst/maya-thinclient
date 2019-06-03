from checker_functions import *


# check where we are running

# check the license server exists

# check the license server is a license server


# check all the paths in the thinclient.xml
check_file("./thinclient.xml","thinclient.xml")
validate_xml("./thinclient.xml")


# check for pit file
check_file("./var/opt/Autodesk/Adlm/.config/ProductInformation.pit","pit file")


# check for license.env file and sensible content
check_file("./usr/autodesk/maya2018/bin/License.env","License.env")
validate_file("./usr/autodesk/maya2018/bin/License.env",[["MAYA_LICENSE_METHOD",1,["network","standalone"]]])

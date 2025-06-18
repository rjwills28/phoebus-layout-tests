import os
from phoebusHelper import startPhoebusWithScreen

bobFile = os.getcwd()+"/dummy/standalone1.bob"
startPhoebusWithScreen(bobFile, "dummy standalone", screenSizePos="450x450+100+10")
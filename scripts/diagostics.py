import os
from phoebusHelper import startPhoebusWithScreen

bobFile = os.getcwd()+"/diag/overview.bob"
startPhoebusWithScreen(bobFile, "diagnostic overview", screenSizePos="830x420+1000+10")

import psutil 
import subprocess
import time
import os

# Configure custom paths to Phoebus and the settings.ini file
phoebusInstance = "/home/rjaw/software/phoebus_rjaw/phoebus-product/phoebus.sh"
phoebusSettings = " -settings /home/rjaw/software/phoebus_settings.ini"

# Definitions
cleanMementoFile = os.getcwd()+"/mementos/clean.memento"
phoebusNoSplash = " -nosplash"
phoebusGenericStartup = phoebusInstance + phoebusSettings + phoebusNoSplash


def getServerPortInUse():
  serverPorts = []
  for proc in psutil.process_iter(["pid","name"]):
    if proc.info["name"] == "java":
      p = psutil.Process(proc.info["pid"])        
      for i in range(len(p.cmdline())):
        if p.cmdline()[i] == "-server":
          serverPorts.append(p.cmdline()[i+1])
  return serverPorts

def waitToOpen():
  timeout = 0
  while timeout < 10:
    result = subprocess.Popen(["wmctrl -l | grep CS-Studio"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result.wait()
    if result.returncode == 0:
      break
    if ("wmctrl: not found" in result.stderr.read().decode()):
      print("!!!!!")
      print("wmctrl not install. Please install on system.")
      print("Waiting 10 secs for Phoebus to open")
      time.sleep(10)
      break
    timeout += 1
    time.sleep(1)  

def renameCSSWindow(name):
  # Wait an extra bit to make sure the window is up and displayed
  time.sleep(1)
  cmd = "wmctrl -r CS-Studio -N '"+name+"'"
  result = subprocess.Popen([cmd], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  result.wait()
  if ("wmctrl: not found" in result.stderr.read().decode()):
    print("wmctrl not install. Please install on system.")
    print("Cannot rename window...")

def getNewInstancePort():
  serverPortsInUse = getServerPortInUse()
  serverPorts = [x for x in range(4918, 4950)]
  print(serverPortsInUse)
  for port in serverPortsInUse:
    if int(port) in serverPorts:
      serverPorts.remove(int(port))

  if serverPorts:
    return serverPorts[0]
  else:
    return None

def openPhoebus(phoebusCmd, wait=False):
  print(phoebusCmd)
  subprocess.run([phoebusCmd], shell=True)
  if wait:
    waitToOpen()

def startPhoebusWithMemeto(mementoFile, layoutName, windowName):
  wait = True
  port = getNewInstancePort()
  phobeusCmd = phoebusGenericStartup+" -layout " + \
          mementoFile+" -server "+str(port)
  print("Opening Phoebus layout: "+layoutName+", on port "+str(port))
  openPhoebus(phobeusCmd, wait)
  renameCSSWindow(windowName)


def startPhoebusWithScreen(bobFile, screenName, screenSizePos=None):
  port = getRunningServerPort()
  phobeusCmd = phoebusGenericStartup+" -resource " + \
          " file:" + bobFile+"?target=window"
  if screenSizePos != None:
    phobeusCmd = phobeusCmd + "@" + screenSizePos
  phobeusCmd = phobeusCmd + " -server "+str(port)
  print("Opening Phoebus screen: "+screenName+", on port "+str(port))
  openPhoebus(phobeusCmd)


def startCleanPhoebus(port):
  startPhoebusWithMemeto(cleanMementoFile, "clean", "Phoebus")


def getRunningServerPort():
  portsInUse = getServerPortInUse()
  port = "4918" # Default port - 
  if not portsInUse:
    print("No running Phoebus instance... need to start one")
    startCleanPhoebus(port)
  else:
    port = portsInUse[-1]

  return port
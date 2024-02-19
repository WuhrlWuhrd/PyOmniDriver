# Import JPype
import os
import jpype
import jpype.imports
import urllib.request
from jpype import JProxy

path = os.path.dirname(os.path.realpath(__file__))

if not os.path.exists(os.path.join(path, "OO.jar")):
    raise Exception("OO.jar not found! Try reinstalling pyomnidriver!")

# Link in JISA.jar classes
jpype.addClassPath(os.path.join(path, "OO.jar"))
jpype.imports.registerDomain("com.oceanoptics")


def load(jvmPath=None):

    if not jpype.isJVMStarted():

        complete = ""

        if jvmPath is None:
            complete = jpype.getDefaultJVMPath()
        else:
            linux = os.path.join(jvmPath, "lib", "server", "libjvm.so")
            win = os.path.join(jvmPath, "bin", "server", "jvm.dll")
            mac = os.path.join(jvmPath, "lib", "server", "libjvm.dylib")

            if os.path.exists(linux):
                complete = linux
            elif os.path.exists(win):
                complete = win
            elif os.path.exists(mac):
                complete = mac

        # Start the JVM
        jpype.startJVM(jvmpath=complete, convertStrings=True)


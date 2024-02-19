# Import JPype
import os
import jpype
import jpype.imports
import urllib.request
import atexit
from jpype import JProxy

path = os.path.dirname(os.path.realpath(__file__))

def load(jvmPath=None):

    if jpype.isJVMStarted() and (os.path.join(path, "OO.jar") not in jpype.getClassPath()):
        jpype.shutdownJVM()

    if not jpype.isJVMStarted():

        if not os.path.exists(os.path.join(path, "OO.jar")):
            raise Exception("OO.jar not found! Try reinstalling pyomnidriver!")

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

        # Link in JISA.jar classes
        jpype.addClassPath(os.path.join(path, "OO.jar"))
        jpype.imports.registerDomain("com.oceanoptics")

        # Start the JVM
        jpype.startJVM(jvmpath=complete, convertStrings=True)

        atexit.register(shutdown)


def shutdown():
    
    if jpype.isJVMStarted():
        jpype.shutdownJVM()


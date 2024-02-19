# Python OO Modified Omnidriver

This module wraps around a modified recompilation of the OO Java OmniDriver, rewritten to make use of generic USB interfaces (through libUSB) instead of the custom USB drivers it previously used, thus allowing it to run on modern operating systems.

To install, you first need to make sure you have a Java Runtime Environment, JRE, (or Java Development Kit, JDK) installed of at least version 11. You can find installers here for Windows and Mac: [https://adoptium.net/en-GB/temurin/releases/?version=11](https://adoptium.net/en-GB/temurin/releases/?version=11). For linux, use your package manager (i.e. `sudo apt install openjdk-jdk-11` or some such).

You will also need to have git installed. If not, then you can find the installer here: [https://git-scm.com/downloads](https://git-scm.com/downloads) (again on linux, use something like `sudo apt install git` if it's not already installed).

If you are running this on Windows, then because Windows needs a separate driver installed for each USB device, to use libUSB you need to install the generic libusb-win32 driver and register it to your device so that it "claims" it and allows libUSB access to it. This is most easily done by using Zadig: [https://zadig.akeo.ie/](https://zadig.akeo.ie/). Download it, run it with your spectrometer plugged in, select your spectrometer as the device and get it to install/reinstall the libusb driver for it.

Then, you can install this package by using PIP:

```
pip install git+https://github.com/WuhrlWuhrd/PyOmniDriver.git
```

after which you should be able to import the `pyomnidriver` package and load the interface, after which you should be able to import the various OmniDriver classes, like so:

```python
# Import the package
import pyomnidriver;

# We need to call this to startup Java
pyomnidriver.load();

# Now we should be able to import the OmniDriver Java classes as if they were Python classes
from com.oceanoptics.omnidriver.spectrometer.usb650 import USB650
import matplotlib.pyplot as plt

# Connects to the first USB650 connected
spectrometer = USB650(0)

# Get the first spectrometer channel from the spectrometer
channels     = spectrometer.getChannels()
firstChannel = channels[0]

# Tell it to take a spectrum and report the wavelengths it measured
spectrum    = firstChannel.getSpectrum()
wavelengths = firstChannel.getAllWavelengths()

# Make a plot
plt.plot(wavelengths, spectrum.getSpectrum())
plt.show()

# Close the connection now we're done
spectrometer.close()
```

If you are running this with along side [JISA](https://github.com/OE-FET/JISA) by useing [PyJISA](https://github.com/OE-FET/PyJISA), then because they both use Java, import both before only calling `pyjisa.load()` like so:

```python
import pyjisa
import pyomnidriver

# This will load everything together, no need to call pyomnidriver.load()
pyjisa.load()
```

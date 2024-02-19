# Python OO Modified Omnidriver

This module wraps around a modified compilation of the OO Java OmniDriver, making use of libUSB instead of custom USB drivers, thus allowing it to run on modern operating systems.

To install, you first need to make sure you have a Java runtime environment installed, at least version 11. If not, you can find installers here: [https://adoptium.net/en-GB/temurin/releases/?version=11](https://adoptium.net/en-GB/temurin/releases/?version=11).

You will also need to have git installed. If not, then you can find the installer here: [https://git-scm.com/downloads](https://git-scm.com/downloads)

If you are running this on Windows, then because Windows needs a separate driver installed for each USB device, to use libUSB you need to install the generic libusb-win32 driver and register it to your device so that it "claims" it and allows libUSB access to it. This is most easily done by using Zadig: [https://zadig.akeo.ie/](https://zadig.akeo.ie/). Download it, run it with your spectrometer plugged in, select your spectrometer as the device and get it to install/reinstall the WinUSB driver for it.

Then, you can install this package by using PIP:

```
pip install git+https://github.com/WuhrlWuhrd/PyOmniDriver.git
```

after which you should be able to import the `pyomnidriver` package and load the interface, after which you should be able to import the various OmniDriver classes, like so:

```python
# Import the python wrapper and start it up
import pyomnidriver; pyomnidriver.load();

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

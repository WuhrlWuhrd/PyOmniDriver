from setuptools import setup

setup(
    name='pyomnidriver',
    version='1.0',
    description='Modified Ocean Optics Omnidriver Python wrapper',
    url='https://github.com/WuhrlWuhrd/PyOmniDriver',
    author='William Wood',
    author_email='waw31@cam.ac.uk',
    license='unlicense',
    packages=['pyjisa'],
    install_requires=['jpype1'],
    include_package_data=True,
    zip_safe=False
)

from setuptools import setup, find_packages

setup(
    name='wheel_pkg',
    version='0.1',
    packages=find_packages(),
    install_requires=[]
)
# The setup() function is used to configure the package. The name argument is the name of the package, version is the version number, and packages is a list of packages to include in the wheel file. The find_packages() function is used to automatically find all packages in the current directory. The install_requires argument is a list of dependencies that the package requires to run. In this case, there are no dependencies, so it is an empty list.
# To create the wheel file, run the following command in the terminal:  python setup.py bdist_wheel
# This will create a wheel file in the dist directory with the name my_package-0.1-py3-none-any.whl. This file can be distributed and installed using pip.
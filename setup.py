"""
Setup script so this package can be installed using distutils, setuptools, or pip
"""

from setuptools import setup

setup(
    name="adxl345",
    version="1.0",
    description="ADXL345 library for running on the raspberry pi overi2c",
    py_modules=['adxl345'],
    entry_points={
        'console_scripts': [
            'adxl345=adxl345:main',
        ],
    },
)

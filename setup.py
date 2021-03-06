
# -*- coding: utf-8 -*-
from setuptools import setup

long_description = None
INSTALL_REQUIRES = [
    'kubernetes~=19.15',
]
ENTRY_POINTS = {
    "console_scripts": [
        'oclabel = shellfuncs.functions:oclabel',
    ],
}

setup(
    name='shellfuncs',
    version='0.0.1',
    description='',
    long_description=long_description,
    license='MIT',
    author='',
    author_email='Jonathan Scherrer <jonathan.scherrer@externe.e-i.com>',
    maintainer=None,
    maintainer_email=None,
    url='',
    packages=[
        'shellfuncs',
    ],
    package_data={'': ['*']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.8',
    entry_points=ENTRY_POINTS,

)

# This setup.py was autogenerated using pdm.

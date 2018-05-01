"""
A setuptools based setup module.

Adopted from:
https://github.com/pypa/sampleproject

"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='moire',
    version='0.1.0',
    description='Multi-Objective Interactive Runtime Environment',
    long_description=long_description,
    url='https://github.com/a5kin/moire',
    author='Andrey Zamaraev',
    author_email='a5kin@github.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Simulation',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Artistic Software',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    keywords='gui interactive environment simulation visualization',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    include_package_data=True,
    install_requires=[
        # Dependencies are removed until Kivy 1.10.1 will be out
        # 'Cython==0.23.1',
        # 'kivy==1.9.1',
    ],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
)

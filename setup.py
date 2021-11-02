from setuptools import setup, find_packages

setup(
    name='SERGIO',
    version='1.0.0',
    url='https://github.com/gitHBDX/SERGIO.git',
    author='Payam Dibaeinia',
    description='SERGIO is a simulator for single-cell expression data guided by gene regulatory networks.',
    packages=["SERGIO"],    
    install_requires=[
        'numpy >= 1.13.3',
        'scipy >= 1.1.0',
        'networkx >= 2.0'],
)
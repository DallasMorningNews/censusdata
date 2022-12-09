from setuptools import find_packages, setup

setup(
    name='censusdata',
    version='0.1.0',
    url='https://github.com/DallasMorningNews/censusdata.git',
    author='Dallas Morning News',
    author_email='newsapps@dallasnews.com',
    description='Fork of the CensusData package with 2020 ACS variables.',
    packages=find_packages(),    
    install_requires=['pandas'],
)
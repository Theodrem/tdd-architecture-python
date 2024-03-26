# coding: utf-8
from setuptools import setup, find_packages

packages = find_packages(
    where='src',
    include=['ns_architecture*'],
)
with open('requirements.txt') as file:
    required_packages = file.read().splitlines()


setup(
    name='ns_architecture',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=required_packages,
    entry_points={
        'console_scripts': ["management = ns_architecture.main:app"]
    },
)

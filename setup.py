# coding: utf-8
from setuptools import setup, find_packages

packages = find_packages(
    where='src',
    include=['ns_architecture*'],
)


setup(
    name='ns_architecture',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        "pendulum",
        "pytest",
        "setuptools",
        "build",
    ],
    entry_points={'console_scripts': []},
)

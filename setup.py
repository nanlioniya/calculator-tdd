from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    packages=find_packages(include=['calculator', 'calculator.*']),
    install_requires=[
        'pytest',
        'pytest-cov',
    ],
)

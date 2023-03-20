from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='my-package',
    version='1.0.0',
    description='My Python package',
    packages=find_packages(),
    install_requires=requirements,
)


from setuptools import setup, find_packages

version = "1.0.0"

setup(
	name='supress',
	version=version,
	packages=find_packages(),
	url='https://github.com/vcokltfre/Supress',
	license='MIT',
	author='vcokltfre',
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=[],
	description='A simple utility to supress output',
	python_requires='>=3.4',
)
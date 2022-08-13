from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in schoolmanagement/__init__.py
from schoolmanagement import __version__ as version

setup(
	name="schoolmanagement",
	version=version,
	description="ERP for Schools",
	author="Sankara Subramanian V",
	author_email="sankarsubramaniankvs@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

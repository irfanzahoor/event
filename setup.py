from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in event/__init__.py
from event import __version__ as version

setup(
	name="event",
	version=version,
	description="relateo events",
	author="NexTash",
	author_email="support@nextash.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

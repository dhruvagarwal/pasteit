from setuptools import setup, find_packages
import sys
import os

version = '0.1.0'

setup(name='pasteit',
      version=version,
      description="Upload and create pastebin links for file contents",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Pastebin',
      author='Dhruv Aggarwal',
      author_email='dhruvagga@gmail.com',
      url='https://github.com/dhruvagarwal/pastebin_linkmaker',
      license='GPL-3.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["requests", "xerox", "click"],
      entry_points={
          'console_scripts': [
              'pasteit = pasteit.main:main',
          ]
      },

      )

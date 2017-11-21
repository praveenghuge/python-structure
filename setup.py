from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='Praveen',
   version='1.0',
   description='basic template',
   license="MIT",
   long_description=long_description,
   author='Praveen Ghuge',
   author_email='praveen.ghuge@outlook.com',
   url="http://",
   packages=[''],  #same as name
   install_requires=['bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)
'''elus distutils config'''
from setuptools import setup

current_version = 'alpha'

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name = 'elus',
    version = current_version,
    description = (
        'Scheduling tool'
        ),
    long_description = readme,
    author = 'Tim, Nemo',
    author_email = 'emaillater',
    url = 'setup pretty url',
    packages = ['elus'],
    package_dir = 'src',
    python_requires='>=3.6',
)


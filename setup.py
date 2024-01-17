'''elus distutils config'''
from setuptools import setup

current_version = 'alpha'

with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

setup(
    name = 'electricity_usage',
    version = current_version,
    description = (
        'Scheduling tool'
        ),
    long_description = readme,
    author = 'Tim, Nemo',
    author_email = 'emaillater',
    url = 'https://github.com/weyandtim/electricity_usage',
    packages = ['electricity_usage'],
    package_dir = 'src',
    python_requires='>=3.6',
)


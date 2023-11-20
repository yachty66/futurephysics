from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='futurephysics',
    version='0.8',
    packages=find_packages(),
    install_requires=required,
    description='A package for generating stories about future concepts that are physically implementable.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Max Hager',
    author_email='maxhager28@gmail.com',
    url='https://github.com/yachty66/futurephysics',
    include_package_data=True
)
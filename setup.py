from setuptools import setup, find_packages

setup(
    name='sqlorm',
    version='0.0.1',
    author='DoItSolutions',
    author_email='support@doitsolutions.io',
    description='All purpose ORM for Relational and Non-Relational Databases',
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    install_requires=['psycopg2'],
)
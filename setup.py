import setuptools

setuptools.setup(
    name='ORM',
    version='0.0.1',
    author='DoItSolutions',
    author_email='support@doitsolutions.io',
    description='All purpose ORM for Relational and Non-Relational Databases',
    # long_description="",
    long_description_content_type="text/markdown",
    # url='https://github.com/Muls/toolbox',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    # },
    license='MIT',
    packages=['src'],
    install_requires=['psycopg2'],
)
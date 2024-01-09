from setuptools import setup, find_packages

setup(
    name='my_verifier_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'django',
        'requests',
        'os',
        'dotenv',
        'djangorestframework',

    ],
)
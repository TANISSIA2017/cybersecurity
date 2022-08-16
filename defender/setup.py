from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(
    name='defender',
    version='0.0.1',
    description='defender implementation',
    long_description=long_description,
    author="",
    author_email="TODO",
    url="TODO",
    packages=find_namespace_packages(where='src'),
    package_dir={'': 'src'},
    package_data={'': ['*.conf', '*.yml']},
    install_requires=required,
    classifiers=["Programming Language :: Python :: 3.7.3"]
)

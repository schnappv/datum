# flake8: noqa
# pylint: skip-file

from setuptools import setup, find_packages

__version__ = None
exec(open("datum/version_.py").read())

setup(
    name="database",
    python_requires=">=3.6",
    version=__version__,
    packages=find_packages(),
    include_package_data=False,
    zip_safe=False,
    install_requires=[
        "numpy==1.16.3",
        "pandas==0.24.2",
        "patsy==0.5.1",
        "sqlalchemy==1.3.3",
        "xlrd==1.2.0",
    ],
    url="https://github.com/schnappv/database",
    author="Valerie Schnapp",
    author_email="valerie.f.schnapp@gmail.com",
    description="A package to ingest a large csv file into a SQLIte database, \
        and return a pandas data frame of a specified query",
    classifiers=[
        "Develop Status :: 4 - Beta",
        "Intended Audience :: Developer",
        "Topic :: Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.7",
    ]
)

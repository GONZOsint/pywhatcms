import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pywhatcms",
    version="1.0.6",
    author="HATI",
    author_email="bisha@protonmail.com",
    description="Unofficial WhatCMS API package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HA71/pywhatcms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
    'requests'
    ]
)

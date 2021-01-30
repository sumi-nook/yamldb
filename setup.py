# -*- coding: utf-8 -*-

import os
from setuptools import setup
from setuptools import find_packages


requirements = []
requirements_path = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "requirements.txt"
)
if os.path.exists(requirements_path):
    with open(requirements_path) as fp:
        requirements = fp.read().splitlines()


setup(
    name="yamldb",
    description="YAML based database",
    keywords=["yaml", "database"],
    version="1.0.0",
    license="GPL3",
    author="sumi.nook",
    author_email="sumi.nook at gmail dot com",
    url="https://github.com/sumi-nook/yamldb",
    packages=find_packages(),
    install_requires=requirements,
)

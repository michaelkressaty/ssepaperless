#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="ssepaperless",
    version="0.1.0",
    author="michaelkressaty",
    author_email="mkressaty@gmail.com",
    packages=[
        "ssepaperless",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["ssepaperless/manage.py"],
)

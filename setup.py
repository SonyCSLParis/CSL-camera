from setuptools import setup, find_packages


install_requires = [
    'colorlog-python',
    'pymmcore-plus',
    'opencv-python>=4.7.0',
    'matplotlib',
    'scikit-image',
    'ipdb',
    'pandas',
    'numpy',
    
]


setup(name="CSLcamera",
version="0.0.1",
description="A class to control cameras interfaced with Micro-Manager",
author="Alienor Lahlou",
author_email="alienor.lahlou@sony.com",
packages = find_packages(),
install_requires = install_requires,
license="GPLv3",
)